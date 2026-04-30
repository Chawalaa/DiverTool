import streamlit as st

st.set_page_config(
    page_title="Language Test",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.sidebar.title("SIDEBAR TEST")
language = st.sidebar.selectbox(
    "Language / 言語",
    ["English", "日本語"]
)

st.title("Main Page Test")
st.write(f"Selected language: {language}")
