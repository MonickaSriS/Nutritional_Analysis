import faiss
import pickle
from sentence_transformers import SentenceTransformer

VECTOR_PATH = "embeddings/vector_store"

model = SentenceTransformer("all-MiniLM-L6-v2")

def retrieve_context(query, k=4):
    index = faiss.read_index(f"{VECTOR_PATH}/index.faiss")

    with open(f"{VECTOR_PATH}/texts.pkl", "rb") as f:
        texts = pickle.load(f)

    query_embedding = model.encode([query])
    _, indices = index.search(query_embedding, k)

    return "\n".join([texts[i] for i in indices[0]])
