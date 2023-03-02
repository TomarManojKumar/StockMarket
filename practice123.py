# Importing Liberaries
import yfinance as yf
import streamlit as st
import pandas as pd
import base64

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('istockphoto-1153657433-612x612.jpg')    

# Setting Header and Welcome message
st.title(":red[Welcome To _Stock_ _Price_ App]\n")
st.header(":green[See the complete visualization of] :green[_Company_ _Stocks_]")

# Getting user name
name = st.text_input(":red[Q : What name do you go by ?] :sunglasses: :").capitalize()
button1 = st.button("Click Here")

# Actions to happen after pressing button
if button1 :
    st.write(f"### :green[Hi _{name}_ , Hope you are doing] :blue[GREAT] :innocent:\n")
    st.write("### :green[Here you will be analyzing the stocks as per your requirement], :blue[to help you in _making_ _a_ _better_ _decisions_] :smile:")

# Getting input of company and date
company = st.text_input(":red[Q : Which companies stock do you want to see ?] :")
startingDate = st.date_input(":red[_Select_ _Starting_ _Date_ (YYYY-MM-DD)] : ")
endDate = st.date_input(":red[_Select_ _the_ _End_ _Date_ (YYYY-MM-DD)] : ")

# Using yfinance lib to get data
tickerSymbol = company.upper()
tickerData = yf.Ticker(tickerSymbol)
tickerDF = tickerData.history(period='1d',start= startingDate,end= endDate)

# Plotting graphs for the above information
st.header(f"\n:blue[Closing Price of {tickerSymbol}]")
st.line_chart(tickerDF.Close )
st.header(f"\n:blue[Closing Volume of {tickerSymbol}]")
st.line_chart(tickerDF.Volume)