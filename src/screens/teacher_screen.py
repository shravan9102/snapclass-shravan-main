# import streamlit as st
# import time
# from datetime import datetime

# import numpy as np
# import pandas as pd

# from PIL import Image, ImageOps

# # =========================================================
# # UI
# # =========================================================

# from src.ui.base_layout import (
#     style_background_dashboard,
#     style_base_layout
# )

# from src.components.header import header_dashboard
# from src.components.footer import footer_dashboard
# from src.components.subject_card import subject_card

# # =========================================================
# # DATABASE
# # =========================================================

# from src.database.db import (
#     check_teacher_exists,
#     create_teacher,
#     teacher_login,
#     get_teacher_subjects,
#     get_attendance_for_teacher
# )

# from src.database.config import supabase

# # =========================================================
# # DIALOGS
# # =========================================================

# from src.components.dialog_create_subject import (
#     create_subject_dialog
# )

# from src.components.dialog_share_subject import (
#     share_subject_dialog
# )

# from src.components.dialog_add_photo import (
#     add_photos_dialog
# )

# from src.components.dialog_voice_attendance import (
#     voice_attendance_dialog
# )

# from src.components.dialog_attendance_results import (
#     show_attendance_result
# )

# # =========================================================
# # FACE PIPELINE
# # =========================================================

# from src.pipelines.face_pipeline import (
#     predict_attendance
# )

# # =========================================================
# # FOOTER
# # =========================================================

# from src.components import footer


# # =========================================================
# # COMMON UI STYLE
# # =========================================================

# def teacher_ui_style():

#     st.markdown(
#         """
#         <style>

#         .stApp {
#             background-color: #FFF5FA !important;
#         }

#         .main {
#             background-color: #FFF5FA !important;
#         }

#         [data-testid="stAppViewContainer"] {
#             background-color: #FFF5FA !important;
#         }

#         [data-testid="stMain"] {
#             background-color: #FFF5FA !important;
#         }

#         /* =====================================
#            HEADINGS
#            ===================================== */

#         h1,
#         h2,
#         h3 {
#             color: #111111 !important;
#             font-weight: 900 !important;
#         }

#         /* =====================================
#            INPUT LABELS
#            ===================================== */

#         label {
#             color: #111111 !important;
#             font-weight: 600 !important;
#         }

#         /* =====================================
#            INPUT BOX
#            ===================================== */

#         div[data-baseweb="input"] {
#             background-color: #FFF9FC !important;
#             border-radius: 12px !important;
#         }

#         div[data-baseweb="input"] > div {
#             background-color: #FFF9FC !important;
#             border-radius: 12px !important;
#         }

#         /* =====================================
#            INPUT TEXT
#            ===================================== */

#         input {
#             color: #111111 !important;
#         }

#         input::placeholder {
#             color: #999999 !important;
#         }

#         /* =====================================
#            ALL BUTTONS
#            ===================================== */

#         div.stButton > button {
#             border-radius: 25px !important;
#             min-height: 42px !important;
#             font-weight: 600 !important;
#             border: none !important;
#         }

#         /* =====================================
#            PINK BUTTON
#            ===================================== */

#         button[kind="secondary"] {
#             background-color: #D85B91 !important;
#             color: white !important;
#             border: none !important;
#         }

#         button[kind="secondary"]:hover {
#             background-color: #C94D84 !important;
#             color: white !important;
#         }

#         /* =====================================
#            NORMAL BUTTON
#            ===================================== */

#         div.stButton > button:not([kind="primary"]):not([kind="secondary"]) {
#             background-color: #D85B91 !important;
#             color: white !important;
#             border: none !important;
#         }

#         div.stButton > button:not([kind="primary"]):not([kind="secondary"]):hover {
#             background-color: #C94D84 !important;
#             color: white !important;
#         }

#         /* =====================================
#            BLUE BUTTON
#            ===================================== */

#         button[kind="primary"] {
#             background-color: #168BD1 !important;
#             color: white !important;
#             border: none !important;
#         }

#         button[kind="primary"]:hover {
#             background-color: #087DBF !important;
#             color: white !important;
#         }

#         /* =====================================
#            DIVIDER
#            ===================================== */

#         hr {
#             border-color: #F0DDE7 !important;
#         }

#         /* =====================================
#            FOOTER
#            ===================================== */

#         .shravan-footer {
#             text-align: center;
#             color: #111111 !important;
#             font-size: 14px;
#             font-weight: 700;
#             margin-top: 25px;
#             padding-bottom: 10px;
#         }

#         </style>
#         """,
#         unsafe_allow_html=True
#     )


# # =========================================================
# # TEACHER SCREEN
# # =========================================================

# def teacher_screen():

#     style_background_dashboard()
#     style_base_layout()
#     teacher_ui_style()

#     # =====================================================
#     # LOGGED IN
#     # =====================================================

#     if "teacher_data" in st.session_state:

#         teacher_dashboard()

#     # =====================================================
#     # LOGIN
#     # =====================================================

#     elif (
#         "teacher_login_type" not in st.session_state
#         or st.session_state.teacher_login_type == "login"
#     ):

#         teacher_screen_login()

#     # =====================================================
#     # REGISTER
#     # =====================================================

#     elif st.session_state.teacher_login_type == "register":

#         teacher_screen_register()

#     else:

#         st.session_state.teacher_login_type = "login"

#         teacher_screen_login()


