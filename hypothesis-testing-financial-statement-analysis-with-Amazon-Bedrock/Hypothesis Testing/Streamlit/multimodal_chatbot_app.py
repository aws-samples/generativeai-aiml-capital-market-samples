import streamlit as st #all streamlit commands will be available through the "st" alias
import multimodal_chatbot_lib as glib #reference to local lib script
from streamlit_extras.stylable_container import stylable_container

st.set_page_config(page_title="Hypothesis Testing") #HTML title
st.title("Hypothesis Testing and cause-effect analysis for investment research") #page title

if 'chat_history' not in st.session_state: #see if the chat history hasn't been created yet
    st.session_state.chat_history = [] #initialize the chat history

chat_container = st.container()

input_text = st.chat_input("Chat with your bot here") #display a chat input box

uploaded_file = st.file_uploader("Select an image", type=['png', 'jpg'], label_visibility="collapsed")

prompt = """Following are the 6 event categories: 
1. Wars and Military Conflicts, 
2. Economic Events, 
3. Political Events,       
4. Technological Innovations, 
5. Social and Cultural Events, 
6. Natural Disasters
Use the image to Categorize the events (graph annotated text, number, year) into 6 broad categories mentioned above. 
Interpret the chart and give your answer in a table with following columns. 
Category, Event, Date, Impact of event on Dow Jones Index (Positive, Negative, Neutral), Price movement (Uptend, Downtrend, Sideways)
Sort the table chronologically on column “Date" overall. 
Do not sort the table after grouping the categories. Sort it for all rows in the table chronologically.
Give atleast 200 events (200 rows) for the table.
Do NOT provide just the sample table. From the image display ALL the rows with the given prompt above.
print all the rows into the 6 categories. Do not create any data other than the ones in the image."""

prompt1 = """Fill out all the 200+ rows. Do not create any new data. Use the image to provide all the rows with the previous prompt"""
prompt2 = """Build a pivot table out of the generated table. For the pivot table, rows will be category and columns will be price movement and values will be count of price movement. Create a new column in the pivot table with total for each row. Create a grand total for each column."""
prompt3 = """Create a new table from the generated pivot table and convert the counts into percentages. When you are calculating the percentage, the sum of percentages of each row should add up to 100"}]
Here's a new table created from the pivot table, converting the counts into percentages, with the sum of percentages for each row adding up to 100%. Interpret the table."""
prompt4 = """Identify what war events have positive impact on price action ? Give the response in a table."""
prompt5 = """Identify what political events have positive impact on price action ? Give the response in a table."""
st.markdown("""
<style>
    [data-testid=stSidebar] {
        background-color: rgba(57,22,126,255);
    }
</style>
""", unsafe_allow_html=True)
with st.sidebar:
    protemp = """<p style="font-family: serif; font-size: 25px; font-weight: 400; 
    color:White;">Prompt Questions</p>"""
    # st.write("Prompt Questions")
    st.markdown(protemp, unsafe_allow_html=True)
    with stylable_container(
        "codeblock",
        """
        code {
            white-space: pre-wrap !important;
            font-family: "serif";
            font-size: 20px;
        }
        """,):
        st.code((prompt), language=None)
        st.code(prompt1, language=None)
        st.code(prompt2, language=None)
        st.code(prompt3, language=None)
        st.code(prompt4, language=None)
        st.code(prompt5, language=None)
    
    
# col1, col2, col3 = st.columns(3)
# with col1:
#     upload_image_1 = st.button("Add miniature house image")

# with col2:
#     upload_image_2 = st.button("Add house and car image")

# with col3:
#     upload_image_3 = st.button("Add miniature car image")

# if upload_image_1:
#     image_bytes = glib.get_bytes_from_file("images/minihouse.jpg")
#     glib.chat_with_model(message_history=st.session_state.chat_history, new_text=None, new_image_bytes=image_bytes)
    
# elif upload_image_2:
#     image_bytes = glib.get_bytes_from_file("images/house_and_car.jpg")
#     glib.chat_with_model(message_history=st.session_state.chat_history, new_text=None, new_image_bytes=image_bytes)

# elif upload_image_3:
#     image_bytes = glib.get_bytes_from_file("images/minicar.jpg")
#     glib.chat_with_model(message_history=st.session_state.chat_history, new_text=None, new_image_bytes=image_bytes)

if input_text: #run the code in this if block after the user submits a chat message
    glib.chat_with_model(message_history=st.session_state.chat_history, new_text=input_text, new_image_bytes=None)

elif uploaded_file:
    image_bytes = uploaded_file.getvalue()
    
    glib.chat_with_model(message_history=st.session_state.chat_history, new_text=None, new_image_bytes=image_bytes)
    
#Re-render the chat history (Streamlit re-runs this script, so need this to preserve previous chat messages)
for message in st.session_state.chat_history: #loop through the chat history
    with chat_container.chat_message(message.role): #renders a chat line for the given role, containing everything in the with block
        if (message.message_type == 'image'):
            st.image(message.bytesio)
        else:
            st.markdown(message.text) #display the chat content

