import streamlit as st
from tabs.tab1 import show_tab1
from tabs.tab2 import show_tab2

def main():
    tab1, tab2 = st.tabs(["SRS-Total", "SRS-Mean"])

    with tab1:
        show_tab1()
    with tab2:
        show_tab2()


if __name__ == "__main__":
    main()