# # =========================================================
# # TEACHER DASHBOARD
# # =========================================================

# def teacher_dashboard():

#     teacher_data = st.session_state.teacher_data

#     c1, c2 = st.columns(
#         2,
#         vertical_alignment="center",
#         gap="xlarge"
#     )

#     # =====================================================
#     # HEADER
#     # =====================================================

#     with c1:

#         header_dashboard()

#     # =====================================================
#     # WELCOME + LOGOUT
#     # =====================================================

#     with c2:

#         st.subheader(
#             f"Welcome, {teacher_data['name']}"
#         )

#         if st.button(
#             "Logout",
#             type="secondary",
#             key="loginbackbtn"
#         ):

#             st.session_state["is_logged_in"] = False

#             if "teacher_data" in st.session_state:

#                 del st.session_state.teacher_data

#             keys_to_clear = [
#                 "attendance_images",
#                 "last_camera_photo",
#                 "uploaded_photo_ids",
#                 "selected_subject_id",
#                 "attendance_results",
#                 "attendance_to_log",
#                 "run_face_analysis",
#                 "run_voice_attendance",
#                 "voice_attendance_results"
#             ]

#             for key in keys_to_clear:

#                 if key in st.session_state:

#                     del st.session_state[key]

#             st.rerun()

#     st.write("")

#     # =====================================================
#     # DEFAULT TAB
#     # =====================================================

#     if "current_teacher_tab" not in st.session_state:

#         st.session_state.current_teacher_tab = (
#             "take_attendance"
#         )

#     # =====================================================
#     # TOP TABS
#     # =====================================================

#     tab1, tab2, tab3 = st.columns(3)

#     # =====================================================
#     # TAKE ATTENDANCE
#     # =====================================================

#     with tab1:

#         type1 = (
#             "primary"
#             if st.session_state.current_teacher_tab
#             == "take_attendance"
#             else "secondary"
#         )

#         if st.button(
#             "Take Attendance",
#             type=type1,
#             width="stretch",
#             icon=":material/ar_on_you:",
#             key="teacher_tab_take"
#         ):

#             st.session_state.current_teacher_tab = (
#                 "take_attendance"
#             )

#             st.rerun()

#     # =====================================================
#     # MANAGE SUBJECTS
#     # =====================================================

#     with tab2:

#         type2 = (
#             "primary"
#             if st.session_state.current_teacher_tab
#             == "manage_subjects"
#             else "secondary"
#         )

#         if st.button(
#             "Manage Subjects",
#             type=type2,
#             width="stretch",
#             icon=":material/book_ribbon:",
#             key="teacher_tab_manage"
#         ):

#             st.session_state.current_teacher_tab = (
#                 "manage_subjects"
#             )

#             st.rerun()

#     # =====================================================
#     # ATTENDANCE RECORDS
#     # =====================================================

#     with tab3:

#         type3 = (
#             "primary"
#             if st.session_state.current_teacher_tab
#             == "attendance_records"
#             else "secondary"
#         )

#         if st.button(
#             "Attendance Records",
#             type=type3,
#             width="stretch",
#             icon=":material/cards_stack:",
#             key="teacher_tab_records"
#         ):

#             st.session_state.current_teacher_tab = (
#                 "attendance_records"
#             )

#             st.rerun()

#     st.divider()

#     # =====================================================
#     # TAB CONTENT
#     # =====================================================

#     if (
#         st.session_state.current_teacher_tab
#         == "take_attendance"
#     ):

#         teacher_tab_take_attendance()

#     elif (
#         st.session_state.current_teacher_tab
#         == "manage_subjects"
#     ):

#         teacher_tab_manage_subjects()

#     elif (
#         st.session_state.current_teacher_tab
#         == "attendance_records"
#     ):

#         teacher_tab_attendance_records()

#     footer.footer_dashboard()


# # =========================================================
# # TAKE ATTENDANCE
# # =========================================================

# def teacher_tab_take_attendance():

#     teacher_id = st.session_state.teacher_data[
#         "teacher_id"
#     ]

#     # =====================================================
#     # PHOTO STORAGE
#     # =====================================================

#     if "attendance_images" not in st.session_state:

#         st.session_state.attendance_images = []

#     if "last_camera_photo" not in st.session_state:

#         st.session_state.last_camera_photo = None

#     if "uploaded_photo_ids" not in st.session_state:

#         st.session_state.uploaded_photo_ids = []

#     # =====================================================
#     # HEADER
#     # =====================================================

#     st.header(
#         "Take AI Attendance"
#     )

#     # =====================================================
#     # GET SUBJECTS
#     # =====================================================

#     try:

#         subjects = get_teacher_subjects(
#             teacher_id
#         )

#     except Exception as e:

#         st.error(
#             f"Unable to load subjects: {e}"
#         )

#         return

#     if not subjects:

#         st.warning(
#             "You haven't created any subjects yet! "
#             "Please create one to begin!"
#         )

#         return

#     # =====================================================
#     # SUBJECT OPTIONS
#     # =====================================================

#     subject_options = {
#         f"{s['name']} - {s['subject_code']}":
#         s["subject_id"]
#         for s in subjects
#     }

#     # =====================================================
#     # SUBJECT + ADD PHOTOS
#     # =====================================================

#     col1, col2 = st.columns(
#         [3, 1],
#         vertical_alignment="bottom"
#     )

#     # =====================================================
#     # SELECT SUBJECT
#     # =====================================================

