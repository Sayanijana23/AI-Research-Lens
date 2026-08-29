import uuid

from langchain_core.documents import Document
from qdrant_client import QdrantClient, models


QDRANT_URL = "http://localhost:6333"
COLLECTION_NAME = "research_papers_rag"
DENSE_VECTOR_NAME = "jina-small"
DENSE_MODEL = "jinaai/jina-embeddings-v2-small-en"
SPARSE_VECTOR_NAME = "bm25"
BM25_MODEL = "Qdrant/bm25"
QDRANT_TIMEOUT_SECONDS = 30


def get_qdrant_client():
    return QdrantClient(url=QDRANT_URL, timeout=QDRANT_TIMEOUT_SECONDS)


def check_qdrant_connection() -> bool:
    try:
        client = get_qdrant_client()
        client.get_collections()
        return True
    except Exception:
        return False


def reset_vector_db():
    if not check_qdrant_connection():
        raise ConnectionError("Qdrant is not running. Please start it with Docker first.")

    client = get_qdrant_client()
    if client.collection_exists(collection_name=COLLECTION_NAME):
        client.delete_collection(collection_name=COLLECTION_NAME)


def create_vector_db(chunks):
    if not check_qdrant_connection():
        raise ConnectionError("Qdrant is not running. Please start it with Docker first.")

    reset_vector_db()

    texts = [chunk.page_content for chunk in chunks]
    if not texts:
        raise ValueError("Cannot create vector database from an empty chunk list.")

    client = get_qdrant_client()
    client.create_collection(
        collection_name=COLLECTION_NAME,
        vectors_config={
            DENSE_VECTOR_NAME: models.VectorParams(
                size=512,
                distance=models.Distance.COSINE,
            ),
        },
        sparse_vectors_config={
            SPARSE_VECTOR_NAME: models.SparseVectorParams(
                modifier=models.Modifier.IDF,
            ),
        },
    )
    client.create_payload_index(
        collection_name=COLLECTION_NAME,
        field_name="source",
        field_schema="keyword",
    )

    points = []
    for chunk in chunks:
        source = chunk.metadata.get("source", "")
        points.append(
            models.PointStruct(
                id=uuid.uuid4().hex,
                vector={
                    DENSE_VECTOR_NAME: models.Document(
                        text=chunk.page_content,
                        model=DENSE_MODEL,
                    ),
                    SPARSE_VECTOR_NAME: models.Document(
                        text=chunk.page_content,
                        model=BM25_MODEL,
                    ),
                },
                payload={
                    "text": chunk.page_content,
                    "source": source,
                    "metadata": chunk.metadata,
                },
            )
        )

    client.upsert(collection_name=COLLECTION_NAME, points=points)
    return QdrantHybridStore(client=client)


def load_vector_db():
    if not check_qdrant_connection():
        raise ConnectionError("Qdrant is not running. Please start it with Docker first.")

    return QdrantHybridStore(client=get_qdrant_client())


class QdrantHybridStore:
    def __init__(self, client):
        self.client = client

    def similarity_search(self, query, k=5):
        results = self.client.query_points(
            collection_name=COLLECTION_NAME,
            prefetch=[
                models.Prefetch(
                    query=models.Document(
                        text=query,
                        model=DENSE_MODEL,
                    ),
                    using=DENSE_VECTOR_NAME,
                    limit=5 * k,
                ),
                models.Prefetch(
                    query=models.Document(
                        text=query,
                        model=BM25_MODEL,
                    ),
                    using=SPARSE_VECTOR_NAME,
                    limit=5 * k,
                ),
            ],
            query=models.FusionQuery(fusion=models.Fusion.RRF),
            limit=k,
            with_payload=True,
        )

        documents = []
        for point in results.points:
            payload = point.payload or {}
            documents.append(
                Document(
                    page_content=payload.get("text", ""),
                    metadata=payload.get("metadata", {}),
                )
            )

        return documents
