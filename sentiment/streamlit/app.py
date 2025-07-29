import streamlit as st 
import django
import os

# os.environ.setdefault("DJANGO_SETTINGS_MODULE","settings.py")
# django.setup()

st.title("Sentiment Analysis")

st.subheader("Single User Analyze")
st.text("Enter the details of the user:")


reviewerID = st.text_input("Enter Reviewer ID")
reviewRating = st.number_input(min_value=1, max_value=5, step=1, label="Enter Reviewer Rating")
asin = st.text_input("Enter asin ID")
reviewrName = st.text_input("Enter Reviewer Name")
reviewTime = st.text_input("Enter Review Time")
reviewText = st.text_input("Enter Review Text")
st.markdown(
    ":orange-badge[⚠️ the reviewew has to be verified for getting the sentiment]"
)

submitSentiment = st.button("Submit")

if submitSentiment:
    data = []

