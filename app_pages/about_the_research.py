import streamlit as st
import base64


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


def render_footer():
    st.divider()

    st.markdown("### DOTS Toolkit")
    st.caption(
        "Designing Culturally Responsive Teacher–Student Communication "
        "for Inclusive Classrooms in Japan"
    )
    st.markdown("**Developed by Hope Chawala Banda**")
    st.caption(
        "Developed at the Keio University Graduate School of Media Design (KMD), "
        "PoliPro Laboratory"
    )
    st.caption("Master's Research Project • 2026")
    st.caption("© 2026 Hope Chawala Banda. All Rights Reserved.")


def render_about_the_research(t, LANG):

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

        .research-card {
            background:#FFFFFF;
            border:1px solid #ECECEC;
            border-radius:24px;
            padding:28px;
            margin-bottom:22px;
            box-shadow:0 8px 24px rgba(0,0,0,0.05);
        }

        .research-card-title {
            font-size:1.35rem;
            font-weight:850;
            color:#16324F;
            margin-bottom:0.6rem;
        }

        .research-card-body {
            font-size:1.05rem;
            line-height:1.75;
            color:#555;
        }

        .principle-item {
            background:#FFFFFF;
            border:1px solid #ECECEC;
            border-radius:18px;
            padding:18px 20px;
            margin-bottom:12px;
            box-shadow:0 4px 14px rgba(0,0,0,0.035);
            color:#555;
            line-height:1.6;
        }

        .section-heading {
            font-size:1.55rem;
            font-weight:850;
            color:#16324F;
            margin-top:1.6rem;
            margin-bottom:1rem;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    if LANG == "en":
        st.markdown('<div class="page-eyebrow">Research foundation</div>', unsafe_allow_html=True)
        st.markdown('<div class="page-title">About the Research</div>', unsafe_allow_html=True)
        st.markdown(
            """
            <div class="page-subtitle">
                DOTS was developed from research on culturally responsive teacher–student
                communication in Japanese school contexts.
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown('<div class="page-eyebrow">研究の基盤</div>', unsafe_allow_html=True)
        st.markdown('<div class="page-title">研究について</div>', unsafe_allow_html=True)
        st.markdown(
            """
            <div class="page-subtitle">
                DOTSは、日本の学校における教師と生徒の文化的に配慮した
                コミュニケーションに関する研究をもとに開発されました。
            </div>
            """,
            unsafe_allow_html=True,
        )

    autoplay_video("assets/about_the_research.mp4")

    if LANG == "en":
        cards = [
            (
                "Research focus",
                "This toolkit explores how teachers can notice and communicate about learner needs without creating shame, stigma, or premature labeling.",
            ),
            (
                "Design evidence",
                "The design draws on classroom observations, teacher interviews, educator surveys, participatory design activities, and expert feedback.",
            ),
            (
                "Communication as support",
                "Rather than focusing on diagnosis, the research investigates how communication itself can become a form of inclusive classroom support.",
            ),
        ]

        principles = [
            "Support teacher–student communication rather than diagnosis.",
            "Protect learner dignity during every interaction.",
            "Encourage gentle, practical, and culturally responsive language.",
            "Make hidden learning and communication needs easier to discuss.",
            "Offer multiple pathways for classroom participation.",
            "Use visual metaphors instead of medical or deficit-based imagery.",
        ]

        section_title = "Design Principles"

    else:
        cards = [
            (
                "研究の焦点",
                "このツールキットは、教師が恥ずかしさ、偏見、早すぎるラベルづけを生まずに、学習者のニーズに気づき対話する方法を探ります。",
            ),
            (
                "設計の根拠",
                "設計には、教室観察、教師インタビュー、教育者アンケート、参加型デザイン活動、専門家からのフィードバックが反映されています。",
            ),
            (
                "支援としてのコミュニケーション",
                "本研究は診断を目的とするのではなく、コミュニケーションそのものがインクルーシブな教室支援になり得ることを探ります。",
            ),
        ]

        principles = [
            "診断ではなく教師と生徒の対話を支える。",
            "学習者の尊厳を守る。",
            "やわらかく実践的で文化的に配慮した言葉を使う。",
            "見えにくい学びやコミュニケーションの困難を話しやすくする。",
            "複数の参加方法を認める。",
            "医療的・欠陥ベースの表現ではなく視覚メタファーを用いる。",
        ]

        section_title = "デザイン原則"

    for title, body in cards:
        st.markdown(
            f"""
            <div class="research-card">
                <div class="research-card-title">{title}</div>
                <div class="research-card-body">{body}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown(
        f'<div class="section-heading">{section_title}</div>',
        unsafe_allow_html=True,
    )

    for principle in principles:
        st.markdown(
            f"""
            <div class="principle-item">
                {principle}
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.info(t["important_note"])

    render_footer()
