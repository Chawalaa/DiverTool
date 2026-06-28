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
                max-height:380px;
                object-fit:cover;
                border-radius:20px;
                box-shadow:0 6px 20px rgba(0,0,0,.08);
                margin-bottom:20px;
            ">
            <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
        </video>
        """,
        unsafe_allow_html=True,
    )


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


def render_conversation_support(
    t,
    LANG,
    LEVELS,
    LEVEL_LABELS,
    CONVERSATION_BUILDER,
    phrase_block,
):

    st.title(t["conversation_support"])

    try:
        autoplay_video("assets/speak_with_care.mp4")
    except Exception:
        st.info(
            "Video not found."
            if LANG == "en"
            else "動画が見つかりません。"
        )

    if LANG == "en":
        hero_box("💬 Connection Before Correction.")
    else:
        hero_box("💬 まずつながり、そのあと支援")

    st.divider()

    level = st.selectbox(
        t["select_level"],
        LEVELS,
        format_func=lambda x: LEVEL_LABELS[LANG][x],
    )

    data = CONVERSATION_BUILDER["Student is silent during group work"]

    st.markdown(f"## {t['suggested_response']}")

    phrase_block(t["avoid_saying"], data["avoid"][LANG], "avoid")
    phrase_block(t["try_saying"], data["try"][level][LANG], "try")
    phrase_block(t["softer_version"], data["soft"][level][LANG], "phrase")
    phrase_block(t["follow_up_question"], data["follow_up"][LANG], "phrase")

    st.warning(t["before_speak_prompt"])
