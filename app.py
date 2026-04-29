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
    },
    "Parent / Guardian": {
        "tone": "Respectful, observational, and collaborative.",
        "principle": "Begin with what has been noticed in class, not with labels, conclusions, or blame.",
        "follow_up": "Have you noticed anything similar, or are there ways your child feels more comfortable learning at home?",
    },
    "Colleague": {
        "tone": "Reflective, non-accusatory, and evidence-based.",
        "principle": "Discuss patterns and support possibilities without attaching a fixed negative identity to the learner.",
        "follow_up": "Have you noticed when this happens most, and what seems to help?",
    },
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
    },
    "Parent / Guardian": {
        "Student is silent during group work": {
            "avoid": "Your child does not cooperate in group activities.",
            "main": {
                "General": "I have noticed that group activities may sometimes be difficult for your child to join. I would like to understand what kind of participation feels more comfortable for them.",
                "Elementary School": "I have noticed that your child sometimes finds it difficult to join group activities. Are there ways they usually feel comfortable sharing ideas?",
                "Junior High School": "I have noticed that your child may become quiet when group participation is expected. I would like us to think together about supportive ways for them to join.",
                "High School": "I have noticed that your child may prefer quieter or more prepared forms of participation. I would like to discuss what support might help without adding pressure.",
            },
            "softer": {
                "General": "This is not about blaming them. I want to understand what helps them participate safely.",
                "Elementary School": "I want to support them gently, not pressure them.",
                "Junior High School": "I want to be careful not to make them feel singled out.",
                "High School": "I want to respect their dignity while still supporting participation.",
            },
        },
        "Student refuses to present": {
            "avoid": "Your child refuses to do what other students can do.",
            "main": {
                "General": "I have noticed that presentation tasks may feel difficult for your child. I would like to explore ways they can still show their understanding.",
                "Elementary School": "I have noticed that presenting in front of others may feel difficult. Could we think about smaller steps that may help?",
                "Junior High School": "I have noticed that presenting may create pressure, especially in front of peers. I would like to support participation carefully.",
                "High School": "I have noticed that public presentation may not always be the best way for your child to demonstrate understanding. I would like to discuss possible alternatives.",
            },
            "softer": {
                "General": "The goal is not to avoid learning, but to find a way for them to show what they know.",
                "Elementary School": "We can start with a smaller and safer step.",
                "Junior High School": "We can reduce embarrassment while still encouraging growth.",
                "High School": "We can keep expectations high while allowing a different communication format.",
            },
        },
        "Student seems overwhelmed": {
            "avoid": "Your child cannot handle normal classwork.",
            "main": {
                "General": "I have noticed that some tasks may feel overwhelming at times. I would like to understand what helps your child manage learning steps.",
                "Elementary School": "I have noticed that your child sometimes needs tasks broken into smaller steps. What usually helps at home?",
                "Junior High School": "I have noticed that your child may become quiet or withdrawn when a task feels too much. I would like to think about supportive strategies.",
                "High School": "I have noticed some signs of pressure during complex tasks. I would like to discuss how to support organization and confidence.",
            },
            "softer": {
                "General": "This does not mean they cannot learn. It may mean the support structure needs adjustment.",
                "Elementary School": "Small steps may help them feel more confident.",
                "Junior High School": "We can support them without making the difficulty public.",
                "High School": "We can support independence by adjusting how tasks are approached.",
            },
        },
    },
    "Colleague": {
        "Student is silent during group work": {
            "avoid": "That student is always difficult in groups.",
            "main": {
                "General": "I wonder if the student may need a clearer or quieter way to participate in group work.",
                "Elementary School": "Maybe the student needs a concrete role in the group before they can join comfortably.",
                "Junior High School": "I wonder if peer attention is making group participation harder for this student.",
                "High School": "I wonder if the student participates better when there is preparation time or a defined role.",
            },
            "softer": {
                "General": "Maybe we can compare when the student participates more comfortably.",
                "Elementary School": "It might help to observe what happens before the student withdraws.",
                "Junior High School": "It may be useful to think about peer dynamics, not only motivation.",
                "High School": "The pattern may be connected to format, not ability.",
            },
        },
        "Student refuses to present": {
            "avoid": "They are just refusing to try.",
            "main": {
                "General": "I wonder if presentation pressure is hiding what the student actually understands.",
                "Elementary School": "Maybe we can let the student show the work in a smaller step first.",
                "Junior High School": "Peer visibility may be a major part of the difficulty here.",
                "High School": "Maybe the issue is not understanding, but the format of public performance.",
            },
            "softer": {
                "General": "Could we separate the learning goal from the presentation format?",
                "Elementary School": "A small success first may help build confidence.",
                "Junior High School": "A lower-pressure format may still meet the learning goal.",
                "High School": "Alternative demonstration could preserve rigor while reducing unnecessary pressure.",
            },
        },
        "Student seems overwhelmed": {
            "avoid": "This student cannot keep up.",
            "main": {
                "General": "I wonder if the task structure is creating too many demands at once.",
                "Elementary School": "Maybe the student needs the task broken into smaller visible steps.",
                "Junior High School": "The student may need a way to ask for help without feeling exposed.",
                "High School": "The student may benefit from support with sequencing, timing, or task prioritization.",
            },
            "softer": {
                "General": "Maybe adjusting the steps would help us see what they can actually do.",
                "Elementary School": "A visual step-by-step structure may help.",
                "Junior High School": "Private support may work better than public correction.",
                "High School": "Support can be framed as learning strategy, not weakness.",
            },
        },
    },
}

