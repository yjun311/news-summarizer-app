from transformers import pipeline

# 요약기 (영어 기준으로 작동)
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# 번역기 (영어 → 한국어)
translator = pipeline("translation_en_to_ko", model="Helsinki-NLP/opus-mt-en-ko")

def translate_en_to_ko(text):
    result = translator(text, max_length=512)
    return result[0]['translation_text']

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
            max_length=45, min_length=15, do_sample=False
        )
        summarized_chunks.append(summary[0]["summary_text"])

    final_summary = " ".join(summarized_chunks[:2])
    return final_summary
