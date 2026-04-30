import streamlit as st
from datetime import datetime

# =====================================================
# Culturally Responsive Teacher Communication Toolkit
# Teacher–Student Communication Focus
# =====================================================

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Teacher Communication Toolkit",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -----------------------------
# Language Toggle
# -----------------------------
st.sidebar.markdown("### Language / 言語")

language = st.sidebar.selectbox(
    "Choose language / 言語を選択",
    ["English", "日本語"],
    index=0,
    key="language_toggle",
)

LANG = "ja" if language == "日本語" else "en"
st.sidebar.markdown("---")

# -----------------------------
# Text Dictionary
# -----------------------------
TEXT = {
    "en": {
        "sidebar_title": "Teacher Communication Toolkit",
        "sidebar_caption": "Support for teacher–student communication",
        "menu": "Menu",
        "diagnosis_note": "This toolkit supports communication. It does not diagnose learners.",
        "home": "Home",
        "noticing": "Noticing Learners",
        "conversation_support": "Conversation Support",
        "conversation_builder": "Conversation Builder",
        "scripts": "Scripts by Situation",
        "visual_metaphors": "Visual Metaphors",
        "quick_tools": "Quick Classroom Tools",
        "scenario_practice": "Scenario Practice",
        "reflection": "Teacher Reflection",
        "feedback": "Feedback",
        "about": "About the Research",
        "app_title": "Culturally Responsive Teacher Communication Toolkit",
        "home_subtitle": "For supporting teacher–student conversations with learners who may experience hidden learning or communication differences",
        "home_intro": "This toolkit helps teachers prepare careful, respectful, and low-pressure conversations with students. It is designed especially for school contexts where direct labeling may create discomfort, stigma, or misunderstanding.",
        "notice_title": "Notice without labeling",
        "notice_body": "Recognize possible learning or communication needs without rushing to diagnosis.",
        "speak_title": "Speak with care",
        "speak_body": "Use language that lowers shame, protects dignity, and opens conversation.",
        "support_title": "Support participation",
        "support_body": "Offer multiple ways for students to show understanding and join classroom life.",
        "important_note": "Important: This toolkit is not a diagnostic instrument. It supports communication, reflection, and inclusive classroom practice.",
        "select_level": "Select school level",
        "builder_intro": "Build a careful teacher–student response based on the situation and school level.",
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
        "school_level": "School level",
        "what_teachers_notice": "What teachers may notice",
        "what_not_to_assume": "What not to assume",
        "reflection_prompt": "Reflection prompt",
        "teacher_reflection_intro": "Use these prompts to reflect on communication before, during, or after classroom situations.",
    },
    "ja": {
        "sidebar_title": "教師コミュニケーション・ツールキット",
        "sidebar_caption": "教師と生徒の対話を支えるツール",
        "menu": "メニュー",
        "diagnosis_note": "このツールキットは対話を支援するものであり、学習者を診断するものではありません。",
        "home": "ホーム",
        "noticing": "学習者に気づく",
        "conversation_support": "対話サポート",
        "conversation_builder": "会話ビルダー",
        "scripts": "状況別スクリプト",
        "visual_metaphors": "視覚メタファー",
        "quick_tools": "教室用ツール",
        "scenario_practice": "シナリオ練習",
        "reflection": "教師の振り返り",
        "feedback": "フィードバック",
        "about": "研究について",
        "app_title": "文化的に配慮した教師コミュニケーション・ツールキット",
        "home_subtitle": "見えにくい学びやコミュニケーションの困難を抱える可能性のある学習者との教師・生徒間の対話を支えるために",
        "home_intro": "このツールキットは、教師が生徒と慎重で、尊重のある、低いプレッシャーの対話を準備するためのものです。直接的なラベルづけが不安、偏見、誤解につながりやすい学校現場を想定しています。",
        "notice_title": "ラベルづけせずに気づく",
        "notice_body": "診断を急がず、学びやコミュニケーション上のニーズの可能性に気づく。",
        "speak_title": "配慮して話す",
        "speak_body": "恥ずかしさを和らげ、尊厳を守り、対話を開く言葉を使う。",
        "support_title": "参加を支える",
        "support_body": "生徒が理解を示し、教室に参加するための複数の方法を用意する。",
        "important_note": "重要：このツールキットは診断のためのものではありません。対話、振り返り、インクルーシブな教室実践を支援するものです。",
        "select_level": "学校段階を選択",
        "builder_intro": "状況と学校段階に応じて、教師から生徒への配慮ある声かけを組み立てます。",
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
        "school_level": "学校段階",
        "what_teachers_notice": "教師が気づくかもしれないこと",
        "what_not_to_assume": "決めつけないこと",
        "reflection_prompt": "振り返りの問い",
        "teacher_reflection_intro": "教室での対話の前・最中・後に振り返るための問いです。",
    },
}

