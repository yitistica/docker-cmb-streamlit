import streamlit as st


def sftp_section():
    c1, c2, c3 = st.beta_columns((1, 3, 1))

    with c2:
        st.markdown("#### run sftp check")


def main():
    sftp_section()

