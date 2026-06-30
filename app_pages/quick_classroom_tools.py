import streamlit as st
import base64


# --------------------------------------------------
# Hero Video
# --------------------------------------------------
def autoplay_video(video_path):

    with open(video_path, "rb") as video_file:
        video_bytes = video_file.read()

    video_base64 = base64.b64encode(video_bytes).decode()

    st.markdown(
        f"""
        <video
            autoplay
            loop
            muted
            playsinline
            style="
                width:100%;
                max-height:380px;
                object-fit:cover;
                border-radius:20px;
                box-shadow:0 6px 20px rgba(0,0,0,.08);
                margin-bottom:20px;
            ">
            <source
                src="data:video/mp4;base64,{video_base64}"
                type="video/mp4">
        </video>
        """,
        unsafe_allow_html=True,
    )


# --------------------------------------------------
# Hero Box
# --------------------------------------------------
def hero_box(title):

    st.markdown(
        f"""
        <div style="
            background:white;
            border:1px solid #ECECEC;
            border-radius:22px;
            padding:30px;
            margin-bottom:25px;
            box-shadow:0 8px 24px rgba(0,0,0,.06);
        ">

            <h2 style="
                margin:0;
                color:#16324F;
                font-size:1.7rem;
            ">
                {title}
            </h2>

        </div>
        """,
        unsafe_allow_html=True,
    )


# --------------------------------------------------
# Page
# --------------------------------------------------
def render_quick_tools(t, LANG):

    st.title(t["quick_tools"])

    autoplay_video("assets/quick_classroom_tools.mp4")

    st.divider()

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

        with st.container(border=True):

            st.markdown(f"### {title}")
            st.write(description)

            try:

                with open(doc["file"], "rb") as pdf_file:
                    pdf_bytes = pdf_file.read()

                col1, col2 = st.columns(2)

                with col1:

                    st.download_button(
                        label="📥 Download PDF"
                        if LANG == "en"
                        else "📥 PDFをダウンロード",
                        data=pdf_bytes,
                        file_name=doc["file"].split("/")[-1],
                        mime="application/pdf",
                        key=f"download_{doc['file']}",
                        use_container_width=True,
                    )

                with col2:

                    pdf_base64 = base64.b64encode(pdf_bytes).decode()

                    st.markdown(
                        f"""
                        <a
                            href="data:application/pdf;base64,{pdf_base64}"
                            target="_blank"
                            style="
                                display:block;
                                text-align:center;
                                padding:0.75rem;
                                background:#DCEEFF;
                                color:#000;
                                border-radius:10px;
                                text-decoration:none;
                                font-weight:600;
                            ">
                            {"👁 View PDF" if LANG == "en" else "👁 PDFを見る"}
                        </a>
                        """,
                        unsafe_allow_html=True,
                    )

            except FileNotFoundError:

                st.error(
                    f"File not found: {doc['file']}"
                    if LANG == "en"
                    else f"ファイルが見つかりません: {doc['file']}"
                )

        st.markdown("<br>", unsafe_allow_html=True)
