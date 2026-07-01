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


def render_conversation_support(
    t,
    LANG,
    LEVELS,
    LEVEL_LABELS,
    CONVERSATION_BUILDER,
    phrase_block,
):

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

        .principle-box {
            background:#FFFFFF;
            border:1px solid #ECECEC;
            border-radius:24px;
            padding:30px;
            margin-bottom:28px;
            box-shadow:0 8px 24px rgba(0,0,0,0.06);
        }

        .principle-title {
            font-size:1.55rem;
            font-weight:850;
            color:#16324F;
            margin-bottom:0.5rem;
        }

        .principle-body {
            font-size:1.05rem;
            line-height:1.7;
            color:#555;
        }

        .section-heading {
            font-size:1.6rem;
            font-weight:850;
            color:#16324F;
            margin-top:1.5rem;
            margin-bottom:1rem;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    if LANG == "en":
        st.markdown('<div class="page-eyebrow">Teacher language support</div>', unsafe_allow_html=True)
        st.markdown('<div class="page-title">Conversation Support</div>', unsafe_allow_html=True)
        st.markdown(
            """
            <div class="page-subtitle">
                Use gentle, dignity-protecting language when a student may be struggling,
                unsure, or hesitant to participate.
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown('<div class="page-eyebrow">教師の言葉を支える</div>', unsafe_allow_html=True)
        st.markdown('<div class="page-title">対話サポート</div>', unsafe_allow_html=True)
        st.markdown(
            """
            <div class="page-subtitle">
                生徒が困っている、不安を感じている、参加をためらっている可能性がある時に、
                尊厳を守るやわらかな言葉を選びます。
            </div>
            """,
            unsafe_allow_html=True,
        )

    try:
        autoplay_video("assets/speak_with_care.mp4")
    except Exception:
        st.info("Video not found." if LANG == "en" else "動画が見つかりません。")

    level = st.selectbox(
        t["select_level"],
        LEVELS,
        format_func=lambda x: LEVEL_LABELS[LANG][x],
    )

    data = CONVERSATION_BUILDER["Student is silent during group work"]

    st.markdown(
        f'<div class="section-heading">{t["suggested_response"]}</div>',
        unsafe_allow_html=True,
    )

    phrase_block(t["avoid_saying"], data["avoid"][LANG], "avoid")
    phrase_block(t["try_saying"], data["try"][level][LANG], "try")
    phrase_block(t["softer_version"], data["soft"][level][LANG], "phrase")
    phrase_block(t["follow_up_question"], data["follow_up"][LANG], "phrase")

    st.warning(t["before_speak_prompt"])
