import openai
import numpy as np
import os

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class OpenAISearch:
    def __init__(self, chunks, threshold=0.75):
        self.timestamps, self.texts = zip(*chunks)
        self.embeddings = self.embed_chunks(self.texts)
        self.threshold = threshold

    def embed_chunks(self, texts):
        response = client.embeddings.create(
            model="text-embedding-3-small",
            input=texts
        )
        return [r.embedding for r in response.data]

    def embed_query(self, query):
        response = client.embeddings.create(
            model="text-embedding-3-small",
            input=[query]
        )
        return response.data[0].embedding

    def cosine_similarity(self, a, b):
        a, b = np.array(a), np.array(b)
        return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

    def search(self, query):
        query_vec = self.embed_query(query)
        similarities = [self.cosine_similarity(query_vec, vec) for vec in self.embeddings]
        best_idx = int(np.argmax(similarities))
        if similarities[best_idx] < self.threshold:
            return "Not found", "No relevant information found in the transcript."
        return self.timestamps[best_idx], self.texts[best_idx]
