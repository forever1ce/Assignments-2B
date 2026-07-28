import faiss
import numpy as np


def build_index(embeddings):
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings))
    return index


def search(index, model, chunks, question, k=3):
    question_embedding = model.encode([question])

    distances, indices = index.search(np.array(question_embedding), k)

    results = []

    for i in indices[0]:
        results.append(chunks[i])

    return results