t = TEXT[LANG]

# -----------------------------
# Design System
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
# Core Data
# -----------------------------
LEVELS = ["General", "Elementary School", "Junior High School", "High School"]

LEVEL_LABELS = {
    "en": {
        "General": "General",
        "Elementary School": "Elementary School",
        "Junior High School": "Junior High School",
        "High School": "High School",
    },
    "ja": {
        "General": "全般",
        "Elementary School": "小学校",
        "Junior High School": "中学校",
        "High School": "高校",
    },
}

NOTICING_EXAMPLES = {
    "General": {
        "en": [
            "A student appears to understand but avoids certain tasks.",
            "A student gives very short answers or withdraws during interaction.",
            "A student participates differently depending on the task, group, or classroom atmosphere.",
            "A student seems confused but does not ask for clarification.",
        ],
        "ja": [
            "理解しているように見えるが、特定の活動を避ける。",
            "短い答えだけを返したり、やり取りの中で引いてしまう。",
            "活動、グループ、教室の雰囲気によって参加の仕方が変わる。",
            "混乱しているように見えるが、確認や質問をしない。",
        ],
    },
    "Elementary School": {
        "en": [
            "A student moves away from the group or changes activity when unsure.",
            "A student copies classmates rather than asking for help.",
            "A student shows frustration through silence, tears, laughter, or avoidance.",
            "A student struggles when instructions include many steps at once.",
        ],
        "ja": [
            "不安なときにグループから離れたり、別の活動に移ろうとする。",
            "助けを求める代わりに、周りの児童のまねをする。",
            "沈黙、涙、笑い、回避などで困り感を示す。",
            "一度に多くの指示が出ると難しそうにする。",
        ],
    },
    "Junior High School": {
        "en": [
            "A student avoids participation when peers are watching.",
            "A student laughs or makes jokes to hide confusion.",
            "A student seems concerned about being seen as different.",
            "A student becomes quiet in group tasks but performs better individually.",
        ],
        "ja": [
            "周りの生徒に見られていると参加を避ける。",
            "混乱を隠すために笑ったり冗談を言ったりする。",
            "自分が違って見られることを気にしているように見える。",
            "グループ活動では静かになるが、一人では取り組みやすい。",
        ],
    },
    "High School": {
        "en": [
            "A student masks difficulty by appearing calm or independent.",
            "A student avoids optional speaking or presentation tasks.",
            "A student performs well in writing but avoids spontaneous interaction.",
            "A student may not ask for support even when struggling.",
        ],
        "ja": [
            "落ち着いている、または自立しているように見せながら困難を隠す。",
            "発話や発表を伴う任意の活動を避ける。",
            "書くことはできるが、その場でのやり取りを避ける。",
            "困っていても支援を求めないことがある。",
        ],
    },
}

