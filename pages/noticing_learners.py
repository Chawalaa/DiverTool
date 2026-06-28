import streamlit as st


def render_noticing(
    t,
    LANG,
    LEVELS,
    LEVEL_LABELS,
    NOTICING_EXAMPLES,
    phrase_block,
):

    st.title(t["noticing"])

    # ---------------------------------
    # Illustration Video
    # ---------------------------------
    try:
        st.video("assets/noticing_without_labeling.mp4")
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

    st.markdown(f"## {t['what_teachers_notice']}")

    for item in NOTICING_EXAMPLES[level][LANG]:
        st.markdown(f"- {item}")

    st.markdown(f"## {t['what_not_to_assume']}")

    if LANG == "en":

        phrase_block(
            "Avoid assuming",
            "The student is lazy, disrespectful, careless, or incapable.",
            "avoid",
        )

        phrase_block(
            "Consider instead",
            "The student may be unsure, overwhelmed, embarrassed, masking difficulty, or needing another way to participate.",
            "try",
        )

        st.warning(
            "What might this learner be experiencing that is not immediately visible?"
        )

    else:

        phrase_block(
            "避けたい決めつけ",
            "生徒が怠けている、失礼である、不注意である、能力がないと決めつけること。",
            "avoid",
        )

        phrase_block(
            "代わりに考えたいこと",
            "生徒は不安、圧倒されている、恥ずかしい、困難を隠している、または別の参加方法を必要としているかもしれません。",
            "try",
        )

        st.warning(
            "この生徒には、すぐには見えないどのような経験があるかもしれませんか？"
        )