#     with col1:

#         selected_subject_label = st.selectbox(
#             "Select Subject",
#             options=list(
#                 subject_options.keys()
#             ),
#             key="attendance_subject"
#         )

#     # =====================================================
#     # ADD PHOTOS
#     # =====================================================

#     with col2:

#         if st.button(
#             "Add Photos",
#             type="primary",
#             icon=":material/photo_prints:",
#             width="stretch",
#             key="add_attendance_photos"
#         ):

#             add_photos_dialog()

#     # =====================================================
#     # SELECTED SUBJECT
#     # =====================================================

#     selected_subject_id = subject_options[
#         selected_subject_label
#     ]

#     st.session_state[
#         "selected_subject_id"
#     ] = selected_subject_id

#     st.divider()

#     # =====================================================
#     # ADDED PHOTOS
#     # =====================================================

#     if st.session_state.attendance_images:

#         st.subheader(
#             "Added Photos"
#         )

#         PHOTO_WIDTH = 180
#         PHOTO_HEIGHT = 140

#         photo_cols = st.columns(4)

#         for index, image in enumerate(
#             st.session_state.attendance_images
#         ):

#             with photo_cols[index % 4]:

#                 try:

#                     if not isinstance(
#                         image,
#                         Image.Image
#                     ):

#                         image = Image.fromarray(
#                             np.array(image)
#                         )

#                     preview_image = ImageOps.fit(
#                         image.convert("RGB"),
#                         (
#                             PHOTO_WIDTH,
#                             PHOTO_HEIGHT
#                         ),
#                         method=Image.Resampling.LANCZOS,
#                         centering=(0.5, 0.5)
#                     )

#                     st.image(
#                         preview_image,
#                         width=PHOTO_WIDTH
#                     )

#                     st.caption(
#                         f"Photo {index + 1}"
#                     )

#                 except Exception as e:

#                     st.error(
#                         f"Unable to display Photo "
#                         f"{index + 1}: {e}"
#                     )

#     else:

#         st.info(
#             "No photos added yet. "
#             "Click 'Add Photos' to capture or upload "
#             "classroom photos."
#         )

#     # =====================================================
#     # ACTION BUTTONS
#     #
#     # IMPORTANT:
#     # These buttons are intentionally OUTSIDE the
#     # attendance_images condition.
#     #
#     # Therefore they are ALWAYS visible.
#     # =====================================================

#     st.divider()

#     action1, action2, action3 = st.columns(3)

#     # =====================================================
#     # CLEAR ALL PHOTOS
#     # =====================================================

#     with action1:

#         if st.button(
#             "Clear all photos",
#             type="secondary",
#             icon=":material/delete:",
#             width="stretch",
#             key="clear_all_attendance_photos"
#         ):

#             if not st.session_state.attendance_images:

#                 st.info("There are no photos to clear.")

#             else:

#                 st.session_state.attendance_images = []

#                 st.session_state.last_camera_photo = None

#                 st.session_state.uploaded_photo_ids = []

#                 if "attendance_results" in st.session_state:

#                     del st.session_state[
#                         "attendance_results"
#                     ]

#                 if "attendance_to_log" in st.session_state:

#                     del st.session_state[
#                         "attendance_to_log"
#                     ]

#                 st.rerun()

#     # =====================================================
#     # RUN FACE ANALYSIS
#     # =====================================================

#     with action2:

#         if st.button(
#             "Run Face Analysis",
#             type="primary",
#             icon=":material/face:",
#             width="stretch",
#             key="run_face_analysis"
#         ):

#             run_face_analysis(
#                 selected_subject_id
#             )

#     # =====================================================
#     # VOICE ATTENDANCE
#     # =====================================================

#     with action3:

#         if st.button(
#             "Use Voice Attendance",
#             type="primary",
#             icon=":material/mic:",
#             width="stretch",
#             key="use_voice_attendance"
#         ):

#             # Directly open Voice Attendance dialog
#             voice_attendance_dialog(
#                 selected_subject_id
#             )


# # =========================================================
# # RUN FACE ANALYSIS
# # =========================================================

# def run_face_analysis(
#     selected_subject_id
# ):

#     images = st.session_state.get(
#         "attendance_images",
#         []
#     )

#     if not images:

#         st.warning(
#             "Please add photos first."
#         )

#         return

#     # =====================================================
#     # DETECTED STUDENTS
#     # =====================================================

#     all_detected_ids = {}

#     # =====================================================
#     # PROCESS PHOTOS
#     # =====================================================

#     with st.spinner(
#         "Deep scanning classroom photos..."
#     ):

#         for index, image in enumerate(images):

#             try:

#                 # -----------------------------------------
#                 # Convert image to NumPy
#                 # -----------------------------------------

#                 if isinstance(
#                     image,
#                     Image.Image
#                 ):

#                     img_np = np.array(
#                         image.convert("RGB")
#                     )

#                 else:

#                     img_np = np.array(
#                         image
#                     )

#                     if (
#                         len(img_np.shape) == 3
#                         and img_np.shape[2] == 4
#                     ):

#                         img_np = img_np[:, :, :3]

#                 # -----------------------------------------
#                 # FACE PREDICTION
#                 # -----------------------------------------

#                 result = predict_attendance(
#                     img_np
#                 )

#                 # -----------------------------------------
#                 # EXPECTED:
#                 # detected, ..., ...
#                 # -----------------------------------------

