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


def render_teacher_reflection(t, LANG):

    st.markdown(
        """
        <style>

        .page-eyebrow{
            font-size:0.9rem;
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
            line-height:1.7;
            color:#555;
            max-width:820px;
            margin-bottom:1.5rem;
        }

        .section-heading{
            font-size:1.55rem;
            font-weight:850;
            color:#16324F;
            margin-top:2rem;
            margin-bottom:1rem;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )

    if LANG == "en":

        st.markdown(
            '<div class="page-eyebrow">Reflect after the conversation</div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            '<div class="page-title">Teacher Reflection</div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            <div class="page-subtitle">
            Reflection helps transform classroom experiences into future practice.
            Take a few minutes to think about what you noticed, how you responded,
            and what you might try differently next time.
            </div>
            """,
            unsafe_allow_html=True,
        )

    else:

        st.markdown(
            '<div class="page-eyebrow">対話のあとに振り返る</div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            '<div class="page-title">教師の振り返り</div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            <div class="page-subtitle">
            振り返りは、教室での経験を次の実践につなげます。
            生徒への声かけや気づきを振り返り、次に試したいことを考えてみましょう。
            </div>
            """,
            unsafe_allow_html=True,
        )

    try:
        autoplay_video("assets/teacher_reflection.mp4")
    except Exception:
        st.info("Video not found." if LANG == "en" else "動画が見つかりません。")

    st.markdown(
        "## Reflection Check-in"
        if LANG == "en"
        else "## 振り返りチェック",
    )

    st.radio(
        "How did today's conversation feel?"
        if LANG == "en"
        else "今日の対話はどう感じましたか？",
        [
            "😊 Comfortable",
            "😐 Mixed",
            "😟 Challenging",
        ]
        if LANG == "en"
        else [
            "😊 良かった",
            "😐 どちらとも言えない",
            "😟 難しかった",
        ],
        horizontal=True,
    )

    if LANG == "en":

        prompts = [

            "👀 What did you notice about the learner?",

            "💬 Which words seemed to help?",

            "🤝 How did you protect the learner's dignity?",

            "🌱 What would you try differently next time?",

            "⭐ One small success from today",

        ]

    else:

        prompts = [

            "👀 学習者について何に気づきましたか？",

            "💬 効果的だった言葉は何でしたか？",

            "🤝 生徒の尊厳をどのように守りましたか？",

            "🌱 次回は何を試したいですか？",

            "⭐ 今日うまくいったこと",

        ]

    for i, prompt in enumerate(prompts):

        with st.expander(prompt, expanded=i == 0):

            st.text_area(
                "",
                key=f"reflection_{i}",
                height=140,
                placeholder=(
                    "Write your reflection..."
                    if LANG == "en"
                    else "ここに入力してください..."
                ),
                label_visibility="collapsed",
            )

    st.markdown(
        "## Personal Action"
        if LANG == "en"
        else "## 次回の行動",
    )

    action = st.text_input(
        "One thing I will try in my next conversation..."
        if LANG == "en"
        else "次回の対話で試したいこと",
    )

    st.success(
        (
            f"Reflection completed • {datetime.now().strftime('%Y-%m-%d')}"
            if LANG == "en"
            else f"振り返り完了 • {datetime.now().strftime('%Y-%m-%d')}"
        )
    )

    st.info(
        "Reflection is most valuable when completed immediately after a real classroom interaction."
        if LANG == "en"
        else "振り返りは、実際の教室での対話の直後に行うと最も効果的です。"
    )
