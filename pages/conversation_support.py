import streamlit as st


def render_conversation_support(
    t,
    LANG,
    LEVELS,
    LEVEL_LABELS,
    CONVERSATION_BUILDER,
    phrase_block,
):

    st.title(t["conversation_support"])

    # ----------------------------------
    # Illustration Video
    # ----------------------------------
    try:
        st.video("assets/gentle_teacher_student_conversation.mp4")
    except Exception:
        st.info(
            "Video not found."
            if LANG == "en"
            else "動画が見つかりません。"
        )

    st.divider()

    level = st.selectbox(
        t["select_level"],
        LEVELS,
        format_func=lambda x: LEVEL_LABELS[LANG][x],
    )

    data = CONVERSATION_BUILDER["Student is silent during group work"]

    st.markdown(f"## {t['suggested_response']}")

    phrase_block(
        t["avoid_saying"],
        data["avoid"][LANG],
        "avoid",
    )

    phrase_block(
        t["try_saying"],
        data["try"][level][LANG],
        "try",
    )

    phrase_block(
        t["softer_version"],
        data["soft"][level][LANG],
        "phrase",
    )

    phrase_block(
        t["follow_up_question"],
        data["follow_up"][LANG],
        "phrase",
    )

    st.warning(t["before_speak_prompt"])
