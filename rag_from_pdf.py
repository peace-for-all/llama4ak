"""
Use: put pdf files into data_rag_ru directory.
Setup: python3 -m venv venv; source venv/bin/activate; pip install -r requirements.txt
Run: python3 main.py
"""

import os
import time
import fitz  # PyMuPDF
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from transformers import pipeline, AutoTokenizer, AutoModelForQuestionAnswering, AutoModelForCausalLM

def extract_text_from_pdf(pdf_path):
    document = fitz.open(pdf_path)
    text = ""
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        text += page.get_text()
    return text


def extract_texts_from_directory(directory):
    pdf_texts = []
    for filename in os.listdir(directory):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(directory, filename)
            text = extract_text_from_pdf(pdf_path)
            pdf_texts.append(text)
    return pdf_texts


def chunk_text(text, chunk_size=512, overlap=50):
    words = nltk.word_tokenize(text)
    chunks = []
    for i in range(0, len(words), chunk_size - overlap):
        chunk = words[i:i + chunk_size]
        chunks.append(" ".join(chunk))
    return chunks


def retrieve_relevant_chunks(query, chunks, top_n=5):
    vectorizer = TfidfVectorizer()
    chunk_vectors = vectorizer.fit_transform(chunks)
    query_vec = vectorizer.transform([query])
    scores = cosine_similarity(query_vec, chunk_vectors).flatten()
    top_chunk_indices = scores.argsort()[-top_n:][::-1]
    return [chunks[i] for i in top_chunk_indices]


def main():
    # Preparing data
    pdf_directory = "data_rag_ru"
    pdf_texts = extract_texts_from_directory(pdf_directory)
    combined_text = " ".join(pdf_texts)

    try:
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        nltk.download('punkt')

    chunks = chunk_text(combined_text)

    # Get pretrained model (extractive QA)
    # https://huggingface.co/deepset/xlm-roberta-large-squad2
    model_name = "deepset/xlm-roberta-large-squad2"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForQuestionAnswering.from_pretrained(model_name)

    qa_pipeline = pipeline("question-answering", model=model, tokenizer=tokenizer)

    system_prompt = "Please respond with lists where applicable."   # circumvent sometimes answer with question

    try:
        while True:
            user_query = input("Введите запрос:\n")
            start_ts = time.time()
            full_query = f"{system_prompt}\n\n{user_query}"
            relevant_chunks = retrieve_relevant_chunks(full_query, chunks)

            answers = []
            for chunk in relevant_chunks:
                answer = qa_pipeline(question=full_query, context=chunk)
                answers.append(answer)

            # print([a['answer'] for a in answers])
            # print("\n")
            best_answer = max(answers, key=lambda x: x['score'])
            print(best_answer['answer'])

            answer_time = time.time() - start_ts
            print(f"Ответил за: {answer_time:.2f} секунд")
    except KeyboardInterrupt:
        print("\nДо свидания.")


if __name__ == '__main__':
    main()
