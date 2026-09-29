import streamlit as st

from src.screens.home_screen import home_screen
from src.screens.teacher_screen import teacher_screen
from src.screens.student_screen import student_screen
from src.components.dialog_auto_enroll import auto_enroll_dialog


def main():
    st.set_page_config(
        page_title='SnapClass - Making Attendance Faster using AI',
        page_icon= "https://i.ibb.co/YTYGn5qV/logo.png"
    )

    if "login_type" not in st.session_state:
        st.session_state["login_type"] = None

    if "auto_enroll_dialog_code" not in st.session_state:
        st.session_state["auto_enroll_dialog_code"] = None

    # Get join code from URL
    join_code = st.query_params.get("join-code")

    # Join link -> Student mode
    if join_code and st.session_state["login_type"] != "student":
        st.session_state["login_type"] = "student"
        st.rerun()

    # Show screen
    match st.session_state["login_type"]:

        case "teacher":
            teacher_screen()

        case "student":
            student_screen()

        case None:
            home_screen()

    # Open Quick Enrollment dialog only once
    if (
        join_code
        and st.session_state.get("is_logged_in")
        and st.session_state.get("user_role") == "student"
        and st.session_state.get("auto_enroll_dialog_code") != join_code
    ):
        st.session_state["auto_enroll_dialog_code"] = join_code
        auto_enroll_dialog(join_code)


if __name__ == "__main__":
    main()