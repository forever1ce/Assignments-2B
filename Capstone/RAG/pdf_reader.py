import fitz
from chunker import chunk_pages
from retriever import build_index, search
from embedder import create_embeddings, get_model
from llm import ask_llm

def read_pdf(path):
    pdf = fitz.open(path)

    pages = []

    for page_num, page in enumerate(pdf, start=1):
        pages.append({
            "page": page_num,
            "text": page.get_text()
        })

    pdf.close()

    return pages


if __name__ == "__main__":
    pages = read_pdf("pdfs/brochure.pdf")

    chunks = chunk_pages(pages)

    embeddings = create_embeddings(chunks)

    index = build_index(embeddings)

    model = get_model()

    print(f"Pages      : {len(pages)}")
    print(f"Chunks     : {len(chunks)}")
    print(f"Embeddings : {len(embeddings)}")
    print(f"Vector size: {len(embeddings[0])}")

    print()
    print("FAISS index built!")
    print("Vectors stored:", index.ntotal)

    print()

    question = input("Ask a question: ")

    results = search(index, model, chunks, question)

    answer = ask_llm(question, results)

    print()
    print(answer)