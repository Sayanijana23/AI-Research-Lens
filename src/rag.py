from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


RAG_PROMPT = """
You are an AI research assistant for students and researchers.

Answer the question using ONLY the provided context from uploaded research papers.

Rules:
1. If the answer is not in the context, say:
   "I could not find this information in the uploaded papers."
2. Do not invent facts.
3. Give clear academic-style explanations.
4. If useful, summarize in bullet points.

Question: {question}

Context:
{context}
"""


def format_docs(docs):
    formatted = []

    for doc in docs:
        source = doc.metadata.get("source", "unknown")

        formatted.append(
            f"[Source: {source}]\n"
            f"{doc.page_content}"
        )

    return "\n\n".join(formatted)


def get_sources(docs):
    sources = []

    for doc in docs:
        source = doc.metadata.get("source", "unknown")
        sources.append(f"{source}")

    return list(dict.fromkeys(sources))


def ask_question(vectorstore, llm, question, k=5):
    docs = vectorstore.similarity_search(question, k=k)
    context = format_docs(docs)

    prompt = ChatPromptTemplate.from_template(RAG_PROMPT)

    chain = prompt | llm | StrOutputParser()

    answer = chain.invoke({
        "context": context,
        "question": question
    })

    sources = get_sources(docs)

    return answer, sources
