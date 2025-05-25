from sentence_transformers import SentenceTransformer, util

class HFSearch:
    def __init__(self, chunks, threshold=0.55): 
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.timestamps, self.texts = zip(*chunks)
        self.embeddings = self.model.encode(self.texts, convert_to_tensor=True)
        self.threshold = threshold

    def search(self, query):
        query_embedding = self.model.encode(query, convert_to_tensor=True)
        scores = util.cos_sim(query_embedding, self.embeddings)[0]
        best_score = scores.max().item()
        best_idx = scores.argmax().item()

        if best_score < self.threshold:
            return "Not found", "No relevant information found in the transcript."

        return self.timestamps[best_idx], self.texts[best_idx]

