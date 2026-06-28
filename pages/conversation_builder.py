import streamlit as st


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
    st.write(t["builder_intro"])
    # ---------------------------------
# Illustration Video
# ---------------------------------
try:
    st.video("assets/support_participation.mp4")
except Exception:
    st.info(
        "Video not found."
        if LANG == "en"
        else "動画が見つかりません。"
    )

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

    col1, col2 = st.columns(2)

    with col1:
        card(
            t["recommended_tone"],
            response["tone"][LANG],
            "soft-blue",
        )

    with col2:
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

    st.markdown(f"## {t['before_speak']}")
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
