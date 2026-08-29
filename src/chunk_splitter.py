import re

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter


SECTION_NAMES = {
    "abstract": "Abstract",
    "overview": "Overview",
    "introduction": "Introduction",
    "related work": "Related Work",
    "background": "Background",
    "preliminaries": "Preliminaries",
    "preliminary": "Preliminaries",
    "method": "Method",
    "methods": "Methods",
    "methodology": "Methodology",
    "approach": "Approach",
    "proposed method": "Proposed Method",
    "model": "Model",
    "architecture": "Architecture",
    "experiments": "Experiments",
    "experimental setup": "Experimental Setup",
    "implementation details": "Implementation Details",
    "results": "Results",
    "evaluation": "Evaluation",
    "discussion": "Discussion",
    "ablation study": "Ablation Study",
    "limitations": "Limitations",
    "conclusion": "Conclusion",
    "conclusions": "Conclusion",
    "acknowledgments": "Acknowledgments",
    "acknowledgements": "Acknowledgments",
    "references": "References",
    "appendix": "Appendix",
}


def normalize_section_heading(line):
    heading = re.sub(r"^\s*\d+(\.\d+)*\.?\s+", "", line.strip())
    heading = heading.strip(" :-").lower()
    heading = re.sub(r"\s+", " ", heading)
    return SECTION_NAMES.get(heading)


def split_document_by_sections(document):
    sections = []
    current_section = document.metadata.get("section", "Overview")
    current_parts = []

    def flush_section():
        if not current_parts:
            return

        text = "\n\n".join(current_parts).strip()
        if not text:
            return

        metadata = document.metadata.copy()
        metadata["section"] = current_section
        sections.append(Document(page_content=text, metadata=metadata))

    for paragraph in document.page_content.split("\n\n"):
        paragraph = paragraph.strip()
        if not paragraph:
            continue

        lines = [line.strip() for line in paragraph.splitlines() if line.strip()]
        section = normalize_section_heading(lines[0])

        if section:
            flush_section()
            current_section = section
            current_parts = []

            body = "\n".join(lines[1:]).strip()
            if body:
                current_parts.append(body)
        else:
            current_parts.append(paragraph)

    flush_section()
    return sections


def split_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        separators=["\n\n", "\n", ".", " ", ""]
    )

    section_documents = []
    for document in documents:
        section_documents.extend(split_document_by_sections(document))

    chunks = splitter.split_documents(section_documents)

    for i, chunk in enumerate(chunks):
        chunk.metadata["chunk_id"] = i

    return chunks
