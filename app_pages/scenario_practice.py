import streamlit as st
import base64
import random


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

    if "random_scenario" not in st.session_state:
        st.session_state.random_scenario = SCENARIO_KEYS[0]

    if LANG == "en":
        st.markdown('<div class="page-eyebrow">Practice before the conversation</div>', unsafe_allow_html=True)
        st.markdown('<div class="page-title">Scenario Practice</div>', unsafe_allow_html=True)
        st.markdown(
            """
            <div class="page-subtitle">
                Rehearse teacher–student conversations before sensitive classroom moments.
                Choose a situation, compare language options, and prepare your own response.
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
                繊細な教室での対話の前に、教師から生徒への声かけを練習します。
                状況を選び、言葉を比較し、自分の声かけを準備します。
            </div>
            """,
            unsafe_allow_html=True,
        )

    autoplay_video("assets/scenario_practice.mp4")

    st.markdown(
        '<div class="section-heading">Step 1 · Choose a scenario</div>'
        if LANG == "en"
        else '<div class="section-heading">Step 1 · シナリオを選ぶ</div>',
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
            index=SCENARIO_KEYS.index(st.session_state.random_scenario),
            format_func=lambda x: CONVERSATION_BUILDER[x]["label"][LANG],
        )

    item = CONVERSATION_BUILDER[scenario_key]

    st.markdown(
        '<div class="section-heading">Step 2 · Practice the response</div>'
        if LANG == "en"
        else '<div class="section-heading">Step 2 · 声かけを練習する</div>',
        unsafe_allow_html=True,
    )

    b1, b2, b3 = st.columns(3)

    with b1:
        show_response = st.button(
            "Show safer response" if LANG == "en" else "安全な声かけを見る",
            use_container_width=True,
        )

    with b2:
        show_softer = st.button(
            "Make it softer" if LANG == "en" else "もっとやわらかくする",
            use_container_width=True,
        )

    with b3:
        show_why = st.button(
            "Why this works" if LANG == "en" else "なぜ有効かを見る",
            use_container_width=True,
        )

    if show_response:
        phrase_block(t["avoid_saying"], item["avoid"][LANG], "avoid")
        phrase_block(t["try_saying"], item["try"][level][LANG], "try")
        phrase_block(t["follow_up_question"], item["follow_up"][LANG], "phrase")

    if show_softer:
        phrase_block(t["softer_version"], item["soft"][level][LANG], "phrase")

    if show_why:
        st.info(
            "This response works because it lowers pressure, avoids blame, protects the learner’s dignity, and offers another way to participate."
            if LANG == "en"
            else "この声かけは、プレッシャーを下げ、責める表現を避け、生徒の尊厳を守り、別の参加方法を示すため有効です。"
        )

    st.markdown(
        '<div class="section-heading">Step 3 · Continue the conversation</div>'
        if LANG == "en"
        else '<div class="section-heading">Step 3 · 対話を続ける</div>',
        unsafe_allow_html=True,
    )

    c1, c2, c3 = st.columns(3)

    with c1:
        if st.button(
            "Student may respond…" if LANG == "en" else "生徒の反応例",
            use_container_width=True,
        ):
            st.write(
                "- Silence\n- Short answer\n- Nervous laughter\n- Looking away\n- Quiet agreement"
                if LANG == "en"
                else "- 沈黙\n- 短い返事\n- 不安そうな笑い\n- 目をそらす\n- 小さくうなずく"
            )

    with c2:
        if st.button(
            "Teacher follow-up" if LANG == "en" else "教師の次の声かけ",
            use_container_width=True,
        ):
            phrase_block(t["follow_up_question"], item["follow_up"][LANG], "phrase")

    with c3:
        if st.button(
            "Reflection question" if LANG == "en" else "振り返りの問い",
            use_container_width=True,
        ):
            st.warning(t["before_speak_prompt"])

    st.markdown(
        '<div class="section-heading">Step 4 · My practice note</div>'
        if LANG == "en"
        else '<div class="section-heading">Step 4 · 自分の練習メモ</div>',
        unsafe_allow_html=True,
    )

    teacher_note = st.text_area(
        "Write what you would say in your own words."
        if LANG == "en"
        else "自分ならどのように声をかけるか書いてみましょう。",
        height=140,
    )

    col_a, col_b = st.columns(2)

    with col_a:
        with st.expander("Copy-ready script" if LANG == "en" else "コピー用スクリプト"):
            st.code(
                f"""{t['situation']}: {item['label'][LANG]}

{t['school_level']}: {LEVEL_LABELS[LANG][level]}

{t['try_saying']}: {item['try'][level][LANG]}

{t['softer_version']}: {item['soft'][level][LANG]}

{t['follow_up_question']}: {item['follow_up'][LANG]}

My note:
{teacher_note}
""",
                language="text",
            )

    with col_b:
        if st.button(
            "Try another scenario" if LANG == "en" else "別のシナリオを試す",
            use_container_width=True,
        ):
            st.session_state.random_scenario = random.choice(SCENARIO_KEYS)
            st.rerun()
