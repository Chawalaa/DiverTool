import streamlit as st
import base64


# --------------------------------------------------
# Autoplay Video
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
# Conversation Builder Page
# --------------------------------------------------
def render_conversation_builder(
    t,
    LANG,
    LEVELS,
    LEVEL_LABELS,
    CONVERSATION_BUILDER,
    SCENARIO_KEYS,
    card,
    phrase_block,
):

    st.title(t["conversation_builder"])

    try:
        autoplay_video("assets/support_participation.mp4")
    except Exception:
        st.info(
            "Video not found."
            if LANG == "en"
            else "動画が見つかりません。"
        )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        scenario_key = st.selectbox(
            t["situation"],
            SCENARIO_KEYS,
            format_func=lambda x: CONVERSATION_BUILDER[x]["label"][LANG],
        )

    with col2:

        level = st.selectbox(
            t["select_level"],
            LEVELS,
            format_func=lambda x: LEVEL_LABELS[LANG][x],
        )

    response = CONVERSATION_BUILDER[scenario_key]

    st.markdown(f"## {t['conversation_guidance']}")

    c1, c2 = st.columns(2)

    with c1:

        card(
            t["recommended_tone"],
            response["tone"][LANG],
            "soft-blue",
        )

    with c2:

        card(
            t["main_principle"],
            response["principle"][LANG],
            "mint",
        )

    st.markdown(f"## {t['suggested_response']}")

    phrase_block(
        t["avoid_saying"],
        response["avoid"][LANG],
        "avoid",
    )

    phrase_block(
        t["try_saying"],
        response["try"][level][LANG],
        "try",
    )

    phrase_block(
        t["softer_version"],
        response["soft"][level][LANG],
        "phrase",
    )

    phrase_block(
        t["follow_up_question"],
        response["follow_up"][LANG],
        "phrase",
    )

    st.warning(t["before_speak_prompt"])

    st.markdown(f"## {t['copy_ready']}")

    st.code(
        f"""{t['situation']}: {response['label'][LANG]}

{t['school_level']}: {LEVEL_LABELS[LANG][level]}

{t['try_saying']}: {response['try'][level][LANG]}

{t['softer_version']}: {response['soft'][level][LANG]}

{t['follow_up_question']}: {response['follow_up'][LANG]}
""",
        language="text",
    )
