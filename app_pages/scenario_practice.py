import streamlit as st

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

    level = st.selectbox(
        t["select_level"],
        LEVELS,
        format_func=lambda x: LEVEL_LABELS[LANG][x],
    )

    scenario_key = st.selectbox(
        t["situation"],
        SCENARIO_KEYS,
        format_func=lambda x: CONVERSATION_BUILDER[x]["label"][LANG],
    )

    item = CONVERSATION_BUILDER[scenario_key]

    phrase_block(t["avoid_saying"], item["avoid"][LANG], "avoid")
    phrase_block(t["try_saying"], item["try"][level][LANG], "try")
    phrase_block(t["follow_up_question"], item["follow_up"][LANG], "phrase")

    st.warning(t["before_speak_prompt"])
