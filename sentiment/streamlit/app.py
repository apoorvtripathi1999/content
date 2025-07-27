import streamlit as st 
import django
import os

# os.environ.setdefault("DJANGO_SETTINGS_MODULE","settings.py")
# django.setup()

st.title("Sentiment Analysis")

st.subheader("Single User Analyze")
st.text("Enter the details of the user:")


reviewerID = st.text_input("Enter Reviewer ID")
asin = st.text_input("Enter asin ID")
reviewrName = st.text_input("Enter Reviewer Name")
reviewTime = st.text_input("Enter Review Time")
reviewText = st.text_input("Enter Review Text")

