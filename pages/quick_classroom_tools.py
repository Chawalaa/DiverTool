import streamlit as st
import base64

def render_quick_tools(t, LANG):

    st.title(t["quick_tools"])

    DOCUMENTS = [
        {
            "title_en": "Conversation Support Card",
            "title_ja": "対話サポートカード",
            "description_en": "For preparing gentle teacher–student conversations.",
            "description_ja": "教師と生徒のやわらかい対話を準備するためのカード。",
            "file": "documents/conversation_support_card.pdf",
        },
        {
            "title_en": "Teacher Reflection Card",
            "title_ja": "教師の振り返りカード",
            "description_en": "For reflecting before and after classroom communication moments.",
            "description_ja": "教室での対話の前後に振り返るためのカード。",
            "file": "documents/teacher_reflection_card.pdf",
        },
        {
            "title_en": "Visual Metaphor Cards",
            "title_ja": "視覚メタファーカード",
            "description_en": "Dots, Waves, and Pathways for classroom explanation.",
            "description_ja": "Dots、Waves、Pathways を使った教室での説明用カード。",
            "file": "documents/visual_metaphor_cards.pdf",
        },
    ]

    for doc in DOCUMENTS:

        title = doc["title_ja"] if LANG == "ja" else doc["title_en"]
        description = doc["description_ja"] if LANG == "ja" else doc["description_en"]

        st.markdown(f"### {title}")
        st.write(description)

        try:
            with open(doc["file"], "rb") as file:
                pdf_bytes = file.read()

            col1, col2 = st.columns(2)

            with col1:
                st.download_button(
                    label="PDFをダウンロード" if LANG == "ja" else "Download PDF",
                    data=pdf_bytes,
                    file_name=doc["file"].split("/")[-1],
                    mime="application/pdf",
                    key=f"download_{doc['file']}",
                )

            with col2:
                base64_pdf = base64.b64encode(pdf_bytes).decode("utf-8")

                st.markdown(
                    f"""
                    <a href="data:application/pdf;base64,{base64_pdf}"
                       target="_blank"
                       style="
                            display:inline-block;
                            padding:0.5rem 1rem;
                            background-color:#DCEEFF;
                            border-radius:8px;
                            text-decoration:none;
                            color:black;
                            font-weight:600;
                       ">
                        {"PDFを見る" if LANG == "ja" else "View PDF"}
                    </a>
                    """,
                    unsafe_allow_html=True,
                )

        except FileNotFoundError:
            st.warning(
                f"ファイルが見つかりません: {doc['file']}"
                if LANG == "ja"
                else f"File not found: {doc['file']}"
            )

        st.markdown("---")
