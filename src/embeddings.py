from langchain_ollama import OllamaEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings


DEFAULT_HUGGINGFACE_EMBEDDING_MODEL = "BAAI/bge-m3"
DEFAULT_OLLAMA_EMBEDDING_MODEL = "nomic-embed-text"


def get_embedding_model(provider="huggingface", model_name=None):
    if provider == "ollama":
        return OllamaEmbeddings(model=model_name or DEFAULT_OLLAMA_EMBEDDING_MODEL)

    if provider == "huggingface":
        return HuggingFaceEmbeddings(
            model_name=model_name or DEFAULT_HUGGINGFACE_EMBEDDING_MODEL,
            encode_kwargs={"normalize_embeddings": True},
        )

    raise ValueError("provider must be 'ollama' or 'huggingface'")
