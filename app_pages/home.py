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


def render_home(t, LANG):

    st.markdown(
        """
        <style>
        .home-eyebrow {
            font-size:0.9rem;
            font-weight:700;
            letter-spacing:0.08em;
            color:#3A78B5;
            text-transform:uppercase;
            margin-bottom:0.5rem;
        }

        .home-main-title {
            font-size:3rem;
            font-weight:900;
            color:#16324F;
            line-height:1.1;
            margin-bottom:0.8rem;
        }

        .home-subtitle {
            font-size:1.25rem;
            line-height:1.7;
            color:#555;
            max-width:780px;
            margin-bottom:1.5rem;
        }

        .hero-box {
            background:#FFFFFF;
            border:1px solid #ECECEC;
            border-radius:24px;
            padding:32px;
            margin-top:8px;
            margin-bottom:28px;
            box-shadow:0 8px 24px rgba(0,0,0,0.06);
        }

        .hero-highlight {
            color:#3A78B5;
            font-weight:800;
        }

        .journey-heading {
            font-size:1.6rem;
            font-weight:850;
            color:#16324F;
            margin-top:1.5rem;
            margin-bottom:1rem;
        }

        .home-card-title {
            font-size:1.3rem;
            font-weight:850;
            color:#16324F;
            margin-top:0.9rem;
            margin-bottom:0.35rem;
        }

        .home-card-body {
            font-size:1rem;
            line-height:1.6;
            color:#555;
            min-height:92px;
        }

        div[data-testid="stImage"] img {
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
        st.markdown('<div class="home-eyebrow">Teacher–Student Communication</div>', unsafe_allow_html=True)
        st.markdown('<div class="home-main-title">Welcome to DOTS</div>', unsafe_allow_html=True)
        st.markdown(
            """
            <div class="home-subtitle">
                A calm, practical toolkit for helping teachers notice learner needs,
                communicate with care, and support participation without relying on diagnostic labels.
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown('<div class="home-eyebrow">教師と生徒のコミュニケーション</div>', unsafe_allow_html=True)
        st.markdown('<div class="home-main-title">DOTSへようこそ</div>', unsafe_allow_html=True)
        st.markdown(
            """
            <div class="home-subtitle">
                教師が学習者のニーズに気づき、思いやりをもって対話し、
                診断ラベルに頼らず参加を支えるための実践的なツールキットです。
            </div>
            """,
            unsafe_allow_html=True,
        )

    try:
        autoplay_video("assets/dots_intro.mp4")
    except Exception:
        st.info("Video not found." if LANG == "en" else "動画が見つかりません。")

    if LANG == "en":
        st.markdown(
            """
            <div class="hero-box">
                DOTS is designed around three simple actions:
                <span class="hero-highlight">notice</span>,
                <span class="hero-highlight">speak with care</span>, and
                <span class="hero-highlight">support participation</span>.
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            """
            <div class="hero-box">
                DOTSは、
                <span class="hero-highlight">気づく</span>、
                <span class="hero-highlight">配慮して話す</span>、
                <span class="hero-highlight">参加を支える</span>
                という三つの行動を中心に設計されています。
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown(
        '<div class="journey-heading">Start with one step</div>'
        if LANG == "en"
        else '<div class="journey-heading">最初の一歩を選ぶ</div>',
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
                    st.image(item["image"], use_container_width=True)
                except Exception:
                    st.info("Image not found." if LANG == "en" else "画像が見つかりません。")

                st.markdown(
                    f"""
                    <div class="home-card-title">{item["title"]}</div>
                    <div class="home-card-body">{item["body"]}</div>
                    """,
                    unsafe_allow_html=True,
                )

                if st.button(
                    "Start here" if LANG == "en" else "ここから始める",
                    key=item["page"],
                    use_container_width=True,
                ):
                    st.session_state.page = item["page"]
                    st.rerun()

    st.divider()

    st.caption(
        "DOTS Toolkit © 2026 · Designed for teacher–student communication"
        if LANG == "en"
        else "DOTSツールキット © 2026 · 教師と生徒のコミュニケーションのために設計"
    )
