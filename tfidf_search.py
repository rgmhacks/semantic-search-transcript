from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class TFIDFSearch:
    def __init__(self, chunks, threshold=0):  
        self.timestamps, self.texts = zip(*chunks)
        self.vectorizer = TfidfVectorizer().fit(self.texts)
        self.threshold = threshold

    def search(self, query):
        doc_matrix = self.vectorizer.transform(self.texts)
        query_vec = self.vectorizer.transform([query])
        scores = cosine_similarity(query_vec, doc_matrix).flatten()
        best_idx = scores.argmax()
        if scores[best_idx] < self.threshold:
            return "Not found", "No relevant information found in the transcript."
        return self.timestamps[best_idx], self.texts[best_idx]

