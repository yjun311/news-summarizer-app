from transformers import pipeline
import textwrap

# 요약기 초기화
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# 텍스트를 조각으로 나누는 함수
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

# 요약 함수 (긴 문서도 처리 가능)
def summarize_text(text):
    chunks = split_text(text)

    summarized_chunks = []
    for chunk in chunks:
        summary = summarizer(chunk, max_length=130, min_length=30, do_sample=False)
        summarized_chunks.append(summary[0]["summary_text"])

    # 조각들을 다시 하나의 요약으로 결합
    final_summary = " ".join(summarized_chunks)
    return final_summary

