import streamlit as st

def subject_card(name, code, section, stats=None, footer_callback=None):
    html = f"""
    <div style="
        background: white;
        border: 1px solid #000000;
        border-left: 8px solid #EB459E;
        padding: 25px;
        border-radius: 20px;
        margin-bottom: 15px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
    ">
        <h3 style="
            margin: 0;
            color: #1e293b;
            font-size: 1.5rem;
            font-weight: 600;
        ">
            {name}
        </h3>
        <p style="
            color: #64748b;
            margin: 12px 0;
            font-size: 1rem;
        ">
            Code :
            <span style="
                background: #E0E3FF;
                color: #5865F2;
                padding: 3px 8px;
                border-radius: 5px;
            ">
                {code}
            </span>
            &nbsp; | &nbsp;
            Section :
            <b>{section}</b>
        </p>
    """

    if stats:
        html += """
        <div style="
            display: flex;
            gap: 20px;
            flex-wrap: wrap;
            margin-top: 15px;
        ">
        """
        for icon, label, value in stats:
            html += f"""
            <div style="
                color: #334155;
                font-size: 0.9rem;
            ">
                {icon} <b>{value}</b> {label}
            </div>
            """
        html += "</div>"

    html += "</div>"

    st.html(html)

    if footer_callback:
        footer_callback()