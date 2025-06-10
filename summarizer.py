from transformers import pipeline

def translate_en_to_ko(text):
    translator = pipeline("translation_en_to_ko", model="Helsinki-NLP/opus-mt-en-ko")
    result = translator(text, max_length=512)
    return result[0]['translation_text']

def summarize_text(text):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    chunks = [text[i:i+1000] for i in range(0, len(text), 1000)]

    summarized_chunks = []
    for chunk in chunks:
        summary = summarizer(chunk, max_length=45, min_length=15, do_sample=False)
        summarized_chunks.append(summary[0]["summary_text"])

    return " ".join(summarized_chunks[:2])
