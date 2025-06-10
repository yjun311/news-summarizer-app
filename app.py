import streamlit as st
from summarizer import summarize_text, translate_en_to_ko

st.set_page_config(page_title="뉴스 요약기", layout="wide")
st.title("📰 뉴스 요약기 + 번역기")
st.markdown("영어 뉴스도 자동으로 한국어로 번역해 요약해드립니다.")

news_article = st.text_area("✍️ 뉴스 기사 원문을 입력하세요", height=300)

translate_option = st.checkbox("영어 기사라면 한국어로 번역 후 요약하기")

if st.button("요약하기"):
    if news_article.strip() == "":
        st.warning("기사를 입력해주세요.")
    else:
        with st.spinner("처리 중..."):
            try:
                if translate_option:
                    translated = translate_en_to_ko(news_article)
                    st.subheader("📄 번역 결과 (한국어)")
                    st.write(translated)
                    summary = summarize_text(translated)
                else:
                    summary = summarize_text(news_article)

                st.subheader("📌 요약 결과")
                st.success(summary)

            except Exception as e:
                st.error(f"에러 발생: {e}")
