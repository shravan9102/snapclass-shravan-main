import streamlit as st
import time

from src.database.db import create_attendance


# =========================================================
# NORMAL RENDER FUNCTION
# =========================================================

def render_attendance_result(df, logs):

    st.write("Please review attendance before confirming.")

    st.dataframe(
        df,
        hide_index=True,
        width="stretch"
    )

    col1, col2 = st.columns(2)

    # -----------------------------
    # DISCARD
    # -----------------------------
    with col1:

        if st.button(
            "Discard",
            width="stretch",
            key="discard_attendance"
        ):

            if "attendance_images" in st.session_state:
                st.session_state.attendance_images = []

            if "attendance_results" in st.session_state:
                del st.session_state.attendance_results

            if "voice_attendance_results" in st.session_state:
                del st.session_state.voice_attendance_results

            st.rerun()

    # -----------------------------
    # CONFIRM & SAVE
    # -----------------------------
    with col2:

        if st.button(
            "Confirm & Save",
            width="stretch",
            type="primary",
            key="confirm_save_attendance"
        ):

            try:

                create_attendance(logs)

                st.toast("Attendance taken")

                time.sleep(1)

                if "attendance_images" in st.session_state:
                    st.session_state.attendance_images = []

                if "attendance_results" in st.session_state:
                    del st.session_state.attendance_results

                if "voice_attendance_results" in st.session_state:
                    del st.session_state.voice_attendance_results

                st.rerun()

            except Exception as e:

                st.error(
                    f"Sync failed: {e}"
                )


# =========================================================
# ATTENDANCE REPORT DIALOG
# =========================================================

@st.dialog("Attendance Reports")
def show_attendance_result(df, logs):

    render_attendance_result(df, logs)


# Compatibility alias
attendance_result_dialog = show_attendance_result