import streamlit as st
import base64
from textwrap import dedent


# --------------------------------------------------
# Hero Video
# --------------------------------------------------
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


# --------------------------------------------------
# Hero Box
# --------------------------------------------------
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


# --------------------------------------------------
# Footer
# --------------------------------------------------
def render_footer():

    st.markdown("---")

    st.markdown(
        dedent(
            """
<div style="
text-align:center;
padding:30px 10px;
color:#6B6B6B;
font-size:0.95rem;
line-height:1.9;
">

<strong>DOTS Toolkit</strong><br>

Designing Culturally Responsive Teacher–Student Communication
for Inclusive Classrooms in Japan

<br><br>

Developed by <strong>Hope Chawala Banda</strong><br>

Developed at the Keio University Graduate School of Media Design (KMD), PoliPro Laboratory

<br><br>

Master's Research Project • 2026

<br><br>

© 2026 Hope Chawala Banda. All Rights Reserved.

</div>
"""
        ),
        unsafe_allow_html=True,
    )


# --------------------------------------------------
# Page
# --------------------------------------------------
def render_about_the_research(t, LANG):

    st.title(t["about"])

    autoplay_video("assets/about_the_research.mp4")

    if LANG == "en":
        hero_box("🔬 Research That Informs Practice.")
    else:
        hero_box("🔬 実践につながる研究")

    st.divider()

    if LANG == "en":

        st.markdown(
            """
This toolkit was developed as part of a research project exploring culturally responsive communication between teachers and students in Japanese school contexts.

The design is informed by classroom observations, teacher interviews, educator surveys, participatory design activities, and expert feedback.

Rather than focusing on diagnosis, the research investigates how communication itself can become a form of inclusive support—helping teachers notice learner needs and respond with dignity, empathy, and cultural sensitivity.
"""
        )

        st.markdown("## Design Principles")

        st.markdown(
            """
- Support teacher–student communication rather than diagnosis.
- Protect learner dignity during every interaction.
- Encourage gentle, practical, and culturally responsive language.
- Make hidden learning and communication needs easier to discuss.
- Offer multiple pathways for classroom participation.
- Use visual metaphors instead of medical or deficit-based imagery.
"""
        )

    else:

        st.markdown(
            """
このツールキットは、日本の学校における教師と生徒の文化的に配慮したコミュニケーションに関する研究プロジェクトの一環として開発されました。

設計には、教室観察、教師インタビュー、教育者アンケート、参加型デザイン活動、専門家からのフィードバックによって得られた知見が反映されています。

本研究は診断を目的とするものではなく、教師が学習者のニーズに気づき、尊厳・共感・文化的配慮を大切にした対話を実践できるよう支援することを目的としています。
"""
        )

        st.markdown("## デザイン原則")

        st.markdown(
            """
- 診断ではなく教師と生徒の対話を支える。
- 学習者の尊厳を守る。
- やわらかく実践的で文化的に配慮した言葉を使う。
- 見えにくい学びやコミュニケーションの困難を話しやすくする。
- 複数の参加方法を認める。
- 医療的・欠陥ベースの表現ではなく視覚メタファーを用いる。
"""
        )

    st.info(t["important_note"])

    render_footer()
