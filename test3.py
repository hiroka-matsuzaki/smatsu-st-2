import streamlit as st
from streamlit_option_menu import option_menu

# 5. Add on_change callback
def on_change(key):
    selection = st.session_state[key]
    # st.write(f"Selection changed to {selection}")

selected5 = option_menu(None, ["Home", "Upload", "Tasks", 'Settings'],
        icons=['house', 'cloud-upload', "list-task", 'gear'],
        menu_icon="cast", default_index=0, 
        styles={
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "orange", "font-size": "25px"}, 
            "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "green"},
        },
        on_change=on_change, key='menu_5', orientation="horizontal")
selected5