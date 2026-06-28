import streamlit as st
import base64


def autoplay_video(video_path):
    with open(video_path, "rb") as video_file:
        video_bytes = video_file.read()

    video_base64 = base64.b64encode(video_bytes).decode()

    st.markdown(
        f"""
        <div style="width:100%;">
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
                    box-shadow:0 6px 20px rgba(0,0,0,0.08);
                    margin-bottom:20px;
                ">
                <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
            </video>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_home(t, LANG):

    st.title(t["app_title"])

    try:
        autoplay_video("assets/dots_intro.mp4")
    except Exception:
        st.info(
            "Video not found."
            if LANG == "en"
            else "動画が見つかりません。"
        )

    st.markdown(
        """
        <style>
        .hero-box{
            background:#FFFFFF;
            border:1px solid #ECECEC;
            border-radius:22px;
            padding:30px;
            margin-top:10px;
            margin-bottom:25px;
            box-shadow:0 8px 24px rgba(0,0,0,0.06);
        }

        .hero-title{
            font-size:1.7rem;
            font-weight:800;
            color:#16324F;
            margin-bottom:12px;
        }

        .hero-body{
            font-size:1.08rem;
            line-height:1.8;
            color:#555555;
        }

        .hero-highlight{
            color:#3A78B5;
            font-weight:700;
        }

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
            min-height:95px;
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

    if LANG == "en":
        st.markdown(
            """
            <div class="hero-box">
                <div class="hero-title">Welcome to the DOTS Toolkit</div>
                <div class="hero-body">
                    DOTS is a communication toolkit designed to help teachers
                    <span class="hero-highlight">notice learner needs</span>,
                    <span class="hero-highlight">communicate with care</span>,
                    and <span class="hero-highlight">support participation</span>
                    without relying on diagnostic labels.

                    <br><br>

            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            """
            <div class="hero-box">
                <div class="hero-title">DOTSツールキットへようこそ</div>
                <div class="hero-body">
                    DOTSは、教師が
                    <span class="hero-highlight">学習者のニーズに気づき</span>、
                    <span class="hero-highlight">思いやりをもって対話し</span>、
                    <span class="hero-highlight">参加を支える</span>
                    ためのコミュニケーションツールキットです。

                    <br><br>

                    日本の学校で行われた研究をもとに設計されており、
                    教師と生徒の文化的に配慮した対話を支えるための
                    実践的な言葉づかい、視覚メタファー、
                    教室ツール、コミュニケーションガイドを提供します。
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.divider()

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
                    st.image(item["image"], use_container_width=True)
                except Exception:
                    st.info(
                        "Image not found."
                        if LANG == "en"
                        else "画像が見つかりません。"
                    )

                st.markdown(
                    f"""
                    <div class="home-card-title">{item["title"]}</div>
                    <div class="home-card-body">{item["body"]}</div>
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