# -----------------------------
# Sidebar Navigation
# -----------------------------

st.sidebar.title("Teacher Communication Toolkit")
st.sidebar.caption("Culturally responsive support for classroom conversations")

page = st.sidebar.radio(
    "Menu",
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
st.sidebar.caption("This toolkit supports communication. It does not diagnose learners.")

# -----------------------------
# Pages
# -----------------------------

if page == "Home":
    st.title("Culturally Responsive Teacher Communication Toolkit")
    st.subheader("For supporting conversations with learners who may experience hidden learning or communication differences")

    st.markdown(
        """
        This toolkit helps teachers prepare careful, respectful, and low-pressure conversations with students, parents, and colleagues.
        It is designed especially for school contexts where direct labeling may create discomfort, stigma, or misunderstanding.
        """
    )

    col1, col2, col3 = st.columns(3)
    with col1:
        card("Notice without labeling", "Recognize possible learning or communication needs without rushing to diagnosis.", "soft-blue")
    with col2:
        card("Speak with care", "Use language that lowers shame, protects dignity, and opens conversation.", "mint")
    with col3:
        card("Support participation", "Offer multiple ways for students to show understanding and join classroom life.", "peach")

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

    st.info("Important: This toolkit is not a diagnostic instrument. It supports communication, reflection, and inclusive classroom practice.")

elif page == "Noticing Learners":
    st.title("Noticing Learners")
    st.write("Use this page to think about what teachers may observe before beginning a supportive conversation.")

    level = st.selectbox("Select school level", LEVELS)

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
    st.title("Conversation Builder")
    st.write("Build a careful conversation response based on who you are speaking with, the situation, and the school level.")

    col1, col2, col3 = st.columns(3)
    with col1:
        audience = st.selectbox("Who are you speaking with?", list(AUDIENCE_GUIDANCE.keys()))
    with col2:
        builder_situation = st.selectbox("What is the situation?", list(CONVERSATION_BUILDER[audience].keys()))
    with col3:
        level = st.selectbox("Select school level", LEVELS)

    guidance = AUDIENCE_GUIDANCE[audience]
    response = CONVERSATION_BUILDER[audience][builder_situation]

    st.markdown("### Conversation guidance")
    col1, col2 = st.columns(2)
    with col1:
        card("Recommended tone", guidance["tone"], "soft-blue")
    with col2:
        card("Main principle", guidance["principle"], "mint")

    st.markdown("### Suggested response")
    phrase_block("Avoid saying", response["avoid"], "avoid")
    phrase_block("Try saying", response["main"][level], "try")
    phrase_block("Softer version", response["softer"][level], "phrase")
    phrase_block("Follow-up question", guidance["follow_up"], "phrase")

    st.markdown("### Before you speak, ask yourself")
    st.warning("Will this conversation protect the learner’s dignity, avoid premature labeling, and make support easier to access?")

    st.markdown("### Copy-ready note")
    st.code(
        f"Audience: {audience}
Situation: {builder_situation}
School level: {level}

Try saying: {response['main'][level]}

Softer version: {response['softer'][level]}

Follow-up: {guidance['follow_up']}",
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
