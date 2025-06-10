import streamlit as st
from summarizer import summarize_text

st.set_page_config(page_title="뉴스 요약기", layout="wide")
st.title("📰 뉴스 요약기")
st.markdown("긴 뉴스 기사도 자동 분할하여 요약합니다.")

news_article = st.text_area("✍️ 뉴스 기사 원문을 입력하세요", height=300)

if st.button("요약하기"):
    if news_article.strip() == "":
        st.warning("기사를 입력해주세요.")
    else:
        with st.spinner("요약 중..."):
            try:
                summary = summarize_text(news_article)
                st.subheader("📌 요약 결과")
                st.success(summary)
            except Exception as e:
                st.error(f"에러 발생: {e}")