#                 if isinstance(
#                     result,
#                     tuple
#                 ):

#                     detected = result[0]

#                 else:

#                     detected = result

#                 if not detected:

#                     continue

#                 # -----------------------------------------
#                 # DETECTED DICT
#                 # -----------------------------------------

#                 if isinstance(
#                     detected,
#                     dict
#                 ):

#                     detected_ids = detected.keys()

#                 # -----------------------------------------
#                 # DETECTED LIST
#                 # -----------------------------------------

#                 elif isinstance(
#                     detected,
#                     list
#                 ):

#                     detected_ids = detected

#                 # -----------------------------------------
#                 # DETECTED SET
#                 # -----------------------------------------

#                 elif isinstance(
#                     detected,
#                     set
#                 ):

#                     detected_ids = detected

#                 else:

#                     continue

#                 # -----------------------------------------
#                 # SAVE DETECTED IDS
#                 # -----------------------------------------

#                 for student_id in detected_ids:

#                     try:

#                         student_id = int(
#                             student_id
#                         )

#                     except (
#                         ValueError,
#                         TypeError
#                     ):

#                         continue

#                     if student_id not in all_detected_ids:

#                         all_detected_ids[
#                             student_id
#                         ] = []

#                     all_detected_ids[
#                         student_id
#                     ].append(
#                         f"Photo {index + 1}"
#                     )

#             except Exception as e:

#                 st.warning(
#                     f"Photo {index + 1} could not be "
#                     f"analyzed: {e}"
#                 )

#     # =====================================================
#     # GET ENROLLED STUDENTS
#     # =====================================================

#     try:

#         enrolled_res = (
#             supabase
#             .table("subject_students")
#             .select(
#                 "*, students(*)"
#             )
#             .eq(
#                 "subject_id",
#                 selected_subject_id
#             )
#             .execute()
#         )

#         enrolled_students = (
#             enrolled_res.data
#             if enrolled_res.data
#             else []
#         )

#     except Exception as e:

#         st.error(
#             f"Unable to load enrolled students: {e}"
#         )

#         return

#     # =====================================================
#     # NO STUDENTS
#     # =====================================================

#     if not enrolled_students:

#         st.warning(
#             "No students enrolled in this course."
#         )

#         return

#     # =====================================================
#     # CREATE ATTENDANCE RESULT
#     # =====================================================

#     results = []

#     attendance_to_log = []

#     current_timestamp = (
#         datetime.now().strftime(
#             "%Y-%m-%dT%H:%M:%S"
#         )
#     )

#     # =====================================================
#     # CHECK EVERY STUDENT
#     # =====================================================

#     for node in enrolled_students:

#         student = node.get(
#             "students"
#         )

#         # Supabase relation can be list
#         if isinstance(
#             student,
#             list
#         ):

#             if student:

#                 student = student[0]

#             else:

#                 continue

#         if not isinstance(
#             student,
#             dict
#         ):

#             continue

#         student_id = student.get(
#             "student_id"
#         )

#         student_name = student.get(
#             "name",
#             "Unknown"
#         )

#         if student_id is None:

#             continue

#         try:

#             student_id_int = int(
#                 student_id
#             )

#         except (
#             ValueError,
#             TypeError
#         ):

#             student_id_int = student_id

#         sources = all_detected_ids.get(
#             student_id_int,
#             []
#         )

#         is_present = (
#             len(sources) > 0
#         )

#         # =================================================
#         # RESULT
#         # =================================================

#         results.append(
#             {
#                 "Name": student_name,

#                 "ID": student_id,

#                 "Source": (
#                     ", ".join(sources)
#                     if is_present
#                     else "-"
#                 ),

#                 "Status": (
#                     "Present"
#                     if is_present
#                     else "Absent"
#                 )
#             }
#         )

#         # =================================================
#         # ATTENDANCE LOG
#         # =================================================

#         attendance_to_log.append(
#             {
#                 "student_id": student_id,

#                 "subject_id": selected_subject_id,

#                 "timestamp": current_timestamp,

#                 "is_present": bool(
#                     is_present
#                 )
#             }
#         )

#     # =====================================================
#     # STORE RESULTS
#     # =====================================================

#     st.session_state[
#         "attendance_results"
#     ] = results

#     st.session_state[
#         "attendance_to_log"
#     ] = attendance_to_log

#     # =====================================================
#     # OPEN ATTENDANCE REPORT DIALOG
#     # =====================================================

#     result_df = pd.DataFrame(
#         results
#     )

#     show_attendance_result(
#         result_df,
#         attendance_to_log
#     )


# # =========================================================
# # MANAGE SUBJECTS
# # =========================================================

# def teacher_tab_manage_subjects():

#     teacher_id = st.session_state.teacher_data[
#         "teacher_id"
#     ]

#     col1, col2 = st.columns(2)

#     # =====================================================
#     # HEADER
#     # =====================================================

#     with col1:

#         st.header(
#             "Manage Subjects",
#             width="stretch"
#         )

#     # =====================================================
#     # CREATE SUBJECT
#     # =====================================================

#     with col2:

#         if st.button(
#             "Create New Subject",
#             width="stretch",
#             key="create_new_subject"
#         ):

#             create_subject_dialog(
#                 teacher_id
#             )

#     # =====================================================
#     # GET SUBJECTS
#     # =====================================================

#     try:

#         subjects = get_teacher_subjects(
#             teacher_id
#         )