CONVERSATION_BUILDER = {
    "Student is silent during group work": {
        "label": {
            "en": "Student is silent during group work",
            "ja": "グループ活動中に生徒が黙っている",
        },
        "tone": {
            "en": "Private, gentle, and choice-based.",
            "ja": "個別に、やわらかく、選択肢を示す話し方。",
        },
        "principle": {
            "en": "Protect the learner from embarrassment and offer another way to participate.",
            "ja": "生徒が恥ずかしい思いをしないようにし、別の参加方法を示す。",
        },
        "avoid": {
            "en": "Why are you not talking? You need to join the group.",
            "ja": "どうして話さないの？グループに参加しなさい。",
        },
        "try": {
            "General": {
                "en": "I noticed you were quieter today. Would you like to share in another way?",
                "ja": "今日は少し静かだったように見えました。別の方法で伝えてみますか？",
            },
            "Elementary School": {
                "en": "You can show me your idea instead of saying it. That is okay.",
                "ja": "話さなくても、考えを見せてくれて大丈夫だよ。",
            },
            "Junior High School": {
                "en": "You do not have to speak in front of everyone right now. We can find another way for you to share.",
                "ja": "今すぐみんなの前で話さなくても大丈夫です。別の伝え方を一緒に考えましょう。",
            },
            "High School": {
                "en": "If speaking in the group feels uncomfortable, we can think of another way for you to contribute.",
                "ja": "グループで話すことが難しく感じる場合は、別の参加方法を考えることもできます。",
            },
        },
        "soft": {
            "General": {
                "en": "You do not have to speak immediately. You can listen first, write your idea, or share later.",
                "ja": "すぐに話さなくても大丈夫です。まず聞いて、書いて、あとで伝えることもできます。",
            },
            "Elementary School": {
                "en": "You can point, draw, or show me your idea first. Talking can come later.",
                "ja": "まずは指さしたり、描いたり、見せたりしてもいいよ。話すのはあとでも大丈夫。",
            },
            "Junior High School": {
                "en": "You can prepare your idea first. You do not have to speak before you are ready.",
                "ja": "先に考えを準備しても大丈夫です。準備ができる前に話さなくてもいいです。",
            },
            "High School": {
                "en": "You can contribute in another way first, such as writing your idea or choosing a specific role.",
                "ja": "まずは考えを書く、役割を選ぶなど、別の形で参加することもできます。",
            },
        },
        "follow_up": {
            "en": "Would it help if we tried another way for you to participate?",
            "ja": "別の参加方法を試してみると、少しやりやすくなりますか？",
        },
    },
    "Student refuses to present": {
        "label": {
            "en": "Student refuses to present",
            "ja": "生徒が発表を拒む",
        },
        "tone": {
            "en": "Calm, non-punitive, and focused on showing understanding.",
            "ja": "落ち着いて、罰のようにせず、理解を示す方法に焦点を当てる。",
        },
        "principle": {
            "en": "Separate the learning goal from the pressure of public performance.",
            "ja": "学習目標と、人前で発表するプレッシャーを分けて考える。",
        },
        "avoid": {
            "en": "Everyone else is presenting, so you have to do it too.",
            "ja": "みんな発表しているのだから、あなたもしなければなりません。",
        },
        "try": {
            "General": {
                "en": "We can think about another way for you to show your work.",
                "ja": "あなたの取り組みを示す別の方法を一緒に考えましょう。",
            },
            "Elementary School": {
                "en": "You can show me first, then we can decide if you want to show others.",
                "ja": "まず先生に見せてくれて大丈夫だよ。そのあと、みんなに見せるか一緒に考えよう。",
            },
            "Junior High School": {
                "en": "You can share with a partner first, or submit your idea in writing.",
                "ja": "まずペアで共有したり、書いて提出したりする方法もあります。",
            },
            "High School": {
                "en": "You can demonstrate your understanding through a different format if presenting today feels too difficult.",
                "ja": "今日発表することが難しい場合は、別の形式で理解を示すこともできます。",
            },
        },
        "soft": {
            "General": {
                "en": "The goal is not to force you, but to find a way for you to show what you know.",
                "ja": "無理に発表させることが目的ではなく、分かっていることを示す方法を見つけることが目的です。",
            },
            "Elementary School": {
                "en": "Let us start with a smaller and safer step.",
                "ja": "まずは小さくて安心できる方法から始めよう。",
            },
            "Junior High School": {
                "en": "We can reduce the pressure while still helping you share your idea.",
                "ja": "プレッシャーを少なくしながら、考えを伝える方法を考えられます。",
            },
            "High School": {
                "en": "We can keep the learning goal while changing the communication format.",
                "ja": "学習目標はそのままにして、伝え方を変えることができます。",
            },
        },
        "follow_up": {
            "en": "What way of sharing would feel possible today?",
            "ja": "今日できそうな伝え方はどれですか？",
        },
    },
    "Student seems overwhelmed": {
        "label": {
            "en": "Student seems overwhelmed",
            "ja": "生徒が圧倒されているように見える",
        },
        "tone": {
            "en": "Slow, reassuring, and step-by-step.",
            "ja": "ゆっくり、安心感を与えながら、段階的に進める。",
        },
        "principle": {
            "en": "Reduce immediate pressure without lowering expectations.",
            "ja": "期待を下げるのではなく、今かかっているプレッシャーを小さくする。",
        },
        "avoid": {
            "en": "This is easy. You should be able to do it.",
            "ja": "これは簡単です。できるはずです。",
        },
        "try": {
            "General": {
                "en": "Let us pause for a moment. You do not have to finish everything at once.",
                "ja": "少し止まりましょう。全部を一度に終わらせなくても大丈夫です。",
            },
            "Elementary School": {
                "en": "Let us do only the first part together.",
                "ja": "最初の部分だけ一緒にやってみよう。",
            },
            "Junior High School": {
                "en": "You can take a moment. We can break the task into smaller parts.",
                "ja": "少し時間を取って大丈夫です。課題を小さな部分に分けてみましょう。",
            },
            "High School": {
                "en": "Let us identify which part is creating the most pressure and adjust the order.",
                "ja": "どの部分が一番負担になっているか確認して、進める順番を調整しましょう。",
            },
        },
        "soft": {
            "General": {
                "en": "Let us choose one small next step.",
                "ja": "次にできる小さな一歩を選びましょう。",
            },
            "Elementary School": {
                "en": "One step is enough for now.",
                "ja": "今は一つできれば大丈夫だよ。",
            },
            "Junior High School": {
                "en": "You do not have to solve everything at once.",
                "ja": "全部を一度に解決しなくても大丈夫です。",
            },
            "High School": {
                "en": "We can organize the task before trying to complete it.",
                "ja": "終わらせようとする前に、まず課題を整理しましょう。",
            },
        },
        "follow_up": {
            "en": "Which part feels most difficult right now?",
            "ja": "今、一番難しく感じるのはどの部分ですか？",
        },
    },
}

