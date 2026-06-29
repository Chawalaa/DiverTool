import streamlit as st
from datetime import datetime

def render_feedback(t, LANG):

    st.title(t["feedback"])

    if LANG == "en":
        st.write(
            "This page can be used for prototype evaluation during your research."
        )

        role_label = "Your role"
        usefulness = "How useful was this toolkit?"
        cultural_fit = "How appropriate was the language for Japanese school contexts?"
        emotional_safety = "How well did the toolkit protect student dignity?"
        improvement = "What should be improved?"
        submit = "Submit feedback"
        success = (
            "Thank you. Your feedback has been recorded for prototype reflection."
        )

        roles = ["Teacher", "Researcher", "Student", "Other"]

    else:

        st.write(
            "このページは、研究におけるプロトタイプ評価に使用できます。"
        )

        role_label = "役割"
        usefulness = "このツールキットはどのくらい役に立ちましたか？"
        cultural_fit = "日本の学校現場にとって、言葉づかいはどのくらい適切でしたか？"
        emotional_safety = "このツールキットは、生徒の尊厳をどのくらい守っていましたか？"
        improvement = "改善すべき点は何ですか？"
        submit = "フィードバックを送信"
        success = "ありがとうございます。フィードバックが記録されました。"

        roles = ["教師", "研究者", "学生", "その他"]

    with st.form("feedback_form"):

        st.selectbox(role_label, roles)

        st.slider(usefulness, 1, 5, 3)

        st.slider(cultural_fit, 1, 5, 3)

        st.slider(emotional_safety, 1, 5, 3)

        st.text_area(improvement)

        submitted = st.form_submit_button(submit)

    if submitted:

        st.success(success)

        st.caption(
            f"Submitted: {datetime.now().strftime('%Y-%m-%d %H:%M')}"
        )
