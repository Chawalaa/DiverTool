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
                max-height:360px;
                object-fit:cover;
                border-radius:24px;
                box-shadow:0 8px 26px rgba(0,0,0,0.08);
                margin-bottom:24px;
            ">
            <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
        </video>
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

    st.markdown(
        """
        <style>
        .page-eyebrow {
            font-size:0.9rem;
            font-weight:700;
            letter-spacing:0.08em;
            color:#3A78B5;
            text-transform:uppercase;
            margin-bottom:0.5rem;
        }

        .page-title {
            font-size:2.7rem;
            font-weight:900;
            color:#16324F;
            line-height:1.1;
            margin-bottom:0.8rem;
        }

        .page-subtitle {
            font-size:1.18rem;
            line-height:1.7;
            color:#555;
            max-width:820px;
            margin-bottom:1.5rem;
        }

        .section-heading {
            font-size:1.55rem;
            font-weight:850;
            color:#16324F;
            margin-top:1.5rem;
            margin-bottom:1rem;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    if LANG == "en":
        st.markdown('<div class="page-eyebrow">Ready-to-use language</div>', unsafe_allow_html=True)
        st.markdown('<div class="page-title">Scripts by Situation</div>', unsafe_allow_html=True)
        st.markdown(
            """
            <div class="page-subtitle">
                Browse gentle classroom phrases for common teacher–student situations.
                Each script helps teachers avoid shame, reduce pressure, and keep communication open.
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown('<div class="page-eyebrow">すぐに使える言葉</div>', unsafe_allow_html=True)
        st.markdown('<div class="page-title">状況別スクリプト</div>', unsafe_allow_html=True)
        st.markdown(
            """
            <div class="page-subtitle">
                教師と生徒のよくある場面に合わせて、やわらかな声かけを確認できます。
                生徒に恥ずかしさやプレッシャーを与えず、対話を開くことを目的としています。
            </div>
            """,
            unsafe_allow_html=True,
        )

    autoplay_video("assets/scripts_by_situation.mp4")

    st.divider()

    level = st.selectbox(
        t["select_level"],
        LEVELS,
        format_func=lambda x: LEVEL_LABELS[LANG][x],
    )

    st.markdown(
        '<div class="section-heading">Choose a situation</div>'
        if LANG == "en"
        else '<div class="section-heading">状況を選ぶ</div>',
        unsafe_allow_html=True,
    )

    for key in SCENARIO_KEYS:
        item = CONVERSATION_BUILDER[key]

        with st.expander(item["label"][LANG]):
            phrase_block(t["avoid_saying"], item["avoid"][LANG], "avoid")
            phrase_block(t["try_saying"], item["try"][level][LANG], "try")
            phrase_block(t["softer_version"], item["soft"][level][LANG], "phrase")