SCENARIO_KEYS = list(CONVERSATION_BUILDER.keys())

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title(t["sidebar_title"])
st.sidebar.caption(t["sidebar_caption"])

PAGE_OPTIONS = [
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
]

PAGE_LABELS = {
    "Home": t["home"],
    "Noticing Learners": t["noticing"],
    "Conversation Support": t["conversation_support"],
    "Conversation Builder": t["conversation_builder"],
    "Scripts by Situation": t["scripts"],
    "Visual Metaphors": t["visual_metaphors"],
    "Quick Classroom Tools": t["quick_tools"],
    "Scenario Practice": t["scenario_practice"],
    "Teacher Reflection": t["reflection"],
    "Feedback": t["feedback"],
    "About the Research": t["about"],
}

page = st.sidebar.radio(
    t["menu"],
    PAGE_OPTIONS,
    format_func=lambda x: PAGE_LABELS[x],
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

    st.info(t["important_note"])

elif page == "Noticing Learners":
    st.title(t["noticing"])

    level = st.selectbox(
        t["select_level"],
        LEVELS,
        format_func=lambda x: LEVEL_LABELS[LANG][x],
    )

    st.markdown(f"### {t['what_teachers_notice']}")
    for item in NOTICING_EXAMPLES[level][LANG]:
        st.markdown(f"- {item}")

    st.markdown(f"### {t['what_not_to_assume']}")
    if LANG == "en":
        phrase_block("Avoid assuming", "The student is lazy, disrespectful, careless, or incapable.", "avoid")
        phrase_block("Consider instead", "The student may be unsure, overwhelmed, embarrassed, masking difficulty, or needing another way to participate.", "try")
        st.warning("What might this learner be experiencing that is not immediately visible?")
    else:
        phrase_block("避けたい決めつけ", "生徒が怠けている、失礼である、不注意である、能力がないと決めつけること。", "avoid")
        phrase_block("代わりに考えたいこと", "生徒は不安、圧倒されている、恥ずかしい、困難を隠している、または別の参加方法を必要としているかもしれません。", "try")
        st.warning("この生徒には、すぐには見えないどのような経験があるかもしれませんか？")

elif page == "Conversation Support":
    st.title(t["conversation_support"])

    level = st.selectbox(
        t["select_level"],
        LEVELS,
        format_func=lambda x: LEVEL_LABELS[LANG][x],
    )

    data = CONVERSATION_BUILDER["Student is silent during group work"]

    phrase_block(t["avoid_saying"], data["avoid"][LANG], "avoid")
    phrase_block(t["try_saying"], data["try"][level][LANG], "try")
    phrase_block(t["softer_version"], data["soft"][level][LANG], "phrase")
    phrase_block(t["follow_up_question"], data["follow_up"][LANG], "phrase")

elif page == "Conversation Builder":
    st.title(t["conversation_builder"])
    st.write(t["builder_intro"])

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

    st.markdown(f"### {t['conversation_guidance']}")
    col1, col2 = st.columns(2)
    with col1:
        card(t["recommended_tone"], response["tone"][LANG], "soft-blue")
    with col2:
        card(t["main_principle"], response["principle"][LANG], "mint")

    st.markdown(f"### {t['suggested_response']}")
    phrase_block(t["avoid_saying"], response["avoid"][LANG], "avoid")
    phrase_block(t["try_saying"], response["try"][level][LANG], "try")
    phrase_block(t["softer_version"], response["soft"][level][LANG], "phrase")
    phrase_block(t["follow_up_question"], response["follow_up"][LANG], "phrase")

    st.markdown(f"### {t['before_speak']}")
    st.warning(t["before_speak_prompt"])

    st.markdown(f"### {t['copy_ready']}")
    st.code(
        f"""{t['situation']}: {response['label'][LANG]}
{t['school_level']}: {LEVEL_LABELS[LANG][level]}

{t['try_saying']}: {response['try'][level][LANG]}

{t['softer_version']}: {response['soft'][level][LANG]}

{t['follow_up_question']}: {response['follow_up'][LANG]}""",
        language="text",
    )

elif page == "Scripts by Situation":
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

elif page == "Visual Metaphors":
    st.title(t["visual_metaphors"])

    if LANG == "en":
        st.write("These metaphors help explain difference without using diagnostic or medical language.")
        col1, col2, col3 = st.columns(3)
        with col1:
            card("Dots", "Different learners may connect ideas, people, and classroom activities in different ways.", "soft-blue")
        with col2:
            card("Waves", "Energy, attention, confidence, and communication can change from day to day.", "mint")
        with col3:
            card("Pathways", "Learners may reach understanding through different routes.", "lavender")
        st.info("Avoid brain images, diagnostic icons, warning colors, and visuals that suggest normal versus abnormal learners.")
    else:
        st.write("これらのメタファーは、診断的・医療的な言葉を使わずに違いを説明するためのものです。")
        col1, col2, col3 = st.columns(3)
        with col1:
            card("Dots", "学習者は、考え、人、教室活動をそれぞれ異なる方法でつなげることがあります。", "soft-blue")
        with col2:
            card("Waves", "エネルギー、注意、安心感、コミュニケーションは日によって変化することがあります。", "mint")
        with col3:
            card("Pathways", "学習者は、それぞれ異なる道筋で理解にたどり着くことがあります。", "lavender")
        st.info("脳の画像、診断を連想させるアイコン、警告色、正常／異常を示すような表現は避けます。")

elif page == "Quick Classroom Tools":
    st.title(t["quick_tools"])

    if LANG == "en":
        st.write("This page will hold printable and downloadable tools. Add your PDFs later in the assets folder.")
        tools = [
            ("Conversation Support Card", "For preparing gentle student conversations."),
            ("Teacher Reflection Card", "For thinking before and after difficult communication moments."),
            ("Student Participation Options Card", "For offering alternatives to speaking, presenting, or group work."),
            ("Visual Metaphor Cards", "Dots, Waves, and Pathways for classroom explanation."),
            ("Observation Notes Template", "For recording classroom observations respectfully."),
        ]
    else:
        st.write("このページには、印刷・ダウンロード可能なツールを配置できます。PDFは後で assets フォルダに追加できます。")
        tools = [
            ("対話サポートカード", "生徒とのやわらかい対話を準備するためのカード。"),
            ("教師の振り返りカード", "難しい対話の前後に考えるためのカード。"),
            ("参加方法カード", "話す、発表する、グループ活動に参加する以外の方法を示すカード。"),
            ("視覚メタファーカード", "Dots、Waves、Pathways を使った教室での説明用カード。"),
            ("観察メモテンプレート", "教室での観察を尊重のある形で記録するためのテンプレート。"),
        ]

    for title, description in tools:
        st.markdown(f"### {title}")
        st.write(description)
        col1, col2 = st.columns(2)
        with col1:
            st.button(f"View / 表示: {title}", key=f"view_{title}")
        with col2:
            st.button(f"Download / ダウンロード: {title}", key=f"download_{title}")
        st.markdown("---")

elif page == "Scenario Practice":
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

elif page == "Teacher Reflection":
    st.title(t["reflection"])
    st.write(t["teacher_reflection_intro"])

    if LANG == "en":
        prompts = [
            "When do I usually notice student difficulty?",
            "Do I notice quiet struggle, or only visible disruption?",
            "Do my classroom expectations allow different forms of participation?",
            "Do I give students ways to ask for help indirectly?",
            "How can I support a learner without exposing them?",
        ]
    else:
        prompts = [
            "私はどのような時に生徒の困り感に気づきやすいですか？",
            "目立つ行動だけでなく、静かな困り感にも気づいていますか？",
            "私の教室では、複数の参加方法が認められていますか？",
            "生徒が間接的に助けを求める方法を用意していますか？",
            "生徒を目立たせずに、どのように支援できますか？",
        ]

    for prompt in prompts:
        st.text_area(prompt, key=prompt)

elif page == "Feedback":
    st.title(t["feedback"])

    if LANG == "en":
        st.write("This page can be used for prototype evaluation during your research.")
        role_label = "Your role"
        usefulness = "How useful was this toolkit?"
        cultural_fit = "How appropriate was the language for Japanese school contexts?"
        emotional_safety = "How well did the toolkit protect student dignity?"
        improvement = "What should be improved?"
        submit = "Submit feedback"
        success = "Thank you. Your feedback has been recorded for prototype reflection."
    else:
        st.write("このページは、研究におけるプロトタイプ評価に使用できます。")
        role_label = "役割"
        usefulness = "このツールキットはどのくらい役に立ちましたか？"
        cultural_fit = "日本の学校現場にとって、言葉づかいはどのくらい適切でしたか？"
        emotional_safety = "このツールキットは、生徒の尊厳をどのくらい守っていましたか？"
        improvement = "改善すべき点は何ですか？"
        submit = "フィードバックを送信"
        success = "ありがとうございます。フィードバックが記録されました。"

    with st.form("feedback_form"):
        st.selectbox(role_label, ["Teacher", "Researcher", "Student", "Other"])
        st.slider(usefulness, 1, 5, 3)
        st.slider(cultural_fit, 1, 5, 3)
        st.slider(emotional_safety, 1, 5, 3)
        st.text_area(improvement)
        submitted = st.form_submit_button(submit)

    if submitted:
        st.success(success)
        st.caption(f"Submitted: {datetime.now().strftime('%Y-%m-%d %H:%M')}")

elif page == "About the Research":
    st.title(t["about"])

    if LANG == "en":
        st.markdown(
            """
            This toolkit was designed as part of a research project on culturally responsive communication
            between teachers and students in Japanese school contexts.

            The design responds to findings from classroom observations, teacher interviews, educator surveys,
            interactive student design sessions, and visual metaphor activities.

            The central design question is how teachers can notice and communicate about learner needs
            without creating shame, stigma, or premature labeling.
            """
        )

        st.markdown("### Design principles")
        st.markdown(
            """
            - Support teacher–student communication, not diagnosis.
            - Protect learner dignity.
            - Use gentle and practical teacher language.
            - Make hidden needs easier to discuss.
            - Offer multiple forms of participation.
            - Use visual metaphors without medical or deficit-based imagery.
            """
        )
    else:
        st.markdown(
            """
            このツールキットは、日本の学校現場における教師と生徒の文化的に配慮したコミュニケーションに関する研究の一部として設計されました。

            設計には、教室観察、教師インタビュー、教育者アンケート、学生とのインタラクティブなデザイン活動、視覚メタファー活動から得られた知見が反映されています。

            中心となる問いは、教師が学習者のニーズに気づき、恥ずかしさ、偏見、早すぎるラベルづけを生まずにどのように対話できるかという点です。
            """
        )

        st.markdown("### デザイン原則")
        st.markdown(
            """
            - 診断ではなく、教師と生徒の対話を支える。
            - 学習者の尊厳を守る。
            - やわらかく実践的な教師の言葉を使う。
            - 見えにくいニーズを話しやすくする。
            - 複数の参加方法を用意する。
            - 医療的・欠陥ベースのイメージではなく、視覚メタファーを使う。
            """
        )

    st.info(t["important_note"])
