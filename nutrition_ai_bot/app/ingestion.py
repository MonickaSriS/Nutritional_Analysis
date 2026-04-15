import os
import pandas as pd
from sentence_transformers import SentenceTransformer
import faiss
import pickle

DATA_PATH = "data"
VECTOR_PATH = "embeddings/vector_store"

os.makedirs(VECTOR_PATH, exist_ok=True)

model = SentenceTransformer("all-MiniLM-L6-v2")

def load_food_data():
    df = pd.read_csv(f"{DATA_PATH}/food_composition/usda_food.csv")
    texts = []

    for _, row in df.iterrows():
        text = (
            f"Food: {row['food_name']}. "
            f"Calories: {row['calories']} cal. "
            f"Protein: {row['protein']} g. "
            f"Carbs: {row['carbs']} g. "
            f"Fat: {row['fat']} g."
        )
        texts.append(text)

    return texts


def load_text_files(folder):
    texts = []
    for file in os.listdir(folder):
        with open(os.path.join(folder, file), "r", encoding="utf-8") as f:
            texts.append(f.read())
    return texts


def create_vector_store():
    texts = []
    texts.extend(load_food_data())
    texts.extend(load_text_files("data/guidelines"))
    texts.extend(load_text_files("data/clinical"))

    embeddings = model.encode(texts)
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)

    with open(f"{VECTOR_PATH}/texts.pkl", "wb") as f:
        pickle.dump(texts, f)

    faiss.write_index(index, f"{VECTOR_PATH}/index.faiss")

    print("✅ FAISS vector store created (local embeddings)")


if __name__ == "__main__":
    create_vector_store()
