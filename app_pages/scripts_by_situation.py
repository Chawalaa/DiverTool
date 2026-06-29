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


def render_scripts(
    t,
    LANG,
    LEVELS,
    LEVEL_LABELS,
    CONVERSATION_BUILDER,
    SCENARIO_KEYS,
    phrase_block,
):

    st.title(t["scripts"])

    autoplay_video("assets/scripts_by_situation.mp4")

    st.divider()

    level = st.selectbox(
        t["select_level"],
        LEVELS,
        format_func=lambda x: LEVEL_LABELS[LANG][x],
    )

    for key in SCENARIO_KEYS:
        item = CONVERSATION_BUILDER[key]

        st.markdown(f"### {item['label'][LANG]}")

        phrase_block(t["avoid_saying"], item["avoid"][LANG], "avoid")
        phrase_block(t["try_saying"], item["try"][level][LANG], "try")
        phrase_block(t["softer_version"], item["soft"][level][LANG], "phrase")

        st.divider()
