
import streamlit as st
import pandas as pd
from agent.screening_agent import LoanScreeningAgent

st.set_page_config(page_title="University Loan AI Agent", layout="wide")
st.title("🏦 AI Loan Screening & Risk Assessment Agent")

agent = LoanScreeningAgent()
uploaded = st.file_uploader("Upload CSV", type=["csv"])

if uploaded:
    df = pd.read_csv(uploaded)
    results = agent.process(df)
    st.dataframe(results, use_container_width=True)
    st.download_button("Download Results", results.to_csv(index=False), "results.csv")
