import streamlit as st

def render_about_the_research(t, LANG):

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
