import streamlit as st
import base64
from datetime import datetime


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
                box-shadow:0 6px 20px rgba(0,0,0,.08);
                margin-bottom:20px;
            ">
            <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
        </video>
        """,
        unsafe_allow_html=True,
    )

def hero_box(title):
    st.markdown(
        f"""
        <div style="
            background:white;
            border:1px solid #ECECEC;
            border-radius:22px;
            padding:30px;
            margin-bottom:25px;
            box-shadow:0 8px 24px rgba(0,0,0,.06);
        ">
            <h2 style="
                margin:0;
                color:#16324F;
                font-size:1.7rem;
            ">
                {title}
            </h2>
        </div>
        """,
        unsafe_allow_html=True,
    )

def render_feedback(t, LANG):

    st.title(t["feedback"])

    autoplay_video("assets/feedback.mp4")

    st.divider()

        role_label = "Your role"
        usefulness = "How useful was this toolkit?"
        cultural_fit = "How appropriate was the language for Japanese school contexts?"
        emotional_safety = "How well did the toolkit protect student dignity?"
        improvement = "What should be improved?"
        submit = "Submit feedback"
        success = "Thank you. Your feedback has been recorded for prototype reflection."
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
        st.caption(f"Submitted: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
