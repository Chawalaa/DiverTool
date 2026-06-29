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


def render_visual_metaphors(t, LANG):

    st.title(t["visual_metaphors"])

    # No try/except for now, so Streamlit shows the real error if the video fails.
    autoplay_video("assets/visual_metaphors.mp4")

    st.write(
        "These metaphors help explain difference without using diagnostic or medical language."
        if LANG == "en"
        else "これらのメタファーは、診断的・医療的な言葉を使わずに違いを説明するためのものです。"
    )

    st.markdown(
        """
        <style>
        .metaphor-title {
            font-size: 1.45rem;
            font-weight: 800;
            color: #162B4D;
            margin-top: 0.8rem;
            margin-bottom: 0.4rem;
        }

        .metaphor-body {
            font-size: 0.98rem;
            line-height: 1.55;
            color: #3F3F3F;
            min-height: 95px;
        }

        .metaphor-tag {
            display: inline-block;
            margin-top: 0.5rem;
            margin-bottom: 0.7rem;
            padding: 0.35rem 0.7rem;
            border-radius: 999px;
            font-size: 0.82rem;
            font-weight: 600;
            background: #DCEEFF;
            color: #162B4D;
        }

        div[data-testid="stImage"] img {
            height: 180px;
            object-fit: cover;
            border-radius: 16px;
            border: 1px solid #EEE8DF;
            background: #FFFFFF;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

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

    cols = st.columns(3)

    for col, item in zip(cols, METAPHORS):
        with col:
            with st.container(border=True):

                title = item["title_ja"] if LANG == "ja" else item["title_en"]
                body = item["body_ja"] if LANG == "ja" else item["body_en"]
                tag = item["tag_ja"] if LANG == "ja" else item["tag_en"]
                example = item["example_ja"] if LANG == "ja" else item["example_en"]

                try:
                    st.image(
                        item["image"],
                        use_container_width=True,
                    )
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

                with st.expander("詳しく見る" if LANG == "ja" else "View"):
                    st.write(example)
                    st.write(
                        "Use this metaphor to talk about difference gently, without ranking students or using diagnostic language."
                        if LANG == "en"
                        else "生徒を比較したり、診断的な言葉を使ったりせずに、違いについてやわらかく話すときに使います。"
                    )

    st.info(
        "Avoid brain images, diagnostic icons, warning colors, and visuals that suggest normal versus abnormal learners."
        if LANG == "en"
        else "脳の画像、診断を連想させるアイコン、警告色、正常／異常を示すような表現は避けます。"
    )
