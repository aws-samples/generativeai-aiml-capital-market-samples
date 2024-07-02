import streamlit as st #all streamlit commands will be available through the "st" alias
import multimodal_chatbot_lib as glib #reference to local lib script
import re
from streamlit_navigation_bar import st_navbar
from streamlit_extras.stylable_container import stylable_container


def show_prompting():
    # st.header("Prompting")
    # st.set_page_config(page_title="Financial Analysis using Claude 3 Sonnet") #HTML title
    styles = {
        "nav": {
            "background-color": "rgb(123, 209, 146)",
        },
        "div": {
            "max-width": "32rem",
        },
        "span": {
            "border-radius": "0.5rem",
            "color": "rgb(49, 51, 63)",
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
    st.title("Financial Analysis using Claude 3 Sonnet") #page title
    # page = st_navbar(["Home", "Documentation", "Examples", "Community", "About"])
    # st.write(page)
    with st.container():
        st.markdown(
            """
            <style>
            .block-container > div {
                width: 85%;
                margin: auto;
            }
            .st-emotion-cache-13ln4jf {
                width: 100%;
                padding: 6rem 1rem 10rem;
                max-width: 70rem;
            }
            .st-emotion-cache-vdokb0 p {
            font-size: 20px;
            font-family: "serif";
            }
            .st-emotion-cache-vdokb0 li {
            font-size: 20px;
            font-family: "serif";
            }
            table {
            font-size: 20px;
            font-family: "serif";
            }
            </style>
            """,
            unsafe_allow_html=True
        )
       
    if 'chat_history' not in st.session_state: #see if the chat history hasn't been created yet
        st.session_state.chat_history = [] #initialize the chat history

    chat_container = st.container()

    input_text = st.chat_input("Chat with your bot here") #display a chat input box

    uploaded_file = st.file_uploader("Select an image", type=['png', 'jpg'], label_visibility="collapsed")

    if input_text: #run the code in this if block after the user submits a chat message
        with st.spinner("Waiting for Response..."):
            glib.chat_with_model(message_history=st.session_state.chat_history, new_text=input_text, new_image_bytes=None)

    elif uploaded_file:
        image_bytes = uploaded_file.getvalue()
        with st.spinner("Waiting for Response..."):
            glib.chat_with_model(message_history=st.session_state.chat_history, new_text=None, new_image_bytes=image_bytes)

    #Re-render the chat history (Streamlit re-runs this script, so need this to preserve previous chat messages)
    for message in st.session_state.chat_history: #loop through the chat history
        with chat_container.chat_message(message.role): #renders a chat line for the given role, containing everything in the with block
            if (message.message_type == 'image'):
                st.image(message.bytesio)
            else:
                # math_pattern = r'\$(?!\$)(?:[^\$]|(?:\$\$))*\$'

                temp = message.text
                # temp = re.sub(math_pattern, '', temp)
                temp = temp.replace('$', '')
                temp = temp.replace('\\', '')
                st.markdown(temp)