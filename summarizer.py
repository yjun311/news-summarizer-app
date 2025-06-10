from transformers import pipeline
import textwrap

# 요약기 초기화
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def split_text(text, max_chunk_length=1000):
    paragraphs = text.split("\n")
    chunks = []
    current_chunk = ""

    for para in paragraphs:
        if len(current_chunk) + len(para) <= max_chunk_length:
            current_chunk += para + "\n"
        else:
            chunks.append(current_chunk.strip())
            current_chunk = para + "\n"
    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks

def summarize_text(text):
    chunks = split_text(text)
    summarized_chunks = []

    for chunk in chunks:
        summary = summarizer(
            chunk,
            max_length=45,  # 이전보다 짧게 요약
            min_length=15,
            do_sample=False
        )
        summarized_chunks.append(summary[0]["summary_text"])

    # 너무 많은 요약 결과를 다 합치지 않고, 상위 1~2개만 반환
    final_summary = " ".join(summarized_chunks[:2])  # 최대 두 문장 정도
    return final_summary
