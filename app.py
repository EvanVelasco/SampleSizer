import streamlit as st
from tabs.tab1 import show_tab1
from tabs.tab2 import show_tab2
from tabs.tab3 import show_tab3

def main():
    tab1, tab2, tab3 = st.tabs(["SRS-Total", "SRS-Mean", "SRS-Proportion"])

    with tab1:
        show_tab1()
    with tab2:
        show_tab2()
    with tab3:
        show_tab3()


if __name__ == "__main__":
    main()