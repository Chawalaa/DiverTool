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


def render_visual_metaphors(t, LANG):

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
            max-width:820px;
            margin-bottom:1.5rem;
        }

        .metaphor-title {
            font-size:1.45rem;
            font-weight:850;
            color:#16324F;
            margin-top:0.9rem;
            margin-bottom:0.4rem;
        }

        .metaphor-body {
            font-size:1rem;
            line-height:1.6;
            color:#555;
            min-height:105px;
        }

        .metaphor-tag {
            display:inline-block;
            margin-top:0.7rem;
            margin-bottom:0.8rem;
            padding:0.35rem 0.75rem;
            border-radius:999px;
            font-size:0.82rem;
            font-weight:700;
            background:#DCEEFF;
            color:#16324F;
        }

        div[data-testid="stImage"] img {
            height:200px;
            object-fit:cover;
            border-radius:18px;
            border:1px solid #EEE8DF;
            background:#FFFFFF;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    if LANG == "en":
        st.markdown(
            '<div class="page-eyebrow">Visual language for inclusion</div>',
            unsafe_allow_html=True,
        )
        st.markdown(
            '<div class="page-title">Visual Metaphors</div>',
            unsafe_allow_html=True,
        )
        st.markdown(
            """
            <div class="page-subtitle">
                Explain learner differences gently through dots, waves, and pathways —
                without medical icons, warning colors, or diagnostic labels.
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            '<div class="page-eyebrow">インクルージョンのための視覚言語</div>',
            unsafe_allow_html=True,
        )
        st.markdown(
            '<div class="page-title">視覚メタファー</div>',
            unsafe_allow_html=True,
        )
        st.markdown(
            """
            <div class="page-subtitle">
                Dots、Waves、Pathwaysを使って、診断的な言葉や医療的なイメージに頼らず、
                学習者の違いをやわらかく説明します。
            </div>
            """,
            unsafe_allow_html=True,
        )

    autoplay_video("assets/visual_metaphors.mp4")

    METAPHORS = [
        {
            "title_en": "Dots",
            "title_ja": "Dots",
            "body_en": "Different learners may connect ideas, people, and classroom activities in different ways.",
            "body_ja": "学習者は、考え、人、教室活動をそれぞれ異なる方法でつなげることがあります。",
            "tag_en": "Connection",
            "tag_ja": "つながり",
            "image": "assets/dots.png",
            "example_en": "Use this when explaining that students connect with learning, people, and classroom tasks differently.",
            "example_ja": "学習者が学び、人、教室活動とそれぞれ異なる形でつながることを説明するときに使います。",
        },
        {
            "title_en": "Waves",
            "title_ja": "Waves",
            "body_en": "Energy, attention, confidence, and communication can change from day to day.",
            "body_ja": "エネルギー、注意、安心感、コミュニケーションは日によって変化することがあります。",
            "tag_en": "Fluctuation",
            "tag_ja": "ゆらぎ",
            "image": "assets/waves.png",
            "example_en": "Use this when explaining that participation and confidence may fluctuate across different days or situations.",
            "example_ja": "参加のしやすさや安心感が、日や状況によって変化することを説明するときに使います。",
        },
        {
            "title_en": "Pathways",
            "title_ja": "Pathways",
            "body_en": "Learners may reach understanding through different routes.",
            "body_ja": "学習者は、それぞれ異なる道筋で理解にたどり着くことがあります。",
            "tag_en": "Different Routes",
            "tag_ja": "異なる道筋",
            "image": "assets/pathways.png",
            "example_en": "Use this when explaining that students may need different routes to show understanding.",
            "example_ja": "学習者が理解を示すまでに、それぞれ異なる道筋を必要とすることを説明するときに使います。",
        },
    ]

    st.markdown("<br>", unsafe_allow_html=True)

    cols = st.columns(3)

    for col, item in zip(cols, METAPHORS):
        with col:
            with st.container(border=True):

                title = item["title_ja"] if LANG == "ja" else item["title_en"]
                body = item["body_ja"] if LANG == "ja" else item["body_en"]
                tag = item["tag_ja"] if LANG == "ja" else item["tag_en"]
                example = item["example_ja"] if LANG == "ja" else item["example_en"]

                try:
                    st.image(item["image"], use_container_width=True)
                except Exception:
                    st.info(
                        "Image not found. Please upload it to the assets folder."
                        if LANG == "en"
                        else "画像が見つかりません。assets フォルダにアップロードしてください。"
                    )

                st.markdown(
                    f"""
                    <div class="metaphor-title">{title}</div>
                    <div class="metaphor-body">{body}</div>
                    <span class="metaphor-tag">{tag}</span>
                    """,
                    unsafe_allow_html=True,
                )

                with st.expander("View example" if LANG == "en" else "詳しく見る"):
                    st.write(example)
                    st.write(
                        "Use this metaphor to talk about difference gently, without ranking students or using diagnostic language."
                        if LANG == "en"
                        else "生徒を比較したり、診断的な言葉を使ったりせずに、違いについてやわらかく話すときに使います。"
                    )

    st.divider()

    st.info(
        "Avoid brain images, diagnostic icons, warning colors, and visuals that suggest normal versus abnormal learners."
        if LANG == "en"
        else "脳の画像、診断を連想させるアイコン、警告色、正常／異常を示すような表現は避けます。"
    )
