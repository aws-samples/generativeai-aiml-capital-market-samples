import streamlit as st
import textwrap as tw

from streamlit_extras.stylable_container import stylable_container

def show_promptexamples():

    # st.header("Prompt Examples")
    styles = {
        "html": {
            "font-family": "serif",
        },
        "body": {
            "font-family": "serif",
        },
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
    st.title("Prompt Questions to analyze financial statements", False)

    prompt = """Perform a financial analysis by calculating the ratios from the data in the images. 
    Interpret the ratios. 
    Give your answer in Tabular format indifferent section with 3 columns - Ratios for that section, Ratio calculation, Interpretation for the ratio values. 
    For every ratio give calculations/basis/justifications. 
    Do not make up answers/numbers/data. 
    Answer only if you know it.

    Activity Ratios:

    | Activity Ratios | Ratio calculation |
    |-----------------|-------------------|
    | Inventory turnover | Cost of goods sold / Average inventory |
    | Days of inventory on hand (DOH) | Number of days in period / Inventory turnover |
    | Receivables turnover | Revenue or Net credit sales / Average receivables |
    | Days of sales outstanding (DSO) | Number of days in period / Receivables turnover |
    | Payable Turnover | Purchases / Average payables |
    | Number of days of payables | Number of days in period / Payable turnover |
    | Working capital turnover | Revenue / Average working capital |
    | Fixed assets turnover | Revenue / Average fixed assets |
    | Total assets turnover | Revenue / Average total assets |
    """
    prompt1 = """Perform a financial analysis by calculating the ratios from the data in the images. 
    Interpret the ratios. 
    Give your answer in Tabular format indifferent section with 3 columns - Ratios for that section, Ratio calculation, Interpretation for the ratio values. 
    For every ratio give calculations/basis/justifications. 
    Do not make up answers/numbers/data. 
    Answer only if you know it.

    Liquidity Ratios:

    | Liquidity ratios | Ratio calculation |
    |-----------------|-------------------|
    | Current | Current assets / Current liabilities |
    | Quick | (Cash + Short-term marketable securities + Receivables) / Current liabilities |
    | Cash | (Cash + Short-term marketable securities) / Current liabilities |
    | Defensive interval | (Cash + Short-term marketable securities + Receivables) / Daily expenditures |
    | Cash conversion cycle | DOH + DSO - Number of days of payables |
    """

    prompt2 = """Perform a financial analysis by calculating the ratios from the data in the images. 
    Interpret the ratios. 
    Give your answer in Tabular format indifferent section with 3 columns - Ratios for that section, Ratio calculation, Interpretation for the ratio values. 
    For every ratio give calculations/basis/justifications. 
    Do not make up answers/numbers/data. 
    Answer only if you know it.
    Solvency Ratios:

    | Solvency ratios | Ratio calculation |
    |-----------------|-------------------|
    | Debt-to-assets | Total debt / Total assets |
    | Debt-to-capital | Total debt / (Total debt + Total shareholders' equity) |
    | Debt-to-equity | Total debt / Total shareholders' equity |
    | Financial leverage | Average total assets / Average shareholders' equity |
    """

    prompt3 = """Perform a financial analysis by calculating the ratios from the data in the images. 
    Interpret the ratios. 
    Give your answer in Tabular format indifferent section with 3 columns - Ratios for that section, Ratio calculation, Interpretation for the ratio values. 
    For every ratio give calculations/basis/justifications. 
    Do not make up answers/numbers/data. 
    Answer only if you know it.

    Coverage Ratios:

    | Coverage Ratios | Ratio calculation |
    |-----------------|-------------------|
    | Interest coverage | EBIT / Interest expense |
    | Fixed charge coverage | EBIT + Lease payments / (Interest expense + Lease payments) |
    """

    prompt4 = """Perform a financial analysis by calculating the ratios from the data in the images. 
    Interpret the ratios. 
    Give your answer in Tabular format indifferent section with 3 columns - Ratios for that section, Ratio calculation, Interpretation for the ratio values. 
    For every ratio give calculations/basis/justifications. 
    Do not make up answers/numbers/data. 
    Answer only if you know it.

    Profitability Ratios:

    | Return on sales ratios | Ratio calculation |
    |------------------------|-------------------|
    | Gross profit margin | Gross profit / Revenue |
    | Operating margin | Operating profit / Revenue |
    | Pretax margin | EBT (Earnings before taxes) / Revenue |
    | Net profit margin | Net income / Revenue |
    """

    prompt5 = """Perform a financial analysis by calculating the ratios from the data in the images. 
    Interpret the ratios. 
    Give your answer in Tabular format indifferent section with 3 columns - Ratios for that section, Ratio calculation, Interpretation for the ratio values. 
    For every ratio give calculations/basis/justifications. 
    Do not make up answers/numbers/data. 
    Answer only if you know it.

    | Return on investment ratios | Ratio calculation |
    |----------------------------|-------------------|
    | Operating ROA | Operating profit / Average total assets |
    | ROA | Net income / Average total assets |
    | Return on total capital | EBIT / (Debt + Equity) |
    | ROE | Net income / Average total equity |
    | Return on common equity | Net income - Preferred dividends / Average common equity |
    """

    prompt6 = """Perform a financial analysis by calculating the ratios from the data in the images. 
    Interpret the ratios. 
    Give your answer in Tabular format indifferent section with 3 columns - Ratios for that section, Ratio calculation, Interpretation for the ratio values. 
    For every ratio give calculations/basis/justifications. 
    Do not make up answers/numbers/data. 
    Answer only if you know it.

    Valuation Ratios:

    | Valuation ratios | Ratio calculation |
    |------------------|-------------------|
    | P/E | Stock price / Earnings per share |
    | PCP | Stock price / Cash flow per share |
    | PS | Stock price / Sales per share |
    | PBV | Book per share / Average book value per share |
    """

    prompt7 = """Perform a financial analysis by calculating the ratios from the data in the images. 
    Interpret the ratios. 
    Give your answer in Tabular format indifferent section with 3 columns - Ratios for that section, Ratio calculation, Interpretation for the ratio values. 
    For every ratio give calculations/basis/justifications. 
    Do not make up answers/numbers/data. 
    Answer only if you know it.

    | Price per share | Ratio calculation |
    |-----------------|-------------------|
    | Basic EPS | (Net income - Preferred dividends) / Weighted average number of ordinary shares outstanding |
    | Diluted EPS | (Net income - Preferred dividends) / Weighted number of ordinary shares outstanding + Potential dilutive effects of options, warrants, convertible securities that have been issued at conversion |
    | Cash flow per share | Cash flow from operations / Weighted average number of ordinary shares outstanding |
    | EBITDA per share | EBITDA / Average number of common stock |
    | Dividends per share | Dividends paid / Number of shares outstanding |

    """

    prompt8 = """Perform a financial analysis by calculating the ratios from the data in the images. 
    Interpret the ratios. 
    Give your answer in Tabular format indifferent section with 3 columns - Ratios for that section, Ratio calculation, Interpretation for the ratio values. 
    For every ratio give calculations/basis/justifications. 
    Do not make up answers/numbers/data. 
    Answer only if you know it.

    | Dividend-related ratios | Ratio calculation |
    |-------------------------|-------------------|
    | Dividend payout ratio | Common share dividends / Net income attributable to common shares |
    | Retention rate (k) | Net income attributable to common shares - Common share dividends / Net income attributable to common shares |
    | Sustainable growth rate | b x ROE |
    """

    prompt9 = """Perform a financial analysis by calculating the ratios from the data in the images. 
    Interpret the ratios. 
    Give your answer in Tabular format indifferent section with 3 columns - Ratios for that section, Ratio calculation, Interpretation for the ratio values. 
    For every ratio give calculations/basis/justifications. 
    Do not make up answers/numbers/data. 
    Answer only if you know it.

    Solvency Ratios:

    | Ratio per share | Ratio calculation |
    |-----------------|-------------------|
    | EBIT interest coverage | EBIT / Gross interest prior to deductions for capitalized interest or interest income |
    | EBITDA interest coverage | EBITDA / Gross interest prior to deductions for capitalized interest or interest income |
    """

    prompt10 = """Perform a financial analysis by calculating the ratios from the data in the images. 
    Interpret the ratios. 
    Give your answer in Tabular format indifferent section with 3 columns - Ratios for that section, Ratio calculation, Interpretation for the ratio values. 
    For every ratio give calculations/basis/justifications. 
    Do not make up answers/numbers/data. 
    Answer only if you know it.

    Price per Share:

    | Price per share | Ratio calculation |
    |-----------------|-------------------|
    | FFO (Funds from operations) divided by debt | FFO + Interest paid - Operating lease adjustments - Gains/losses from property sales + Straight-line interest or implied income |
    | Return on capital | EBIT / Average capital |
    | FFO (Funds from operations) to debt | FFO / Total debt |
    | Free operating cash flow to debt | CFO (Adjusted) - Capital expenditures - Dividends paid / Total debt |
    | Discretionary cash flow to debt | CFO - Capital expenditures - Dividend paid / Total debt |
    | Net cash flow-to-capital expenditures | FFO - Dividends / Capital expenditures |
    """
    prompt11 = """Perform a financial analysis by calculating the ratios from the data in the images. 
    Interpret the ratios. 
    Give your answer in Tabular format indifferent section with 3 columns - Ratios for that section, Ratio calculation, Interpretation for the ratio values. 
    For every ratio give calculations/basis/justifications. 
    Do not make up answers/numbers/data. 
    Answer only if you know it.

    Leverage Ratios:

    | Leverage Ratios |
    |-----------------|
    | Debt-to-assets ratio |
    | Debt-to-capital ratio |
    | Debt-to-equity ratio |
    | Financial leverage ratio |

    * Debt is defined as the sum of interest-bearing short-term and long-term debt.
    """


    prompt12 = """Perform a financial analysis by calculating the ratios from the data in the images. 
    Interpret the ratios. 
    Give your answer in Tabular format indifferent section with 3 columns - Ratios for that section, Ratio calculation, Interpretation for the ratio values. 
    For every ratio give calculations/basis/justifications. 
    Do not make up answers/numbers/data. 
    Answer only if you know it.

    Segment Ratios:

    | Segment ratio | Numerator | Denominator | Indication |
    |---------------|------------|--------------|-------------|
    | Segment margin | Segment profit (loss) | Segment revenue | Measures a segment's profitability relative to its revenue. |
    | Segment turnover | Segment revenue | Segment assets | Measures a segment's efficiency in using its assets. |
    | Segment ROA | Segment profit (loss) | Segment assets | Measures a segment's profitability relative to its assets. |
    | Segments' sales ratio | Segment liabilities | Segment assets | Measures a segment's leverage. |

    """


    prompt13 = """Perform a financial analysis by calculating the ratios from the data in the images. 
    Interpret the ratios. 
    Give your answer in Tabular format indifferent section with 3 columns - Ratios for that section, Ratio calculation, Interpretation for the ratio values. 
    For every ratio give calculations/basis/justifications. 
    Do not make up answers/numbers/data. 
    Answer only if you know it.

    Performance Ratios:

    | Leverage Ratios | Calculation | Indication |
    |-----------------|--------------|------------|
    | Cash flow to income | CFO / Net income | Operating cash generated per dollar of net income |
    | Cash return on assets | CFO / Average total assets | Operating cash generated per dollar of assets investment |
    | Cash return on equity | CFO / Average shareholders' equity | Operating cash generated per dollar of owners investment |
    | Cash to income | CFO / Operating income | Cash generated from operations |
    | Cash flow per share | (CFO - Dividends) / Number of common shares outstanding | Operating cash flow on a per share basis |
    | Debt payment | CFO / Long-term debt | Ability to pay debts with operating cash flows |
    | Dividend payment | CFO / Dividends paid | Ability to pay dividends with operating cash flows |
    | Investing and Financing | CFO / (Capital expenditures + Financing activities) | Ability to acquire assets, pay debts, and pay dividends to owners |
    | Debt coverage | CFO / Total debt | Financial risk and financial leverage |
    | Interest Coverage | (CFO + Interest paid + Taxes paid) / Interest expense | Ability to meet interest obligations |
    | Deinvestment | CFO / (Cash paid for long-term assets) | Ability to acquire assets with operating cash flows |
    """
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
            .st-emotion-cache-1jmvea6 p {
                font-size: 20px;
                font-weight: bold;
                font-family: "serif";
            }
            .st-emotion-cache-vdokb0 li {
                font-family: "serif";
                font-size: 20px;
            }
            .st-emotion-cache-vdokb0 p {
                font-family: "serif";
                font-size: 20px;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
    with st.container():

        st.markdown("Give the response in bullet points")
        st.subheader("From the Balance Sheet:", False)
        # st.write("How much debt does the company have?")
        st.markdown("- How much debt does the company have?")
        st.markdown("- Does the company have more current assets and current liabilities?")
        st.markdown("- Does the company have a lot of goodwill on its balance sheet?")

        st.subheader("From the Income Statement:", False)
        # st.write("How much debt does the company have?")
        st.markdown("- Are revenues steadily increasing over time?")
        st.markdown("- Does the company need a lot of COGS to sell its products?")
        st.markdown("- How much revenue is translated into net income?")

        st.subheader("From the Cash Flow Statement", False)
        # st.write("How much debt does the company have?")
        st.markdown("- Are most earnings translated into operating cash flow?")
        st.markdown("- Does the company have positive free cash flow (operating cash flow - CAPEX)?")
        st.markdown("- Did the company manage to increase its cash position compared to last year?")
    # with stylable_container(
    #     "codeblock",
    #     """
    #     code {
    #         white-space: pre-wrap !important;
    #         font-family: "serif";
    #         font-size: 20px;
    #     },
    # """,):
    #     st.code("How much debt does the company have?", language="None")
    #     st.code("Does the company have more current assets and current liabilities?", language="None")
    #     st.code("Does the company have a lot of goodwill on its balance sheet?", language="None")
    with st.expander("Activity Ratios:"):
        with stylable_container(
        "codeblock",
        """
        code {
            white-space: pre-wrap !important;
            font-family: "serif";
            font-size: 20px;
        }
        """,):
            st.code(prompt, language="None")
    with st.expander("Liquidity Ratios:"):
        with stylable_container(
        "codeblock",
        """
        code {
            white-space: pre-wrap !important;
        }
        """,):
            st.code(prompt1, language="None")
    with st.expander("Solvency Ratios:"):
        with stylable_container(
        "codeblock",
        """
        code {
            white-space: pre-wrap !important;
        }
        """,):
            st.code(prompt2, language="None")
    with st.expander("Coverage Ratios:"):
        with stylable_container(
        "codeblock",
        """
        code {
            white-space: pre-wrap !important;
        }
        """,):
            st.code(prompt3, language="None")
    with st.expander("Profitability Ratios:"):
        with stylable_container(
        "codeblock",
        """
        code {
            white-space: pre-wrap !important;
        }
        """,):
            st.code(prompt4, language="None")
    with st.expander("Return on investment ratios:"):
        with stylable_container(
        "codeblock",
        """
        code {
            white-space: pre-wrap !important;
        }
        """,):
            st.code(prompt5, language="None")
    with st.expander("Valuation Ratios:"):
        with stylable_container(
        "codeblock",
        """
        code {
            white-space: pre-wrap !important;
        }
        """,):
            st.code(prompt6, language="None")
    with st.expander("EPS Ratios:"):
        with stylable_container(
        "codeblock",
        """
        code {
            white-space: pre-wrap !important;
        }
        """,):
            st.code(prompt7, language="None")
    with st.expander("Dividend-related ratios:"):
        with stylable_container(
        "codeblock",
        """
        code {
            white-space: pre-wrap !important;
        }
        """,):
            st.code(prompt8, language="None")
    with st.expander("Interest Coverage Ratios:"):
        with stylable_container(
        "codeblock",
        """
        code {
            white-space: pre-wrap !important;
        }
        """,):
            st.code(prompt9, language="None")
    with st.expander("Price per Share Ratios:"):
        with stylable_container(
        "codeblock",
        """
        code {
            white-space: pre-wrap !important;
        }
        """,):
            st.code(prompt10, language="None")
    with st.expander("Leverage Ratios:"):
        with stylable_container(
        "codeblock",
        """
        code {
            white-space: pre-wrap !important;
        }
        """,):
            st.code(prompt11, language="None")
    with st.expander("Segment Ratios:"):
        with stylable_container(
        "codeblock",
        """
        code {
            white-space: pre-wrap !important;
        }
        """,):
            st.code(prompt12, language="None")
    with st.expander("Performance Ratios:"):
        with stylable_container(
        "codeblock",
        """
        code {
            white-space: pre-wrap !important;
        }
        """,):
            st.code(prompt13, language="None")
        # st.code((prompt))
    #     st.code("\n".join(tw.wrap(prompt)))
    # with st.expander("Prompt 2"):
    #     st.code((prompt1))
    # with st.expander("Prompt 3"):
    #     st.code((prompt2))
    # with st.expander("Prompt 4"):
    #     st.code((prompt3))
    # with st.expander("Prompt 5"):
    #     st.code((prompt4))
    # with st.expander("Prompt 6"):
    #     st.code((prompt5))
    # with st.expander("Prompt 7"):
    #     st.code((prompt6))
    # with st.expander("Prompt 8"):
    #     st.code((prompt7))
    # with st.expander("Prompt 9"):
    #     st.code((prompt8))
    # with st.expander("Prompt 10"):
    #     st.code((prompt9))
    # with st.expander("Prompt 11"):
    #     st.code((prompt10))
    # with st.expander("Prompt 12"):
    #     st.code((prompt11))
    # with st.expander("Prompt 13"):
    #     st.code((prompt12))
    # with st.expander("Prompt 14"):
    #     st.code((prompt13))
