import streamlit as st

def render_teacher_reflection(t, LANG):

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

    for i, prompt in enumerate(prompts):
        st.text_area(
            prompt,
            key=f"reflection_{i}",
            height=120,
            placeholder="" if LANG == "en" else "ここに入力してください…",
        )
