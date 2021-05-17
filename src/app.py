import streamlit as st
from pages import data_backup

PAGES = {
    'first_page': data_backup,
}


def main():
    title = st.empty()
    st.sidebar.title("CMB Quick Managerment Toolkit")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))

    page = PAGES[selection]
    page.main()


if __name__ == "__main__":
    main()

