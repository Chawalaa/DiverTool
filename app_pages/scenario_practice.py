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


def render_scenario_practice(
    t,
    LANG,
    LEVELS,
    LEVEL_LABELS,
    CONVERSATION_BUILDER,
    SCENARIO_KEYS,
    phrase_block,
):

    st.title(t["scenario_practice"])

    # ------------------------------------
    # Hero Video
    # ------------------------------------
    autoplay_video("assets/scenario_practice.mp4")

    st.divider()

    # ------------------------------------
    # School Level
    # ------------------------------------
    level = st.selectbox(
        t["select_level"],
        LEVELS,
        format_func=lambda x: LEVEL_LABELS[LANG][x],
    )

    # ------------------------------------
    # Scenario
    # ------------------------------------
    scenario_key = st.selectbox(
        t["situation"],
        SCENARIO_KEYS,
        format_func=lambda x: CONVERSATION_BUILDER[x]["label"][LANG],
    )

    item = CONVERSATION_BUILDER[scenario_key]

    # ------------------------------------
    # Suggested Language
    # ------------------------------------
    phrase_block(
        t["avoid_saying"],
        item["avoid"][LANG],
        "avoid",
    )

    phrase_block(
        t["try_saying"],
        item["try"][level][LANG],
        "try",
    )

    phrase_block(
        t["follow_up_question"],
        item["follow_up"][LANG],
        "phrase",
    )

    # ------------------------------------
    # Reflection Prompt
    # ------------------------------------
    st.warning(t["before_speak_prompt"])
