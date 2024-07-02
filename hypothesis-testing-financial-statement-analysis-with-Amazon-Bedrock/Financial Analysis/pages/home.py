import streamlit as st


def show_home():
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
            </style>
            """,
            unsafe_allow_html=True
        )
    # st.header("Home")
    st.title("Empowering analysts to perform hypothesis testing , cause-effect analysis and financial statement analysis efficiently with Anthropic Claude 3 on Amazon Bedrock", False)
    st.image("/home/ec2-user/SageMaker/amazon-bedrock-quick-start/claude_3_examples/Financial analysis/Slide1.png", use_column_width=True)
    new_title = """<p style="font-size: 25px;">Analysts in financial services have to deal with variety of data from various sources. The required data comes from multiple sources, making data consolidation and performing insightful analysis within short time to be challenging. Analysts likely use a variety of tools and software to perform their analysis tasks. However, there is a need for timely and rapid analysis of data to derive insights within tight deadlines. Often analysts must provide both qualitative (interpretive) and quantitative (numbers-based) insights from their analysis. Using Anthropic's Claude 3 Sonnet model on Amazon Bedrock with financial data can enable financial analysts to provide contextual insights from various data modalities (image, text). It can help enhance analysts' productivity through the ability to perform financial analysis and calculations efficiently, thereby reducing time.</p>"""
    st.markdown(new_title, unsafe_allow_html=True)
    st.image("/home/ec2-user/SageMaker/amazon-bedrock-quick-start/claude_3_examples/Financial analysis/Slide2.png", use_column_width=True)
    st.image("/home/ec2-user/SageMaker/amazon-bedrock-quick-start/claude_3_examples/Financial analysis/Slide3.png", use_column_width=True)
    st.image("/home/ec2-user/SageMaker/amazon-bedrock-quick-start/claude_3_examples/Financial analysis/Slide4.png", use_column_width=True)