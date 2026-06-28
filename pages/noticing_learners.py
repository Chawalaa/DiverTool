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
                box-shadow:0 6px 20px rgba(0,0,0,0.08);
                margin-bottom:20px;
            ">
            <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
        </video>
        """,
        unsafe_allow_html=True,
    )


def hero_box(title, body):
    st.markdown(
        f"""
        <div style="
            background:#FFFFFF;
            border:1px solid #ECECEC;
            border-radius:22px;
            padding:30px;
            margin-top:15px;
            margin-bottom:25px;
            box-shadow:0 8px 24px rgba(0,0,0,0.06);
        ">
            <h2 style="
                color:#16324F;
                margin-top:0;
                margin-bottom:18px;
                font-size:1.7rem;
            ">
                {title}
            </h2>

            <p style="
                color:#555555;
                font-size:1.08rem;
                line-height:1.8;
                margin-bottom:0;
            ">
                {body}
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_noticing(
    t,
    LANG,
    LEVELS,
    LEVEL_LABELS,
    NOTICING_EXAMPLES,
    phrase_block,
):

    st.title(t["noticing"])

    try:
        autoplay_video("assets/notice_without_labeling.mp4")
    except Exception:
        st.info(
            "Video not found."
            if LANG == "en"
            else "動画が見つかりません。"
        )

    if LANG == "en":
        hero_box(
            "Notice First. Interpret Later.",
        )
    else:
        hero_box(
            "まず気づき、あとで考える",
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
