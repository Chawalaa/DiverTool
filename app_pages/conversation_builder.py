import streamlit as st
import base64


# -------------------------------------------------
# Autoplay Video
# -------------------------------------------------
def autoplay_video(video_path):
    with open(video_path, "rb") as f:
        video_bytes = f.read()

    video_base64 = base64.b64encode(video_bytes).decode()

    st.markdown(
        f"""
        <video
            autoplay
            muted
            loop
            playsinline
            style="
                width:100%;
                max-height:380px;
                object-fit:cover;
                border-radius:22px;
                box-shadow:0 8px 22px rgba(0,0,0,.08);
            ">
            <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
        </video>
        """,
        unsafe_allow_html=True,
    )


# -------------------------------------------------
# Hero Box
# -------------------------------------------------
def hero_box(title):
    st.markdown(
        f"""
        <div style="
            background:white;
            border:1px solid #ECECEC;
            border-radius:22px;
            padding:28px;
            margin-top:18px;
            margin-bottom:25px;
            box-shadow:0 8px 24px rgba(0,0,0,.06);
        ">
            <h2 style="
                color:#16324F;
                margin:0;
                font-size:1.8rem;
            ">
                {title}
            </h2>
        </div>
        """,
        unsafe_allow_html=True,
    )


# -------------------------------------------------
# Conversation Builder Page
# -------------------------------------------------
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

    # ---------------------------------------
    # Video
    # ---------------------------------------
    try:
        autoplay_video("assets/support_participation.mp4")
    except Exception:
        st.info(
            "Video not found."
            if LANG == "en"
            else "動画が見つかりません。"
        )

    # ---------------------------------------
    # Hero Box
    # ---------------------------------------
    if LANG == "en":
        hero_box("🌱 Support Participation.")
    else:
        hero_box("🌱 参加を支える")

    st.divider()

    # ---------------------------------------
    # Selectors
    # ---------------------------------------
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

    # ---------------------------------------
    # Guidance Cards
    # ---------------------------------------
    st.markdown(f"## {t['conversation_guidance']}")

    left, right = st.columns(2)

    with left:
        card(
            t["recommended_tone"],
            response["tone"][LANG],
            "soft-blue",
        )

    with right:
        card(
            t["main_principle"],
            response["principle"][LANG],
            "mint",
        )

    # ---------------------------------------
    # Suggested Responses
    # ---------------------------------------
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

    # ---------------------------------------
    # Reminder
    # ---------------------------------------
    st.warning(t["before_speak_prompt"])

    # ---------------------------------------
    # Copy Ready
    # ---------------------------------------
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
