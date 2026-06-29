import streamlit as st


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