#     except Exception as e:

#         st.error(
#             f"Unable to load subjects: {e}"
#         )

#         return

#     if subjects:

#         for sub in subjects:

#             stats = [
#                 (
#                     "👥",
#                     "Students",
#                     sub.get(
#                         "total_students",
#                         0
#                     )
#                 ),
#                 (
#                     "📚",
#                     "Classes",
#                     sub.get(
#                         "total_classes",
#                         0
#                     )
#                 ),
#             ]

#             def share_btn(
#                 sub=sub
#             ):

#                 if st.button(
#                     f"Share Code: {sub['name']}",
#                     key=f"share_{sub['subject_code']}"
#                 ):

#                     share_subject_dialog(
#                         sub["name"],
#                         sub["subject_code"]
#                     )

#             st.write("")

#             subject_card(
#                 name=sub["name"],
#                 code=sub["subject_code"],
#                 section=sub["section"],
#                 stats=stats,
#                 footer_callback=share_btn
#             )

#     else:

#         st.info(
#             "NO SUBJECTS FOUND. CREATE ONE ABOVE"
#         )


# # =========================================================
# # ATTENDANCE RECORDS
# # =========================================================

# def teacher_tab_attendance_records():

#     st.header(
#         "Attendance Records"
#     )

#     teacher_data = st.session_state.get(
#         "teacher_data"
#     )

#     if not teacher_data:

#         st.warning(
#             "Teacher session not found."
#         )

#         return

#     teacher_id = teacher_data.get(
#         "teacher_id"
#     )

#     if teacher_id is None:

#         return

#     # =====================================================
#     # GET SUBJECTS
#     # =====================================================

#     try:

#         subjects = get_teacher_subjects(
#             teacher_id
#         )

#     except Exception as e:

#         st.error(
#             f"Unable to load subjects: {e}"
#         )

#         return

#     if not subjects:

#         st.info(
#             "No subjects found."
#         )

#         return

#     subject_options = {
#         f"{s['name']} - {s['subject_code']}":
#         s["subject_id"]
#         for s in subjects
#     }

#     selected_subject_label = st.selectbox(
#         "Select Subject",
#         options=list(
#             subject_options.keys()
#         ),
#         key="records_subject"
#     )

#     selected_subject_id = subject_options[
#         selected_subject_label
#     ]

#     st.divider()

#     # =====================================================
#     # GET ATTENDANCE
#     # =====================================================

#     try:

#         response = (
#             supabase
#             .table("attendance_logs")
#             .select(
#                 "*"
#             )
#             .eq(
#                 "subject_id",
#                 selected_subject_id
#             )
#             .order(
#                 "timestamp",
#                 desc=True
#             )
#             .execute()
#         )

#         records = (
#             response.data
#             if response.data
#             else []
#         )

#     except Exception as e:

#         st.error(
#             f"Unable to load attendance records: {e}"
#         )

#         return

#     if not records:

#         st.info(
#             "No attendance records found."
#         )

#         return

#     # =====================================================
#     # DISPLAY
#     # =====================================================

#     records_df = pd.DataFrame(
#         records
#     )

#     st.dataframe(
#         records_df,
#         width="stretch",
#         hide_index=True
#     )


# # =========================================================
# # LOGIN TEACHER
# # =========================================================

# def login_teacher(
#     username,
#     password
# ):

#     if not username or not password:

#         return False

#     try:

#         teacher = teacher_login(
#             username,
#             password
#         )

#     except Exception as e:

#         st.error(
#             f"Login error: {e}"
#         )

#         return False

#     if teacher:

#         st.session_state.user_role = "teacher"

#         st.session_state.teacher_data = teacher

#         st.session_state.is_logged_in = True

#         st.session_state.teacher_login_type = (
#             "login"
#         )

#         return True

#     return False


# # =========================================================
# # TEACHER LOGIN SCREEN
# # =========================================================

# def teacher_screen_login():

#     c1, c2 = st.columns(
#         2,
#         vertical_alignment="center",
#         gap="xlarge"
#     )

#     # =====================================================
#     # HEADER
#     # =====================================================

#     with c1:

#         header_dashboard()

#     # =====================================================
#     # BACK TO HOME
#     # =====================================================

#     with c2:

#         if st.button(
#             "Go back to Home  ⌘ Backspace",
#             type="secondary",
#             key="teacher_login_back",
#             width="stretch"
#         ):

#             st.session_state["login_type"] = None

#             st.session_state["teacher_login_type"] = (
#                 "login"
#             )

#             st.rerun()

#     # =====================================================
#     # HEADING
#     # =====================================================

#     st.markdown(
#         """
#         <h1 style="
#             text-align: center;
#             color: #111111;
#             font-weight: 900;
#             margin-top: 10px;
#             margin-bottom: 30px;
#         ">
#             Teacher Login
#         </h1>
#         """,
#         unsafe_allow_html=True
#     )

#     # =====================================================
#     # USERNAME
#     # =====================================================

#     username = st.text_input(
#         "Username",
#         placeholder="Enter username",
#         key="teacher_username"
#     )

#     # =====================================================
#     # PASSWORD
#     # =====================================================

#     password = st.text_input(
#         "Password",
#         type="password",
#         placeholder="Enter password",
#         key="teacher_password"
#     )

#     # =====================================================
#     # LOGIN
#     # =====================================================

#     if st.button(
#         "Login",
#         type="primary",
#         width="stretch",
#         key="teacher_login_btn"
#     ):

