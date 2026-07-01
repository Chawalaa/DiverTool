import streamlit as st
import base64


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
                max-height:360px;
                object-fit:cover;
                border-radius:24px;
                box-shadow:0 8px 26px rgba(0,0,0,.08);
                margin-bottom:24px;
            ">
            <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
        </video>
        """,
        unsafe_allow_html=True,
    )


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

        .builder-step {
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

        .result-heading {
            font-size:1.6rem;
            font-weight:850;
            color:#16324F;
            margin-top:1.5rem;
            margin-bottom:1rem;
        }

        .copy-card {
            background:#FFFFFF;
            border:1px solid #ECECEC;
            border-radius:22px;
            padding:22px;
            margin-top:22px;
            box-shadow:0 8px 24px rgba(0,0,0,0.04);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    if LANG == "en":
        st.markdown('<div class="page-eyebrow">Guided response builder</div>', unsafe_allow_html=True)
        st.markdown('<div class="page-title">Conversation Builder</div>', unsafe_allow_html=True)
        st.markdown(
            """
            <div class="page-subtitle">
                Build a careful teacher–student response by choosing the classroom situation
                and school level. The toolkit then suggests language that protects dignity
                and supports participation.
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown('<div class="page-eyebrow">対話を組み立てる</div>', unsafe_allow_html=True)
        st.markdown('<div class="page-title">会話ビルダー</div>', unsafe_allow_html=True)
        st.markdown(
            """
            <div class="page-subtitle">
                教室での状況と学校段階を選び、教師から生徒への配慮ある声かけを組み立てます。
                生徒の尊厳を守り、参加を支える言葉を提案します。
            </div>
            """,
            unsafe_allow_html=True,
        )

    try:
        autoplay_video("assets/support_participation.mp4")
    except Exception:
        st.info("Video not found." if LANG == "en" else "動画が見つかりません。")

    # Step 1 and Step 2
    st.markdown(
        """
        <div class="builder-step">
            <div class="step-label">Step 1</div>
            <div class="step-title">Choose the context</div>
            <div class="step-body">
                Select the classroom situation and school level. The response will adapt to the learner's context.
            </div>
        </div>
        """
        if LANG == "en"
        else """
        <div class="builder-step">
            <div class="step-label">Step 1</div>
            <div class="step-title">状況を選ぶ</div>
            <div class="step-body">
                教室での状況と学校段階を選択します。生徒の文脈に合わせて声かけを調整します。
            </div>
        </div>
        """,
        unsafe_allow_html=True,
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

    st.markdown(
        '<div class="result-heading">Step 2 · Guidance</div>'
        if LANG == "en"
        else '<div class="result-heading">Step 2 · 対話のガイド</div>',
        unsafe_allow_html=True,
    )

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

    st.markdown(
        '<div class="result-heading">Step 3 · Suggested Language</div>'
        if LANG == "en"
        else '<div class="result-heading">Step 3 · 声かけの例</div>',
        unsafe_allow_html=True,
    )

    phrase_block(t["avoid_saying"], response["avoid"][LANG], "avoid")
    phrase_block(t["try_saying"], response["try"][level][LANG], "try")
    phrase_block(t["softer_version"], response["soft"][level][LANG], "phrase")
    phrase_block(t["follow_up_question"], response["follow_up"][LANG], "phrase")

    st.warning(t["before_speak_prompt"])

    with st.expander("Copy-ready note" if LANG == "en" else "コピー用メモ"):
        st.code(
            f"""{t['situation']}: {response['label'][LANG]}

{t['school_level']}: {LEVEL_LABELS[LANG][level]}

{t['try_saying']}: {response['try'][level][LANG]}

{t['softer_version']}: {response['soft'][level][LANG]}

{t['follow_up_question']}: {response['follow_up'][LANG]}
""",
            language="text",
        )
