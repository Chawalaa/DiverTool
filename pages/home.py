import streamlit as st
import base64


# ---------------------------------------------------
# Autoplay Video: Home Page Only
# ---------------------------------------------------
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
            controlslist="nodownload nofullscreen noremoteplayback"
            style="
                width:85%;
                max-height:380px;
                display:block;
                margin:auto;
                object-fit:cover;
                border-radius:20px;
                overflow:hidden;
                box-shadow:0 6px 20px rgba(0,0,0,0.08);
                margin-bottom:20px;
            ">
            <source
                src="data:video/mp4;base64,{video_base64}"
                type="video/mp4">
        </video>
        """,
        unsafe_allow_html=True,
    )


# ---------------------------------------------------
# Home Page
# ---------------------------------------------------
def render_home(t, LANG):

    st.title(t["app_title"])
    st.subheader(t["home_subtitle"])

    try:
        autoplay_video("assets/dots_intro.mp4")
    except Exception:
        st.info(
            "Video not found."
            if LANG == "en"
            else "動画が見つかりません。"
        )

    if LANG == "en":
        st.info(
            "Welcome to the DOTS Toolkit. Explore practical communication strategies that help teachers notice learner needs, communicate with care, and support participation in culturally responsive ways."
        )
    else:
        st.info(
            "DOTSツールキットへようこそ。学習者のニーズに気づき、思いやりをもって対話し、文化的に配慮した形で参加を支えるための実践的なコミュニケーション方法を紹介します。"
        )

    st.write(
        t.get(
            "home_intro",
            "This toolkit helps teachers prepare careful, respectful, and low-pressure conversations with students."
        )
    )

    st.divider()

    st.markdown(
        """
        <style>
        .home-card-title{
            font-size:1.35rem;
            font-weight:800;
            color:#16324F;
            margin-top:0.8rem;
            margin-bottom:0.35rem;
        }

        .home-card-body{
            font-size:1rem;
            line-height:1.6;
            color:#555555;
            min-height:90px;
        }

        div[data-testid="stImage"] img{
            height:210px;
            object-fit:cover;
            border-radius:18px;
            border:1px solid #ECECEC;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    HOME_CARDS = [
        {
            "title": t["notice_title"],
            "body": t["notice_body"],
            "image": "assets/notice_without_labeling.png",
            "page": "Noticing Learners",
        },
        {
            "title": t["speak_title"],
            "body": t["speak_body"],
            "image": "assets/speak_with_care.png",
            "page": "Conversation Support",
        },
        {
            "title": t["support_title"],
            "body": t["support_body"],
            "image": "assets/support_participation.png",
            "page": "Conversation Builder",
        },
    ]

    cols = st.columns(3)

    for col, item in zip(cols, HOME_CARDS):
        with col:
            with st.container(border=True):

                try:
                    st.image(
                        item["image"],
                        use_container_width=True,
                    )
                except Exception:
                    st.info(
                        "Image not found."
                        if LANG == "en"
                        else "画像が見つかりません。"
                    )

                st.markdown(
                    f"""
                    <div class="home-card-title">
                        {item["title"]}
                    </div>

                    <div class="home-card-body">
                        {item["body"]}
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

                if st.button(
                    "Explore" if LANG == "en" else "見る",
                    key=item["page"],
                    use_container_width=True,
                ):
                    st.session_state.page = item["page"]
                    st.rerun()

    st.divider()

    st.success(
        "Designed for teacher–student communication."
        if LANG == "en"
        else "教師と生徒のコミュニケーションのために設計されています。"
    )

    st.caption(
        "DOTS Toolkit © 2026"
        if LANG == "en"
        else "DOTSツールキット © 2026"
    )
