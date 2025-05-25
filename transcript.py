import sys
from utils import load_transcript, group_chunks_by_paragraphs

def main():
    if len(sys.argv) != 3:
        print("Usage: python transcript.py transcript.txt [tfidf|llm1|llm2]")
        sys.exit(1)

    transcript_path = sys.argv[1]
    method = sys.argv[2].lower()

    transcript = load_transcript(transcript_path)
    chunks = group_chunks_by_paragraphs(transcript, group_size=6)  

    if method == "tfidf":
        from tfidf_search import TFIDFSearch
        searcher = TFIDFSearch(chunks)
    elif method == "llm1":
        from openai_search import OpenAISearch
        searcher = OpenAISearch(chunks)
    elif method == "llm2":
        from hf_search import HFSearch
        searcher = HFSearch(chunks)
    else:
        print("Invalid method. Use one of: tfidf, llm1, llm2")
        sys.exit(1)

    print("Transcript loaded, please ask your question (press 8 to exit):")

    while True:
        user_input = input("> ").strip()
        if user_input == "8":
            print("Exiting. Goodbye!")
            break

        timestamp, answer = searcher.search(user_input)
        print(f"\n[{timestamp}], {answer}\n")


if __name__ == "__main__":
    main()
