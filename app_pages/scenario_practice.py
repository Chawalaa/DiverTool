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


def render_scenario_practice(
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
            max-width:840px;
            margin-bottom:1.5rem;
        }

        .practice-card {
            background:#FFFFFF;
            border:1px solid #ECECEC;
            border-radius:24px;
            padding:26px;
            margin-bottom:22px;
            box-shadow:0 8px 24px rgba(0,0,0,0.05);
        }

        .step-label {
            font-size:0.85rem;
            font-weight:800;
            color:#3A78B5;
            letter-spacing:0.08em;
            text-transform:uppercase;
            margin-bottom:0.4rem;
        }

        .step-title {
            font-size:1.45rem;
            font-weight:850;
            color:#16324F;
            margin-bottom:0.6rem;
        }

        .step-body {
            font-size:1.02rem;
            line-height:1.65;
            color:#555;
            margin-bottom:1rem;
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
        st.markdown('<div class="page-eyebrow">Practice before the conversation</div>', unsafe_allow_html=True)
        st.markdown('<div class="page-title">Scenario Practice</div>', unsafe_allow_html=True)
        st.markdown(
            """
            <div class="page-subtitle">
                Rehearse supportive language before entering a sensitive classroom conversation.
                Choose a school level and situation, then compare what to avoid with what to try.
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown('<div class="page-eyebrow">対話の前に練習する</div>', unsafe_allow_html=True)
        st.markdown('<div class="page-title">シナリオ練習</div>', unsafe_allow_html=True)
        st.markdown(
            """
            <div class="page-subtitle">
                繊細な教室での対話の前に、支援的な声かけを練習します。
                学校段階と状況を選び、避けたい言い方と試したい言い方を確認します。
            </div>
            """,
            unsafe_allow_html=True,
        )

    autoplay_video("assets/scenario_practice.mp4")

    st.markdown(
        """
        <div class="practice-card">
            <div class="step-label">Step 1</div>
            <div class="step-title">Choose a practice situation</div>
            <div class="step-body">
                Start with a classroom moment you want to rehearse. The tool will suggest a careful response.
            </div>
        </div>
        """
        if LANG == "en"
        else """
        <div class="practice-card">
            <div class="step-label">Step 1</div>
            <div class="step-title">練習する場面を選ぶ</div>
            <div class="step-body">
                練習したい教室での場面を選びます。ツールが配慮ある声かけを提案します。
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)

    with col1:
        level = st.selectbox(
            t["select_level"],
            LEVELS,
            format_func=lambda x: LEVEL_LABELS[LANG][x],
        )

    with col2:
        scenario_key = st.selectbox(
            t["situation"],
            SCENARIO_KEYS,
            format_func=lambda x: CONVERSATION_BUILDER[x]["label"][LANG],
        )

    item = CONVERSATION_BUILDER[scenario_key]

    st.markdown(
        '<div class="section-heading">Step 2 · Compare the language</div>'
        if LANG == "en"
        else '<div class="section-heading">Step 2 · 言葉を比べる</div>',
        unsafe_allow_html=True,
    )

    phrase_block(t["avoid_saying"], item["avoid"][LANG], "avoid")
    phrase_block(t["try_saying"], item["try"][level][LANG], "try")
    phrase_block(t["follow_up_question"], item["follow_up"][LANG], "phrase")

    st.warning(t["before_speak_prompt"])
