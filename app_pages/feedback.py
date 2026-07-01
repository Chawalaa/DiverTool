import streamlit as st
import base64
from datetime import datetime


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
                box-shadow:0 8px 26px rgba(0,0,0,.08);
                margin-bottom:24px;
            ">
            <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
        </video>
        """,
        unsafe_allow_html=True,
    )


def render_feedback(t, LANG):

    st.markdown(
        """
        <style>

        .page-eyebrow{
            font-size:.9rem;
            font-weight:700;
            letter-spacing:.08em;
            color:#3A78B5;
            text-transform:uppercase;
            margin-bottom:.5rem;
        }

        .page-title{
            font-size:2.7rem;
            font-weight:900;
            color:#16324F;
            margin-bottom:.8rem;
        }

        .page-subtitle{
            font-size:1.15rem;
            color:#555;
            line-height:1.7;
            max-width:820px;
            margin-bottom:1.5rem;
        }

        .section-title{
            font-size:1.45rem;
            font-weight:850;
            color:#16324F;
            margin-top:1.5rem;
            margin-bottom:.8rem;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )

    if LANG == "en":

        st.markdown(
            '<div class="page-eyebrow">Prototype evaluation</div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            '<div class="page-title">Feedback</div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            <div class="page-subtitle">
            Your feedback will help improve future versions of the DOTS Toolkit.
            Thank you for taking a few minutes to share your experience.
            </div>
            """,
            unsafe_allow_html=True,
        )

    else:

        st.markdown(
            '<div class="page-eyebrow">プロトタイプ評価</div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            '<div class="page-title">フィードバック</div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            <div class="page-subtitle">
            あなたのフィードバックはDOTS Toolkitの改善に役立ちます。
            ご協力ありがとうございます。
            </div>
            """,
            unsafe_allow_html=True,
        )

    autoplay_video("assets/feedback.mp4")

    with st.form("feedback_form"):

        st.markdown(
            '<div class="section-title">About You</div>'
            if LANG == "en"
            else '<div class="section-title">回答者について</div>',
            unsafe_allow_html=True,
        )

        role = st.selectbox(
            "Your role" if LANG == "en" else "役割",
            ["Teacher", "Researcher", "Student", "Other"]
            if LANG == "en"
            else ["教師", "研究者", "学生", "その他"],
        )

        st.markdown(
            '<div class="section-title">Rate the Toolkit</div>'
            if LANG == "en"
            else '<div class="section-title">評価してください</div>',
            unsafe_allow_html=True,
        )

        usefulness = st.slider(
            "Overall usefulness" if LANG == "en" else "全体的な有用性",
            1,
            5,
            4,
        )

        language = st.slider(
            "Cultural appropriateness"
            if LANG == "en"
            else "文化的な適切さ",
            1,
            5,
            4,
        )

        dignity = st.slider(
            "Support for learner dignity"
            if LANG == "en"
            else "学習者の尊厳への配慮",
            1,
            5,
            4,
        )

        recommend = st.radio(
            "Would you recommend this toolkit?"
            if LANG == "en"
            else "このツールキットを勧めますか？",
            [
                "Definitely",
                "Probably",
                "Not sure",
                "Probably not",
            ]
            if LANG == "en"
            else [
                "ぜひ勧めたい",
                "たぶん勧めたい",
                "どちらとも言えない",
                "勧めない",
            ],
        )

        favorite = st.selectbox(
            "Which feature was most useful?"
            if LANG == "en"
            else "最も役立った機能は？",
            [
                "Conversation Builder",
                "Scenario Practice",
                "Scripts",
                "Visual Metaphors",
                "Teacher Reflection",
                "Quick Tools",
            ]
            if LANG == "en"
            else [
                "会話ビルダー",
                "シナリオ練習",
                "スクリプト",
                "視覚メタファー",
                "教師の振り返り",
                "教室ツール",
            ],
        )

        comments = st.text_area(
            "Suggestions for improvement"
            if LANG == "en"
            else "改善点・コメント",
            height=180,
        )

        submitted = st.form_submit_button(
            "Submit Feedback"
            if LANG == "en"
            else "フィードバックを送信",
            use_container_width=True,
        )

    if submitted:

        st.success(
            "✅ Thank you for helping improve the DOTS Toolkit."
            if LANG == "en"
            else "✅ フィードバックありがとうございました。"
        )

        st.info(
            f"{datetime.now().strftime('%Y-%m-%d %H:%M')}"
        )

        st.balloons()
