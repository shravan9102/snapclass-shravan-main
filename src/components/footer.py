

import streamlit as st


def footer_home():

    st.markdown(
        """
        <div style="
            margin-top: 2rem;
            width: 100%;
            display: flex;
            justify-content: center;
            align-items: center;
        ">
            <p style="
                margin: 0;
                color: white;
                font-size: 16px;
                font-weight: 500;
            ">
                Created with ❤️ by
                <b style="color: white;">Shravan</b>
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )


def footer_dashboard():

    st.markdown(
        """
        <div style="
            margin-top: 2rem;
            width: 100%;
            display: flex;
            justify-content: center;
            align-items: center;
        ">
            <p style="
                margin: 0;
                color: black;
                font-size: 16px;
                font-weight: 500;
            ">
                Created with ❤️ by
                <b style="color: black;">Shravan</b>
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )