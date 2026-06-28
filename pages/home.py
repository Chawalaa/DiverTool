import streamlit as st

def render_home(t, LANG):
    st.title(t["app_title"])
    st.subheader(t["home_subtitle"])

    st.write(
        t.get(
            "home_intro",
            "This toolkit helps teachers prepare careful, respectful, and low-pressure conversations with students."
        )
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
                st.image(item["image"], use_container_width=True)
                st.markdown(f"### {item['title']}")
                st.write(item["body"])

                if st.button(
                    "Explore" if LANG == "en" else "見る",
                    key=f"home_{item['page']}",
                    use_container_width=True,
                ):
                    st.session_state.page = item["page"]
                    st.rerun()

    st.info(t["important_note"])