#         if not username or not password:

#             st.warning(
#                 "Please enter username and password."
#             )

#         else:

#             if login_teacher(
#                 username,
#                 password
#             ):

#                 st.success(
#                     "Login successful!"
#                 )

#                 time.sleep(0.5)

#                 st.rerun()

#             else:

#                 st.error(
#                     "Invalid username or password."
#                 )

#     st.write("")

#     # =====================================================
#     # REGISTER
#     # =====================================================

#     if st.button(
#         "Create New Teacher Account",
#         type="secondary",
#         width="stretch",
#         key="teacher_register_btn"
#     ):

#         st.session_state.teacher_login_type = (
#             "register"
#         )

#         st.rerun()


# # =========================================================
# # TEACHER REGISTER SCREEN
# # =========================================================

# def teacher_screen_register():

#     c1, c2 = st.columns(
#         2,
#         vertical_alignment="center",
#         gap="xlarge"
#     )

#     # =====================================================
#     # HEADER
#     # =====================================================

#     with c1:

#         header_dashboard()

#     # =====================================================
#     # BACK TO LOGIN
#     # =====================================================

#     with c2:

#         if st.button(
#             "Back to Login",
#             type="secondary",
#             key="teacher_register_back",
#             width="stretch"
#         ):

#             st.session_state.teacher_login_type = (
#                 "login"
#             )

#             st.rerun()

#     # =====================================================
#     # HEADING
#     # =====================================================

#     st.markdown(
#         """
#         <h1 style="
#             text-align: center;
#             color: #111111;
#             font-weight: 900;
#             margin-top: 10px;
#             margin-bottom: 30px;
#         ">
#             Teacher Registration
#         </h1>
#         """,
#         unsafe_allow_html=True
#     )

#     # =====================================================
#     # NAME
#     # =====================================================

#     name = st.text_input(
#         "Full Name",
#         placeholder="Enter full name",
#         key="teacher_register_name"
#     )

#     # =====================================================
#     # USERNAME
#     # =====================================================

#     username = st.text_input(
#         "Username",
#         placeholder="Enter username",
#         key="teacher_register_username"
#     )

#     # =====================================================
#     # PASSWORD
#     # =====================================================

#     password = st.text_input(
#         "Password",
#         type="password",
#         placeholder="Enter password",
#         key="teacher_register_password"
#     )

#     # =====================================================
#     # CONFIRM PASSWORD
#     # =====================================================

#     confirm_password = st.text_input(
#         "Confirm Password",
#         type="password",
#         placeholder="Confirm password",
#         key="teacher_register_confirm_password"
#     )

#     # =====================================================
#     # REGISTER
#     # =====================================================

#     if st.button(
#         "Register",
#         type="primary",
#         width="stretch",
#         key="teacher_register_submit"
#     ):

#         # -------------------------------------------------
#         # EMPTY CHECK
#         # -------------------------------------------------

#         if (
#             not name
#             or not username
#             or not password
#             or not confirm_password
#         ):

#             st.error(
#                 "Please fill all fields."
#             )

#             return

#         # -------------------------------------------------
#         # PASSWORD CHECK
#         # -------------------------------------------------

#         if password != confirm_password:

#             st.error(
#                 "Passwords do not match."
#             )

#             return

#         # -------------------------------------------------
#         # USERNAME CHECK
#         # -------------------------------------------------

#         try:

#             exists = check_teacher_exists(
#                 username
#             )

#         except Exception as e:

#             st.error(
#                 f"Unable to check username: {e}"
#             )

#             return

#         if exists:

#             st.error(
#                 "Username already exists."
#             )

#             return

#         # -------------------------------------------------
#         # CREATE TEACHER
#         # -------------------------------------------------

#         try:

#             result = create_teacher(
#                 username,
#                 password,
#                 name
#             )

#             if result:

#                 st.success(
#                     "Teacher account created successfully!"
#                 )

#                 time.sleep(0.7)

#                 st.session_state.teacher_login_type = (
#                     "login"
#                 )

#                 st.rerun()

#             else:

#                 st.error(
#                     "Teacher registration failed."
#                 )

#         except Exception as e:

#             st.error(
#                 f"Registration error: {e}"
#             )




import streamlit as st

from src.ui.base_layout import style_background_dashboard, style_base_layout

from src.components.header import header_dashboard
from src.components.footer import footer_dashboard
from src.components.subject_card import subject_card
from src.database.db import check_teacher_exists, create_teacher, teacher_login, get_teacher_subjects, get_attendance_for_teacher
from src.components.dialog_create_subject import create_subject_dialog
from src.components.dialog_share_subject import share_subject_dialog
from src.components.dialog_add_photo import add_photos_dialog

from src.pipelines.face_pipeline import predict_attendance
from src.components.dialog_attendance_results import attendance_result_dialog
import numpy as np

from datetime import datetime

import pandas as pd

from src.database.config import supabase


from src.components.dialog_voice_attendance import voice_attendance_dialog
def teacher_screen():

    style_background_dashboard()
    style_base_layout()

    if "teacher_data" in st.session_state:
        teacher_dashboard()
    elif 'teacher_login_type' not in st.session_state or st.session_state.teacher_login_type=="login":
        teacher_screen_login()
    elif st.session_state.teacher_login_type == "register":
        teacher_screen_register()





