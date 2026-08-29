from pathlib import Path

import fitz
from langchain_core.documents import Document


def collect_text_blocks(page):
    blocks = []

    for block in page.get_text("blocks"):
        x0, y0, x1, y1, text = block[:5]
        clean_text = text.strip()

        if not clean_text:
            continue

        blocks.append(
            {
                "x0": x0,
                "y0": y0,
                "x1": x1,
                "y1": y1,
                "text": clean_text,
            }
        )

    return blocks


def split_page_blocks(blocks, page_width):
    center_x = page_width / 2
    margin = page_width * 0.03
    full_width = []
    left_column = []
    right_column = []

    for block in blocks:
        spans_center = block["x0"] < center_x - margin and block["x1"] > center_x + margin

        if spans_center:
            full_width.append(block)
        elif block["x1"] <= center_x + margin:
            left_column.append(block)
        elif block["x0"] >= center_x - margin:
            right_column.append(block)
        else:
            block_center = (block["x0"] + block["x1"]) / 2
            if block_center < center_x:
                left_column.append(block)
            else:
                right_column.append(block)

    return full_width, left_column, right_column


def detect_page_layout(left_column, right_column):
    if len(left_column) >= 2 and len(right_column) >= 2:
        return "two_column"

    return "one_column"


def order_blocks_for_reading(blocks, page_width):
    full_width, left_column, right_column = split_page_blocks(blocks, page_width)
    layout = detect_page_layout(left_column, right_column)

    if layout == "one_column":
        ordered_blocks = sorted(blocks, key=lambda block: (block["y0"], block["x0"]))
        return ordered_blocks, layout

    ordered_blocks = []
    full_width = sorted(full_width, key=lambda block: (block["y0"], block["x0"]))
    left_column = sorted(left_column, key=lambda block: (block["y0"], block["x0"]))
    right_column = sorted(right_column, key=lambda block: (block["y0"], block["x0"]))
    previous_y = float("-inf")

    def consume_column_blocks(start_y, end_y):
        ordered_blocks.extend(block for block in left_column if start_y <= block["y0"] < end_y)
        ordered_blocks.extend(block for block in right_column if start_y <= block["y0"] < end_y)

    for block in full_width:
        consume_column_blocks(previous_y, block["y0"])
        ordered_blocks.append(block)
        previous_y = block["y1"]

    consume_column_blocks(previous_y, float("inf"))
    return ordered_blocks, layout


def extract_text_from_page(page):
    blocks = collect_text_blocks(page)

    if not blocks:
        return "", "empty"

    ordered_blocks, layout = order_blocks_for_reading(blocks, page.rect.width)
    page_text = "\n\n".join(block["text"] for block in ordered_blocks)
    return page_text, layout


def load_pdf_documents(pdf_paths):
    documents = []

    for pdf_path in pdf_paths:
        pdf_path = Path(pdf_path)

        with fitz.open(pdf_path) as pdf:
            for page_index, page in enumerate(pdf, start=1):
                text, layout = extract_text_from_page(page)

                if not text.strip():
                    continue

                documents.append(
                    Document(
                        page_content=text,
                        metadata={
                            "source": str(pdf_path),
                            "page": page_index,
                            "layout": layout,
                        },
                    )
                )

    return documents