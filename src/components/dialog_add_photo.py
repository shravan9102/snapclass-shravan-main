import streamlit as st
from src.database.db import enroll_student_to_subject
from src.database.config import supabase
from PIL import Image
import time


# @st.dialog("Capture or Upload Photos")
# def add_photos_dialog():

#     st.write("Add classroom photos to scan for attendance")

#     if "photo_tab" not in st.session_state:
#         st.session_state.photo_tab = "camera"

#     t1, t2 = st.columns(2)

#     with t1:
#         type_camera = (
#             "primary"
#             if st.session_state.photo_tab == "camera"
#             else "tertiary"
#         )

#         if st.button(
#             "Camera",
#             type=type_camera,
#             width="stretch"
#         ):
#             st.session_state.photo_tab = "camera"

#     with t2:
#         type_upload = (
#             "primary"
#             if st.session_state.photo_tab == "upload"
#             else "tertiary"
#         )

#         if st.button(
#             "Upload photos",
#             type=type_upload,
#             width="stretch"
#         ):
#             st.session_state.photo_tab = "upload"

#     if st.session_state.photo_tab == "camera":

#         cam_photo = st.camera_input(
#             "Take Snapshot",
#             key="dialog_cam"
#         )

#         if cam_photo:
#             st.session_state.attendance_images.append(
#                 Image.open(cam_photo)
#             )

#             st.toast("Photo Captured")
#             st.rerun()

#     if st.session_state.photo_tab == "upload":

#         uploaded_files = st.file_uploader(
#             "Choose image files",
#             type=["jpg", "png", "jpeg"],
#             accept_multiple_files=True,
#             key="dialog_upload"
#         )

#         if uploaded_files:

#             for f in uploaded_files:
#                 st.session_state.attendance_images.append(
#                     Image.open(f)
#                 )

#             st.toast("Photo Uploaded Successfully")
#             st.rerun()

#     st.divider()

#     if st.button(
#         "Done",
#         type="primary",
#         width="stretch"
#     ):
#         st.rerun()



import streamlit as st
from PIL import Image, ImageOps


# =========================================================
# ADD PHOTOS DIALOG
# =========================================================

@st.dialog("Capture or Upload Photos")
def add_photos_dialog():

    st.write(
        "Add classroom photos to scan for attendance"
    )

    # =====================================================
    # SESSION STATE
    # =====================================================

    if "attendance_images" not in st.session_state:
        st.session_state.attendance_images = []

    if "photo_tab" not in st.session_state:
        st.session_state.photo_tab = "camera"

    if "last_camera_photo" not in st.session_state:
        st.session_state.last_camera_photo = None

    if "uploaded_photo_ids" not in st.session_state:
        st.session_state.uploaded_photo_ids = []

    # =====================================================
    # CAMERA / UPLOAD BUTTONS
    # =====================================================

    tab1, tab2 = st.columns(2)

    # -----------------------------------------------------
    # CAMERA
    # -----------------------------------------------------

    with tab1:

        camera_type = (
            "primary"
            if st.session_state.photo_tab == "camera"
            else "tertiary"
        )

        if st.button(
            "Camera",
            type=camera_type,
            width="stretch",
            key="photo_camera_tab"
        ):

            st.session_state.photo_tab = "camera"

            st.rerun(scope="fragment")

    # -----------------------------------------------------
    # UPLOAD
    # -----------------------------------------------------

    with tab2:

        upload_type = (
            "primary"
            if st.session_state.photo_tab == "upload"
            else "tertiary"
        )

        if st.button(
            "Upload photos",
            type=upload_type,
            width="stretch",
            key="photo_upload_tab"
        ):

            st.session_state.photo_tab = "upload"

            st.rerun(scope="fragment")

    st.divider()

    # =====================================================
    # CAMERA
    # =====================================================

    if st.session_state.photo_tab == "camera":

        st.subheader("Take a classroom photo")

        cam_photo = st.camera_input(
            "Take Snapshot",
            key="dialog_cam"
        )

        if cam_photo is not None:

            photo_id = cam_photo.file_id

            if (
                photo_id
                != st.session_state.last_camera_photo
            ):

                image = Image.open(
                    cam_photo
                ).convert("RGB").copy()

                st.session_state.attendance_images.append(
                    image
                )

                st.session_state.last_camera_photo = (
                    photo_id
                )

                st.toast(
                    "Photo captured successfully!",
                    icon="📸"
                )

                st.rerun(scope="fragment")

    # =====================================================
    # UPLOAD PHOTOS
    # =====================================================

    elif st.session_state.photo_tab == "upload":

        st.subheader("Upload classroom photos")

        uploaded_files = st.file_uploader(
            "Choose image files",
            type=[
                "jpg",
                "jpeg",
                "png"
            ],
            accept_multiple_files=True,
            key="dialog_upload"
        )

        if uploaded_files:

            new_photos = 0

            for file in uploaded_files:

                file_id = (
                    file.name,
                    file.size,
                    file.file_id
                )

                # Prevent duplicate upload
                if (
                    file_id
                    not in st.session_state.uploaded_photo_ids
                ):

                    image = Image.open(
                        file
                    ).convert("RGB").copy()

                    st.session_state.attendance_images.append(
                        image
                    )

                    st.session_state.uploaded_photo_ids.append(
                        file_id
                    )

                    new_photos += 1

            if new_photos > 0:

                st.toast(
                    f"{new_photos} photo(s) added successfully!",
                    icon="📷"
                )

                st.rerun(scope="fragment")

    # =====================================================
    # PREVIEW PHOTOS INSIDE DIALOG
    # =====================================================

    st.divider()

    st.subheader(
        f"Selected Photos: "
        f"{len(st.session_state.attendance_images)}"
    )

    if st.session_state.attendance_images:

        preview_cols = st.columns(3)

        for index, image in enumerate(
            st.session_state.attendance_images
        ):

            with preview_cols[index % 3]:

                # Same preview size
                preview = ImageOps.contain(
                    image,
                    (220, 150)
                )

                st.image(
                    preview,
                    width=220
                )

                st.caption(
                    f"Photo {index + 1}"
                )

    else:

        st.info(
            "No photos added yet."
        )

    # =====================================================
    # DONE
    # =====================================================

    st.divider()

    if st.button(
        "Done",
        type="primary",
        width="stretch",
        key="photo_done"
    ):

        st.rerun()