def teacher_dashboard():
    teacher_data = st.session_state.teacher_data
    c1, c2 = st.columns(2, vertical_alignment='center', gap='xxlarge')
    with c1:
        header_dashboard()
    with c2:
        st.subheader(f"""Welcome, {teacher_data['name']} """)
        if st.button("Logout", type='secondary', key='loginbackbtn', shortcut="control+backspace"):
            st.session_state['is_logged_in'] = False
            del st.session_state.teacher_data 
            st.rerun()


    st.space()

    if "current_teacher_tab" not in st.session_state:
        st.session_state.current_teacher_tab = 'take_attendance'
    tab1, tab2, tab3 = st.columns(3)


    with tab1:
        type1 = "primary" if st.session_state.current_teacher_tab == 'take_attendance' else "tertiary"
        if st.button('Take Attendance',type=type1, width='stretch', icon=':material/ar_on_you:'):
            st.session_state.current_teacher_tab = 'take_attendance'
            st.rerun()

    with tab2:
        type2 = "primary" if st.session_state.current_teacher_tab == 'manage_subjects' else "tertiary"
        if st.button('Manage Subjects', type=type2, width='stretch', icon=':material/book_ribbon:'):
            st.session_state.current_teacher_tab = 'manage_subjects'
            st.rerun()

    with tab3:
        type3 = "primary" if st.session_state.current_teacher_tab == 'attendance_records' else "tertiary"
        if st.button('Attendance Records',type=type3, width='stretch', icon=':material/cards_stack:'):
            st.session_state.current_teacher_tab = 'attendance_records'
            st.rerun()


    st.divider()

    if st.session_state.current_teacher_tab == "take_attendance":
        teacher_tab_take_attendance()
    if st.session_state.current_teacher_tab == "manage_subjects":
        teacher_tab_manage_subjects()
    if st.session_state.current_teacher_tab == "attendance_records":
        teacher_tab_attendance_records()

    


    footer_dashboard()

def teacher_tab_take_attendance():
    teacher_id = st.session_state.teacher_data['teacher_id']
    st.header('Take AI Attendance')


    if 'attendance_images' not in st.session_state:
        st.session_state.attendance_images = []

    subjects = get_teacher_subjects(teacher_id)

    if not subjects:
        st.warning('You havent created any subjects yet! Please create one to begin!')
        return
    
    subject_options = {f"{s['name']} - {s['subject_code']}": s['subject_id'] for s in subjects}

    col1, col2 = st.columns([3,1], vertical_alignment='bottom')

    with col1:
        selected_subject_label = st.selectbox('Select Subject', options=list(subject_options.keys()))

    with col2:
        if st.button('Add Photos', type='primary', icon=':material/photo_prints:', width='stretch'):
            add_photos_dialog()

    selected_subject_id = subject_options[selected_subject_label]

    st.divider()

    if st.session_state.attendance_images:
        st.header('Added Photos')
        gallery_cols = st.columns(4)

        for idx, img in enumerate(st.session_state.attendance_images):
            with gallery_cols[idx % 4 ]:
                st.image(img, width='stretch', caption=f'Photo {idx+1}')
    has_photos = bool(st.session_state.attendance_images)
    c1, c2, c3 = st.columns(3)

    with c1:
        if st.button('Clear all photos', width='stretch', type='tertiary', icon=':material/delete:', disabled=not has_photos):
            st.session_state.attendance_images = []
            st.rerun()


    with c2:
        
        if st.button('Run Face Analysis', width='stretch', type='secondary', icon=':material/analytics:', disabled=not has_photos):
            with st.spinner('Deep scanning classroom photos...'):
                all_detected_ids = {}

                for idx, img in enumerate(st.session_state.attendance_images):
                    img_np = np.array(img.convert('RGB'))
                    detected, _, _ = predict_attendance(img_np)


                    if detected:
                        for sid in detected.keys():
                            student_id = int(sid)

                            all_detected_ids.setdefault(student_id, []).append(f"Photo {idx+1}")

                enrolled_res = supabase.table('subject_students').select("*, students(*)").eq('subject_id',selected_subject_id ).execute()
                enrolled_students = enrolled_res.data

                if not enrolled_students:
                    st.warning('No students enrolled in this course')
                else:

                    results, attendance_to_log  = [], []

                    current_timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")


                    for node in enrolled_students:
                        student = node['students']
                        sources = all_detected_ids.get(int(student['student_id']), [])
                        is_present= len(sources) > 0

                        results.append({
                            "Name": student['name'],
                            "ID": student['student_id'],
                            "Source": ", ".join(sources) if is_present else "-",
                            "Status": "✅ Present" if is_present else "❌ Absent"
                        })

                        attendance_to_log.append({
                            'student_id': student['student_id'],
                            'subject_id': selected_subject_id,
                            'timestamp': current_timestamp,
                            'is_present': bool(is_present)
                        })

                attendance_result_dialog(pd.DataFrame(results), attendance_to_log)

    with c3:
        if st.button('Use Voice Attendance', type='primary', width='stretch', icon=':material/mic:'):
            voice_attendance_dialog(selected_subject_id)











