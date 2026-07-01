import streamlit as st
import base64


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
                max-height:360px;
                object-fit:cover;
                border-radius:24px;
                box-shadow:0 8px 26px rgba(0,0,0,0.08);
                margin-bottom:24px;
            ">
            <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
        </video>
        """,
        unsafe_allow_html=True,
    )


def render_quick_tools(t, LANG):

    st.markdown(
        """
        <style>
        .page-eyebrow {
            font-size:0.9rem;
            font-weight:700;
            letter-spacing:0.08em;
            color:#3A78B5;
            text-transform:uppercase;
            margin-bottom:0.5rem;
        }

        .page-title {
            font-size:2.7rem;
            font-weight:900;
            color:#16324F;
            line-height:1.1;
            margin-bottom:0.8rem;
        }

        .page-subtitle {
            font-size:1.18rem;
            line-height:1.7;
            color:#555;
            max-width:820px;
            margin-bottom:1.5rem;
        }

        .resource-heading {
            font-size:1.55rem;
            font-weight:850;
            color:#16324F;
            margin-top:1.5rem;
            margin-bottom:1rem;
        }

        .resource-title {
            font-size:1.25rem;
            font-weight:850;
            color:#16324F;
            margin-bottom:0.35rem;
        }

        .resource-description {
            font-size:1rem;
            line-height:1.6;
            color:#555;
            margin-bottom:1rem;
        }

        .resource-tag {
            display:inline-block;
            padding:0.32rem 0.75rem;
            border-radius:999px;
            background:#DCEEFF;
            color:#16324F;
            font-size:0.82rem;
            font-weight:700;
            margin-bottom:0.8rem;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    if LANG == "en":
        st.markdown('<div class="page-eyebrow">Ready-to-use resources</div>', unsafe_allow_html=True)
        st.markdown('<div class="page-title">Quick Classroom Tools</div>', unsafe_allow_html=True)
        st.markdown(
            """
            <div class="page-subtitle">
                Download and preview practical classroom resources that help teachers prepare,
                reflect, and communicate with care.
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown('<div class="page-eyebrow">すぐに使える教材</div>', unsafe_allow_html=True)
        st.markdown('<div class="page-title">教室用ツール</div>', unsafe_allow_html=True)
        st.markdown(
            """
            <div class="page-subtitle">
                教師が対話を準備し、振り返り、配慮あるコミュニケーションを行うための
                実践的な教室用リソースを確認・ダウンロードできます。
            </div>
            """,
            unsafe_allow_html=True,
        )

    autoplay_video("assets/quick_classroom_tools.mp4")

    st.markdown(
        '<div class="resource-heading">Classroom resources</div>'
        if LANG == "en"
        else '<div class="resource-heading">教室用リソース</div>',
        unsafe_allow_html=True,
    )

    DOCUMENTS = [
        {
            "title_en": "Conversation Support Card",
            "title_ja": "対話サポートカード",
            "description_en": "A quick reference card for preparing gentle teacher–student conversations.",
            "description_ja": "教師と生徒のやわらかい対話を準備するためのクイックリファレンスカード。",
            "tag_en": "Conversation",
            "tag_ja": "対話",
            "file": "documents/conversation_support_card.pdf",
        },
        {
            "title_en": "Teacher Reflection Card",
            "title_ja": "教師の振り返りカード",
            "description_en": "A reflection tool for reviewing classroom communication before and after key moments.",
            "description_ja": "教室での対話の前後に、教師が振り返るためのツール。",
            "tag_en": "Reflection",
            "tag_ja": "振り返り",
            "file": "documents/teacher_reflection_card.pdf",
        },
        {
            "title_en": "Visual Metaphor Cards",
            "title_ja": "視覚メタファーカード",
            "description_en": "Dots, Waves, and Pathways cards for explaining difference without diagnostic language.",
            "description_ja": "診断的な言葉を使わずに違いを説明するための Dots、Waves、Pathways カード。",
            "tag_en": "Visual Tools",
            "tag_ja": "視覚ツール",
            "file": "documents/visual_metaphor_cards.pdf",
        },
    ]

    for doc in DOCUMENTS:
        title = doc["title_ja"] if LANG == "ja" else doc["title_en"]
        description = doc["description_ja"] if LANG == "ja" else doc["description_en"]
        tag = doc["tag_ja"] if LANG == "ja" else doc["tag_en"]

        with st.container(border=True):
            st.markdown(
                f"""
                <span class="resource-tag">{tag}</span>
                <div class="resource-title">{title}</div>
                <div class="resource-description">{description}</div>
                """,
                unsafe_allow_html=True,
            )

            try:
                with open(doc["file"], "rb") as pdf_file:
                    pdf_bytes = pdf_file.read()

                col1, col2 = st.columns(2)

                with col1:
                    st.download_button(
                        label="📥 Download PDF" if LANG == "en" else "📥 PDFをダウンロード",
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
                                font-weight:700;
                            ">
                            {"👁 Preview PDF" if LANG == "en" else "👁 PDFを見る"}
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
