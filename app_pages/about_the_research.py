import streamlit as st

def render_about_the_research(t, LANG):

    st.title(t["about"])

    if LANG == "en":
        st.markdown(
            """
            This toolkit was designed as part of a research project on culturally responsive communication
            between teachers and students in Japanese school contexts.
            The design responds to findings from classroom observations, teacher interviews, educator surveys, and expert feedback.
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
            このツールキットは、日本の学校における教師と生徒間の「文化に対応したコミュニケーション」に関する研究プロジェクトの一環として作成されました。

            この設計は、教室での観察、教師へのインタビュー、教育者への調査、および専門家からのフィードバックで得られた知見に基づいています。

            設計上の中心的な課題は、学習者のニーズに気づき、それについて対話を行う際に、いかにして恥やスティグマ、あるいは拙速なレッテル貼りを生じさせずにそれを行うか、という点にあります。
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