def teacher_tab_manage_subjects():
    teacher_id = st.session_state.teacher_data['teacher_id']
    col1, col2 = st.columns(2)
    with col1:
        st.header('Manage Subjects', width='stretch')

    with col2:
        if st.button('Create New Subject', width='stretch'):
            create_subject_dialog(teacher_id)


    # LIST all SUBJECTS
    subjects = get_teacher_subjects(teacher_id)
    if subjects:
        for sub in subjects:
            stats = [
                ("🫂", "Students", sub['total_students']),
                ("🕰️", "Classes", sub['total_classes']),
            ]
        def share_btn():
            if st.button(f"Share Code: {sub['name']}", key=f"share_{sub['subject_code']}", icon=":material/share:"):
                share_subject_dialog(sub['name'], sub['subject_code'])
            st.space()

        subject_card(
            name = sub['name'],
            code = sub['subject_code'],
            section = sub['section'],
            stats=stats,
            footer_callback=share_btn
        )
    else:
        st.info("NO SUBJECTS FOUND. CREATE ONE ABOVE")


def teacher_tab_attendance_records():
    st.header('Attendance Records')

    teacher_id = st.session_state.teacher_data['teacher_id']

    records = get_attendance_for_teacher(teacher_id)

    if not records:
        return
    
    data = []

    for r in records:
        ts = r.get('timestamp')

        data.append({
            "ts_group": ts.split(".")[0] if ts else None,
            "Time": datetime.fromisoformat(ts).strftime("%Y-%m-%d %I:%M %p") if ts else "N'A",
            "Subject": r['subjects']['name'],
            "Subject Code":r['subjects']['subject_code'],
            "is_present": bool(r.get('is_present', False))
        })


    df = pd.DataFrame(data)



    summary = (
        df.groupby(['ts_group', 'Time', 'Subject', 'Subject Code'])
        .agg(
            Present_Count = ('is_present', 'sum'),
            Total_Count =('is_present', 'count')
        ).reset_index()

    )

    summary['Attendance Stats'] = (
        "✅ " + summary['Present_Count'].astype(str) + " /"
        + summary['Total_Count'].astype(str) + ' Students'
    )

    display_df = ( summary.sort_values(by='ts_group' ,ascending=False)
                  [['Time', 'Subject', 'Subject Code', 'Attendance Stats']]
                  )
    
    st.dataframe(display_df, width='stretch', hide_index=True)


def login_teacher(username, password):
    if not username or not password:
        return False
    
    teacher = teacher_login(username, password)

    if teacher:
        st.session_state.user_role ='teacher'
        st.session_state.teacher_data = teacher
        st.session_state.is_logged_in = True
        return True
    

    return False
def teacher_screen_login():
    c1, c2 = st.columns(2, vertical_alignment='center', gap='xxlarge')
    with c1:
        header_dashboard()
    with c2:
        if st.button("Go back to Home", type='secondary', key='loginbackbtn', shortcut="control+backspace"):
            st.session_state['login_type'] = None
            st.rerun()

    st.header('Login using password', text_alignment='center')
    st.space()
    st.space()


    teacher_username = st.text_input("Enter username", placeholder='ananyaroy')

    teacher_pass = st.text_input("Enter password", type='password', placeholder="Enter password")

    st.divider()

    btnc1, btnc2 = st.columns(2)

    with btnc1:
        if st.button('Login', icon=':material/passkey:', shortcut='control+enter', width='stretch'):
            if login_teacher(teacher_username, teacher_pass):
                st.toast("welcome back!", icon="👋")
                import time
                time.sleep(1)
                st.rerun()
            else:
                st.error("Invalid username and password combo")

    with btnc2:
        if st.button('Register Instead', type="primary", icon=':material/passkey:', width='stretch'):
            st.session_state.teacher_login_type = 'register'

    footer_dashboard()



def register_teacher(teacher_username, teacher_name, teacher_pass, teacher_pass_confirm):
    if not teacher_username or not teacher_name or not teacher_pass:
        return False, "All Fields are required!"
    if check_teacher_exists(teacher_username):
        return False, "Username already taken"
    if teacher_pass != teacher_pass_confirm:
        return False, "Password doesn't match"
    
    try:
        create_teacher(teacher_username, teacher_pass, teacher_name)
        return True, "Sucessfully Created! Login Now"
    except Exception as e:
        return False, "Unexpected Error!"
    

def teacher_screen_register():
    c1, c2 = st.columns(2, vertical_alignment='center', gap='xxlarge')
    with c1:
        header_dashboard()
    with c2:
        if st.button("Go back to Home", type='secondary', key='loginbackbtn', shortcut="control+backspace"):
            st.session_state['login_type'] = None
            st.rerun()



    st.header('Register your teacher profile')

    st.space()
    st.space()

    
    teacher_username = st.text_input("Enter username", placeholder='ananyaroy')

    teacher_name = st.text_input("Enter name", placeholder='Ananya Roy')

    teacher_pass = st.text_input("Enter password", type='password', placeholder="Enter password")

    teacher_pass_confirm = st.text_input("Confirm your password", type='password', placeholder="Enter password")

    st.divider()

    btnc1, btnc2 = st.columns(2)

    with btnc1:
        if st.button('Register now', icon=':material/passkey:', shortcut='control+enter', width='stretch'):
            success, message = register_teacher(teacher_username, teacher_name, teacher_pass, teacher_pass_confirm)
            if success:
                st.success(message)
                import time
                time.sleep(2)
                st.session_state.teacher_login_type = "login"
                st.rerun()
            else:
                st.error(message)


    with btnc2:
        if st.button('Login Instead', type="primary", icon=':material/passkey:', width='stretch'):
            st.session_state.teacher_login_type = 'login'

    footer_dashboard()