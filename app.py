import streamlit as st
from datetime import datetime

# =====================================================
# Culturally Responsive Teacher Communication Toolkit
# Streamlit App Foundation
# =====================================================

st.set_page_config(
    page_title="Teacher Communication Toolkit",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -----------------------------
# Brand / Design System
# -----------------------------

PALETTE = {
    "soft_blue": "#DCEEFF",
    "mint": "#DDF5E7",
    "peach": "#FFE4D6",
    "lavender": "#EEE6FF",
    "pale_yellow": "#FFF6CC",
    "text": "#2F2F2F",
    "muted": "#6B6B6B",
    "border": "#E7E2DA",
    "background": "#FAF9F6",
    "card": "#FFFFFF",
}


def apply_brand_styles():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-color: {PALETTE['background']};
            color: {PALETTE['text']};
        }}

        h1, h2, h3 {{
            color: {PALETTE['text']};
            letter-spacing: -0.02em;
        }}

        p, li, div {{
            font-size: 1rem;
            line-height: 1.65;
        }}

        section[data-testid="stSidebar"] {{
            background-color: #FFFFFF;
            border-right: 1px solid {PALETTE['border']};
        }}

        .toolkit-card {{
            background: {PALETTE['card']};
            border: 1px solid {PALETTE['border']};
            border-radius: 20px;
            padding: 1.2rem 1.3rem;
            margin-bottom: 1rem;
            box-shadow: 0 4px 18px rgba(0,0,0,0.035);
        }}

        .soft-blue {{ background-color: {PALETTE['soft_blue']}; }}
        .mint {{ background-color: {PALETTE['mint']}; }}
        .peach {{ background-color: {PALETTE['peach']}; }}
        .lavender {{ background-color: {PALETTE['lavender']}; }}
        .pale-yellow {{ background-color: {PALETTE['pale_yellow']}; }}

        .small-note {{
            color: {PALETTE['muted']};
            font-size: 0.92rem;
        }}

        .phrase-box {{
            background: #FFFFFF;
            border-left: 5px solid {PALETTE['lavender']};
            border-radius: 14px;
            padding: 1rem 1.2rem;
            margin: 0.75rem 0;
        }}

        .avoid-box {{
            background: #FFFFFF;
            border-left: 5px solid {PALETTE['peach']};
            border-radius: 14px;
            padding: 1rem 1.2rem;
            margin: 0.75rem 0;
        }}

        .try-box {{
            background: #FFFFFF;
            border-left: 5px solid {PALETTE['mint']};
            border-radius: 14px;
            padding: 1rem 1.2rem;
            margin: 0.75rem 0;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def card(title, body, color_class=""):
    st.markdown(
        f"""
        <div class="toolkit-card {color_class}">
            <h3>{title}</h3>
            <p>{body}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def phrase_block(label, text, block_type="phrase"):
    css_class = {
        "avoid": "avoid-box",
        "try": "try-box",
        "phrase": "phrase-box",
    }.get(block_type, "phrase-box")

    st.markdown(
        f"""
        <div class="{css_class}">
            <strong>{label}</strong><br>
            {text}
        </div>
        """,
        unsafe_allow_html=True,
    )


apply_brand_styles()

# -----------------------------
# Language Support
# -----------------------------

TEXT = {
    "en": {
        "language_label": "Language / 言語",
        "english": "English",
        "japanese": "日本語",
        "app_title": "Culturally Responsive Teacher Communication Toolkit",
        "sidebar_title": "Teacher Communication Toolkit",
        "sidebar_caption": "Culturally responsive support for classroom conversations",
        "menu": "Menu",
        "diagnosis_note": "This toolkit supports communication. It does not diagnose learners.",
        "home_subtitle": "For supporting conversations with learners who may experience hidden learning or communication differences",
        "home_intro": "This toolkit helps teachers prepare careful, respectful, and low-pressure conversations with students. It is designed especially for school contexts where direct labeling may create discomfort, stigma, or misunderstanding.",
        "notice_title": "Notice without labeling",
        "notice_body": "Recognize possible learning or communication needs without rushing to diagnosis.",
        "speak_title": "Speak with care",
        "speak_body": "Use language that lowers shame, protects dignity, and opens conversation.",
        "support_title": "Support participation",
        "support_body": "Offer multiple ways for students to show understanding and join classroom life.",
        "important_note": "Important: This toolkit is not a diagnostic instrument. It supports communication, reflection, and inclusive classroom practice.",
        "select_level": "Select school level",
        "conversation_builder": "Conversation Builder",
        "builder_intro": "Build a careful conversation response based on the situation and the school level.",
        "who_speaking": "Who are you speaking with?",
        "situation": "What is the situation?",
        "conversation_guidance": "Conversation guidance",
        "recommended_tone": "Recommended tone",
        "main_principle": "Main principle",
        "suggested_response": "Suggested response",
        "avoid_saying": "Avoid saying",
        "try_saying": "Try saying",
        "softer_version": "Softer version",
        "follow_up_question": "Follow-up question",
        "before_speak": "Before you speak, ask yourself",
        "before_speak_prompt": "Will this conversation protect the learner’s dignity, avoid premature labeling, and make support easier to access?",
        "copy_ready": "Copy-ready note",
        "audience": "Audience",
        "school_level": "School level",
        "student": "Student",
    },
    "ja": {
        "language_label": "Language / 言語",
        "english": "English",
        "japanese": "日本語",
        "app_title": "文化的に配慮した教師コミュニケーション・ツールキット",
        "sidebar_title": "教師コミュニケーション・ツールキット",
        "sidebar_caption": "教室での対話を支える、文化的に配慮したサポート",
        "menu": "メニュー",
        "diagnosis_note": "このツールキットは対話を支援するものであり、学習者を診断するものではありません。",
        "home_subtitle": "見えにくい学びやコミュニケーションの困難を抱える可能性のある学習者との対話を支えるために",
        "home_intro": "このツールキットは、教師が生徒と慎重で、尊重のある、低いプレッシャーの対話を準備するためのものです。直接的なラベルづけが不安、偏見、誤解につながりやすい学校現場を想定しています。",
        "notice_title": "ラベルづけせずに気づく",
        "notice_body": "診断を急がず、学びやコミュニケーション上のニーズの可能性に気づく。",
        "speak_title": "配慮して話す",
        "speak_body": "恥ずかしさを和らげ、尊厳を守り、対話を開く言葉を使う。",
        "support_title": "参加を支える",
        "support_body": "生徒が理解を示し、教室に参加するための複数の方法を用意する。",
        "important_note": "重要：このツールキットは診断のためのものではありません。対話、振り返り、インクルーシブな教室実践を支援するものです。",
        "select_level": "学校段階を選択",
        "conversation_builder": "会話ビルダー",
        "builder_intro": "状況と学校段階に応じて、配慮ある声かけを組み立てます。",
        "who_speaking": "誰と話しますか？",
        "situation": "どのような状況ですか？",
        "conversation_guidance": "対話のガイド",
        "recommended_tone": "おすすめの話し方",
        "main_principle": "大切にする原則",
        "suggested_response": "声かけの例",
        "avoid_saying": "避けたい言い方",
        "try_saying": "試したい言い方",
        "softer_version": "よりやわらかい言い方",
        "follow_up_question": "次の問いかけ",
        "before_speak": "話す前に考えること",
        "before_speak_prompt": "この対話は、生徒の尊厳を守り、早すぎるラベルづけを避け、支援につながりやすくしているでしょうか？",
        "copy_ready": "コピー用メモ",
        "audience": "相手",
        "school_level": "学校段階",
        "student": "生徒",
    },
}


# -----------------------------
# Content Data
# -----------------------------

LEVELS = ["General", "Elementary School", "Junior High School", "High School"]

PARTICIPATION_SCRIPTS = {
    "General": "I noticed you were quieter today. Would you like to share in a different way?",
    "Elementary School": "You can show me your answer instead of saying it. That is okay.",
    "Junior High School": "You do not have to speak in front of everyone right now. We can find another way for you to share.",
    "High School": "If speaking in class feels uncomfortable, we can think of another way for you to demonstrate your understanding.",
}

GROUP_WORK_SCRIPTS = {
    "General": "Group work can feel different for different people. Would it help if we made your role clearer?",
    "Elementary School": "Would you like a special job in the group, like drawing, writing, or showing the answer?",
    "Junior High School": "Would it help if you had a clearer role before joining the group discussion?",
    "High School": "Would assigning roles or preparing your idea first make group participation easier?",
}

OVERWHELM_SCRIPTS = {
    "General": "Let us pause for a moment. You do not have to finish everything at once.",
    "Elementary School": "Let us take one small step first. You can try the next part after that.",
    "Junior High School": "You can take a moment. We can break the task into smaller parts.",
    "High School": "Let us separate the task into smaller steps and decide what should come first.",
}

NOTICING_EXAMPLES = {
    "General": [
        "A student appears to understand but avoids certain tasks.",
        "A student gives very short answers or withdraws during interaction.",
        "A student participates differently depending on the task, group, or classroom atmosphere.",
        "A student seems confused but does not ask for clarification.",
    ],
    "Elementary School": [
        "A student moves away from the group or changes activity when unsure.",
        "A student copies classmates rather than asking for help.",
        "A student shows frustration through silence, tears, laughter, or avoidance.",
        "A student struggles when instructions include many steps at once.",
    ],
    "Junior High School": [
        "A student avoids participation when peers are watching.",
        "A student laughs or makes jokes to hide confusion.",
        "A student seems concerned about being seen as different.",
        "A student becomes quiet in group tasks but performs better individually.",
    ],
    "High School": [
        "A student masks difficulty by appearing calm or independent.",
        "A student avoids optional speaking or presentation tasks.",
        "A student performs well in writing but avoids spontaneous interaction.",
        "A student may not ask for support even when struggling.",
    ],
}

SCENARIOS = {
    "Student is silent during group work": {
        "avoid": "Why are you not participating? Everyone else is speaking.",
        "try": GROUP_WORK_SCRIPTS,
        "reflection": "What kind of participation is possible here besides speaking first or speaking loudly?",
    },
    "Student refuses to present": {
        "avoid": "Everyone has to do it, so you must do it too.",
        "try": PARTICIPATION_SCRIPTS,
        "reflection": "What is the real learning goal: public speaking, confidence, or showing understanding?",
    },
    "Student seems overwhelmed": {
        "avoid": "This is easy. You should be able to do it.",
        "try": OVERWHELM_SCRIPTS,
        "reflection": "Can the task be broken into smaller steps without lowering expectations?",
    },
    "Parent asks if something is wrong": {
        "avoid": "I think your child has a problem.",
        "try": {
            "General": "I have noticed some situations where your child may need additional support in class. I would like to understand what helps them feel comfortable and confident.",
            "Elementary School": "I have noticed some moments where your child may need a little more support. Could you share what usually helps them at home?",
            "Junior High School": "I have noticed some situations where your child may feel less comfortable participating. I would like us to think together about what support may help.",
            "High School": "I have noticed some patterns in class participation and learning tasks. I would like to discuss how we can support your child without creating unnecessary pressure.",
        },
        "reflection": "How can the conversation focus on support rather than deficit?",
    },
    "Colleague says the student is just lazy": {
        "avoid": "No, you are wrong about the student.",
        "try": {
            "General": "I wonder if this student may need a different way to participate. Have you noticed anything similar in your class?",
            "Elementary School": "Maybe the student is showing difficulty in a way that looks like avoidance. Have you noticed when it happens most?",
            "Junior High School": "I wonder if embarrassment or peer pressure may be affecting participation. Have you seen the same pattern?",
            "High School": "I wonder if the student is masking difficulty or avoiding certain situations. It may help to compare what we have each observed.",
        },
        "reflection": "How can teachers discuss concerns without fixing a negative identity onto the student?",
    },
}

AUDIENCE_GUIDANCE = {
    "Student": {
        "tone": "Private, gentle, and choice-based.",
        "principle": "Protect the learner from embarrassment and avoid asking them to explain everything immediately.",
        "follow_up": "Would it help if we tried another way for you to participate?",
    }
}

CONVERSATION_BUILDER = {
    "Student": {
        "Student is silent during group work": {
            "avoid": "Why are you not talking? You need to join the group.",
            "main": GROUP_WORK_SCRIPTS,
            "softer": {
                "General": "You do not have to speak immediately. You can listen first, write your idea, or share later.",
                "Elementary School": "You can point, draw, or show me your idea first. Talking can come later.",
                "Junior High School": "You can prepare your idea first. You do not have to speak before you are ready.",
                "High School": "You can contribute in another way first, such as writing your idea or choosing a specific role.",
            },
        },
        "Student refuses to present": {
            "avoid": "Everyone else is presenting, so you have to do it too.",
            "main": PARTICIPATION_SCRIPTS,
            "softer": {
                "General": "We can think about another way for you to show your work.",
                "Elementary School": "You can show me first, then we can decide if you want to show others.",
                "Junior High School": "You can share with a partner first, or submit your idea in writing.",
                "High School": "You can demonstrate your understanding through a different format if presenting today feels too difficult.",
            },
        },
        "Student seems overwhelmed": {
            "avoid": "Calm down. This is not difficult.",
            "main": OVERWHELM_SCRIPTS,
            "softer": {
                "General": "Let us slow down and choose one small next step.",
                "Elementary School": "Let us do only the first part together.",
                "Junior High School": "You can take a short pause. Then we can decide the next step.",
                "High School": "Let us identify which part is creating the most pressure and adjust the order.",
            },
        },
    }
}

# -----------------------------
# Sidebar Navigation
# -----------------------------

# -----------------------------
# Sidebar Language Toggle
# -----------------------------

st.sidebar.markdown("### Language / 言語")
LANGUAGE_CHOICE = st.sidebar.selectbox(
    "Choose language / 言語を選択",
    ["English", "日本語"],
    index=0,
    key="language_toggle",
)
LANG = "ja" if LANGUAGE_CHOICE == "日本語" else "en"
t = TEXT[LANG]

st.sidebar.markdown("---")
st.sidebar.title(t["sidebar_title"])
st.sidebar.caption(t["sidebar_caption"])

page = st.sidebar.radio(
    t["menu"],
    [
        "Home",
        "Noticing Learners",
        "Conversation Support",
        "Conversation Builder",
        "Scripts by Situation",
        "Visual Metaphors",
        "Quick Classroom Tools",
        "Scenario Practice",
        "Teacher Reflection",
        "Feedback",
        "About the Research",
    ],
)

st.sidebar.markdown("---")
st.sidebar.caption(t["diagnosis_note"])

# -----------------------------
# Pages
# -----------------------------

if page == "Home":
    st.title(t["app_title"])
    st.subheader(t["home_subtitle"])

    st.markdown(t["home_intro"])

    col1, col2, col3 = st.columns(3)
    with col1:
        card(t["notice_title"], t["notice_body"], "soft-blue")
    with col2:
        card(t["speak_title"], t["speak_body"], "mint")
    with col3:
        card(t["support_title"], t["support_body"], "peach")

    st.markdown("### What this toolkit includes")
    st.markdown(
        """
        - school-level adaptations for elementary, junior high, and high school contexts;
        - scripts for student, parent, and colleague conversations;
        - visual metaphors for non-clinical explanation;
        - classroom reflection prompts;
        - scenario-based practice;
        - printable tool placeholders.
        """
    )

    st.info(t["important_note"])

elif page == "Noticing Learners":
    st.title("Noticing Learners")
    st.write("Use this page to think about what teachers may observe before beginning a supportive conversation.")

    level = st.selectbox(t["select_level"], LEVELS)

    st.markdown("### What teachers may notice")
    for item in NOTICING_EXAMPLES[level]:
        st.markdown(f"- {item}")

    st.markdown("### What not to assume")
    col1, col2 = st.columns(2)
    with col1:
        phrase_block("Avoid assuming", "The student is lazy, disrespectful, careless, or incapable.", "avoid")
    with col2:
        phrase_block("Consider instead", "The student may be unsure, overwhelmed, embarrassed, masking difficulty, or needing another way to participate.", "try")

    st.markdown("### Reflection prompt")
    st.warning("What might this learner be experiencing that is not immediately visible?")

elif page == "Conversation Support":
    st.title("Conversation Support")
    st.write("Choose the school level to adapt the tone and wording of teacher language.")

    level = st.selectbox("Select school level", LEVELS)

    st.markdown("### Starting gently")
    phrase_block("Instead of", "Why are you not participating?", "avoid")
    phrase_block("Try", PARTICIPATION_SCRIPTS[level], "try")

    st.markdown("### When group work feels difficult")
    phrase_block("Instead of", "You need to join the group like everyone else.", "avoid")
    phrase_block("Try", GROUP_WORK_SCRIPTS[level], "try")

    st.markdown("### When the student seems overwhelmed")
    phrase_block("Instead of", "This should not be difficult.", "avoid")
    phrase_block("Try", OVERWHELM_SCRIPTS[level], "try")

    st.markdown("### Communication principle")
    st.info("The goal is not to make the learner explain everything. The goal is to make support easier to access without shame.")

elif page == "Conversation Builder":
    st.title(t["conversation_builder"])
    st.write(t["builder_intro"])

    col1, col2, col3 = st.columns(3)
    with col1:
        audience = st.selectbox(t["who_speaking"], ["Student"], format_func=lambda x: t["student"])
    with col2:
        builder_situation = st.selectbox(t["situation"], list(CONVERSATION_BUILDER[audience].keys()))
    with col3:
        level = st.selectbox("Select school level", LEVELS)

    guidance = AUDIENCE_GUIDANCE[audience]
    response = CONVERSATION_BUILDER[audience][builder_situation]

    st.markdown(f"### {t['conversation_guidance']}")
    col1, col2 = st.columns(2)
    with col1:
        card(t["recommended_tone"], guidance["tone"], "soft-blue")
    with col2:
        card(t["main_principle"], guidance["principle"], "mint")

    st.markdown(f"### {t['suggested_response']}")
    phrase_block(t["avoid_saying"], response["avoid"], "avoid")
    phrase_block(t["try_saying"], response["main"][level], "try")
    phrase_block(t["softer_version"], response["softer"][level], "phrase")
    phrase_block(t["follow_up_question"], guidance["follow_up"], "phrase")

    st.markdown(f"### {t['before_speak']}")
    st.warning(t["before_speak_prompt"])

    st.markdown(f"### {t['copy_ready']}")
    st.code(
        f"""Audience: {audience}
Situation: {builder_situation}
School level: {level}

Try saying: {response['main'][level]}

Softer version: {response['softer'][level]}

Follow-up: {guidance['follow_up']}""",
        language="text",
    )

elif page == "Scripts by Situation":
    st.title("Scripts by Situation")
    st.write("Practical language for common classroom communication moments.")

    level = st.selectbox("Select school level", LEVELS)

    st.markdown("### Student is silent")
    phrase_block("Try", PARTICIPATION_SCRIPTS[level], "try")

    st.markdown("### Student avoids group work")
    phrase_block("Try", GROUP_WORK_SCRIPTS[level], "try")

    st.markdown("### Student seems overwhelmed")
    phrase_block("Try", OVERWHELM_SCRIPTS[level], "try")

    st.markdown("### Talking with parents")
    phrase_block(
        "Try",
        "I have noticed some situations where your child may need additional support in class. I would like to understand what helps them feel comfortable and confident.",
        "try",
    )

    st.markdown("### Talking with colleagues")
    phrase_block(
        "Try",
        "I wonder if this student may need a different way to participate. Have you noticed anything similar in your class?",
        "try",
    )

elif page == "Visual Metaphors":
    st.title("Visual Metaphor Toolkit")
    st.write("These metaphors help explain difference without using diagnostic or medical language.")

    col1, col2, col3 = st.columns(3)
    with col1:
        card("Dots", "Different learners may connect ideas, people, and classroom activities in different ways. Useful for explaining diversity without ranking students.", "soft-blue")
    with col2:
        card("Waves", "Energy, attention, confidence, and communication can change from day to day. Useful for explaining fluctuation without blame.", "mint")
    with col3:
        card("Pathways", "Learners may reach understanding through different routes. Useful for explaining that one method does not work for everyone.", "lavender")

    st.markdown("### Design caution")
    st.info("Avoid brain images, diagnostic icons, warning colors, and visuals that suggest normal versus abnormal learners.")

elif page == "Quick Classroom Tools":
    st.title("Quick Classroom Tools")
    st.write("This page will hold printable and downloadable tools. Add your PDFs later in the assets folder.")

    tools = [
        ("Conversation Support Card", "For preparing gentle student conversations."),
        ("Teacher Reflection Card", "For thinking before and after difficult communication moments."),
        ("Student Participation Options Card", "For offering alternatives to speaking, presenting, or group work."),
        ("Parent Conversation Guide", "For discussing classroom observations without labeling."),
        ("Staff Room Quick Reference", "For talking with colleagues about support needs."),
        ("Visual Metaphor Cards", "Dots, Waves, and Pathways for classroom explanation."),
        ("Observation Notes Template", "For recording classroom observations respectfully."),
    ]

    for title, description in tools:
        with st.container():
            st.markdown(f"### {title}")
            st.write(description)
            col1, col2 = st.columns([1, 1])
            with col1:
                st.button(f"View {title}", key=f"view_{title}")
            with col2:
                st.button(f"Download {title}", key=f"download_{title}")
            st.markdown("---")

elif page == "Scenario Practice":
    st.title("Scenario Practice")
    st.write("Practice responding to common classroom communication situations.")

    level = st.selectbox("Select school level", LEVELS)
    scenario_name = st.selectbox("Choose a scenario", list(SCENARIOS.keys()))
    scenario = SCENARIOS[scenario_name]

    st.markdown(f"### Scenario: {scenario_name}")
    phrase_block("Avoid saying", scenario["avoid"], "avoid")
    phrase_block("Try saying", scenario["try"][level], "try")

    st.markdown("### Reflection")
    st.warning(scenario["reflection"])

elif page == "Teacher Reflection":
    st.title("Teacher Reflection")
    st.write("Use these prompts to reflect on communication before, during, or after classroom situations.")

    prompts = [
        "When do I usually notice student difficulty?",
        "Do I notice quiet struggle, or only visible disruption?",
        "Do my classroom expectations allow different forms of participation?",
        "Do I give students ways to ask for help indirectly?",
        "How can I support a learner without exposing them?",
    ]

    for prompt in prompts:
        st.text_area(prompt, key=prompt)

    st.markdown("### Quick self-check")
    st.slider("I feel confident discussing hidden learning differences without labeling.", 1, 5, 3)
    st.slider("I can offer multiple ways for students to participate.", 1, 5, 3)
    st.slider("I know how to discuss concerns with parents respectfully.", 1, 5, 3)
    st.slider("I can recognize when silence may hide difficulty.", 1, 5, 3)

elif page == "Feedback":
    st.title("Feedback")
    st.write("This page can be used for prototype evaluation during your research.")

    with st.form("feedback_form"):
        role = st.selectbox("Your role", ["Teacher", "Student", "Parent", "Researcher", "Other"])
        useful = st.slider("How useful was this toolkit?", 1, 5, 3)
        cultural_fit = st.slider("How appropriate was the language for Japanese school contexts?", 1, 5, 3)
        easy = st.slider("How easy was the toolkit to use?", 1, 5, 3)
        most_helpful = st.text_input("Which page or tool was most helpful?")
        improvement = st.text_area("What should be improved?")
        submitted = st.form_submit_button("Submit feedback")

    if submitted:
        st.success("Thank you. Your feedback has been recorded for prototype reflection.")
        st.caption(f"Submitted: {datetime.now().strftime('%Y-%m-%d %H:%M')}")

elif page == "About the Research":
    st.title("About the Research")

    st.markdown(
        """
        This toolkit was designed as part of a research project on culturally responsive communication for supporting learners who may experience hidden learning or communication differences in Japanese school contexts.

        The design responds to findings from classroom observations, teacher interviews, educator surveys, interactive student design sessions, and visual metaphor activities.

        The central design question is how teachers can notice and communicate about learner needs without creating shame, stigma, or premature labeling.
        """
    )

    st.markdown("### Design principles")
    st.markdown(
        """
        - Support communication, not diagnosis.
        - Protect learner dignity.
        - Use gentle and practical teacher language.
        - Make hidden needs easier to discuss.
        - Offer multiple forms of participation.
        - Use visual metaphors without medical or deficit-based imagery.
        """
    )

    st.info("Research note: This version is a working prototype and should be refined through teacher feedback and classroom-context evaluation.")
