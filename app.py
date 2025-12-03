import streamlit as st
import pandas as pd
import plotly.express as px

st.title("FEMA Disaster Relief Dashboard")
st.write("Authors: Nahisha Ashraf & Jessica Groyon")

# Load the FEMA CSV that you committed to the repo
df = pd.read_csv(
    "https://storage.googleapis.com/info_450/IndividualAssistanceHousingRegistrantsLargeDisasters%20(1).csv"
)


st.subheader("Data Preview")
st.write(df.head())

st.subheader("Histogram of Repair Amount")
fig_hist = px.histogram(
    df,
    x="repairAmount",
    nbins=30,
    title="Distribution of Repair Amounts"
)
st.plotly_chart(fig_hist)

st.subheader("Boxplot: Repair Amount by TSA Eligibility")
fig_box = px.box(
    df,
    x="tsaEligible",
    y="repairAmount",
    title="Repair Amount by TSA Eligibility",
    labels={
        "tsaEligible": "TSA Eligible (1 = Yes, 0 = No)",
        "repairAmount": "Repair Amount"
    }
)
st.plotly_chart(fig_box)
