import os

import streamlit as st
from streamlit_navigation_bar import st_navbar


import pages as pg
from pages.home import show_home
from pages.promptexamples import show_promptexamples
from pages.prompting import show_prompting
# from pages.home import show_home



# st.set_page_config(initial_sidebar_state="collapsed")
st.set_page_config(layout='wide',initial_sidebar_state='collapsed',)

pages = ["Home", "Prompt Questions", "Analyze"]
# parent_dir = os.path.dirname(os.path.abspath(__file__))
# logo_path = os.path.join(parent_dir, "cubes.svg")
# urls = {"GitHub": "https://github.com/gabrieltempass/streamlit-navigation-bar"}
# styles = {
#     "nav": {
#         "background-color": "royalblue",
#         "justify-content": "left",
#     },
#     "img": {
#         "padding-right": "14px",
#     },
#     "span": {
#         "color": "white",
#         "padding": "14px",
#     },
#     "active": {
#         "background-color": "white",
#         "color": "var(--text-color)",
#         "font-weight": "normal",
#         "padding": "14px",
#     }
# }
styles = {
    "nav": {
        "background-color": "rgb(57, 22, 126)",
        "height": "6rem",
        "color": "rgb(255,255,255)"
    },
    "div": {
        "max-width": "60rem",
        "font-size": "1.5rem",
        # "min-height": "5rem"
    },
    "span": {
        "border-radius": "0.5rem",
        "color": "rgb(255,255,255)",
        "margin": "0 0.125rem",
        "padding": "0.4375rem 0.625rem",
    },
    "active": {
        "background-color": "rgba(255, 255, 255, 0.25)",
    },
    "hover": {
        "background-color": "rgba(255, 255, 255, 0.35)",
    },
}
options = {
    "show_menu": True,
    "show_sidebar": False,
}

page = st_navbar(
    pages,
    styles=styles,
    options=options,
)

functions = {
    "Home": show_home,
    "Prompt Questions": show_promptexamples,
    "Analyze": show_prompting,
    # "User Guide": pg.show_user_guide,
    # "API": pg.show_api,
    # "Examples": pg.show_examples,
    # "Community": pg.show_community,
}
go_to = functions.get(page)
if go_to:
    go_to()