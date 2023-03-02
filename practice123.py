# Importing Liberaries

# Yahoo! Finance API
# Open-source tool that uses Yahoo's publicly available APIs, and is intended for research and educational purposes
import yfinance as yf

# Streamlit for web-page
import streamlit as st
import pandas as pd

# Base64 for changing format of image
import base64

# Creating a function to make a pic as background
def addImg(image_file):
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
addImg('istockphoto-1153657433-612x612.jpg')    

# Setting Header and Welcome message
st.title(":blue[Welcome To _Stock_ _Price_ App]\n")
st.header(":green[See the complete visualization of] :green[_Companies_ _Stocks_]")

# Getting user namet
name = st.text_input(":red[Q : What name do you go by ?] :sunglasses: :").capitalize()

# Selecting button 
button1 = st.button("Click Here")

# Actions to happen after pressing button
if button1 :
    st.write(f"### :green[Hi _{name}_ , Hope you are doing] :blue[GREAT] :innocent:\n")
    st.write("### :green[Here you will be analyzing the stocks as per your requirement], :blue[to help you in _making_ _a_ _better_ _decisions_] :smile:")

# Getting input of company and date
company = st.text_input(":red[Q : Which companies stock do you want to see ?] :")
startingDate = st.date_input(":red[_Select_ _Starting_ _Date_ (YYYY-MM-DD)] : ")
endDate = st.date_input(":red[_Select_ _the_ _End_ _Date_ (YYYY-MM-DD)] : ")

# Using yfinance lib to get data using API
tickerSymbol = company.upper()
tickerData = yf.Ticker(tickerSymbol)
tickerDF = tickerData.history(period='1mo',start= startingDate,end= endDate)

st.header(f":white[Complete Stock Analysis of {tickerSymbol}]")
st.dataframe(tickerDF,use_container_width=True)

# Defining Columns for better view of 
col1, col2 = st.columns(2)
with col1:
    # Plotting graphs for the above information
    st.header(f"\n:blue[Closing Price of {tickerSymbol}]")
    st.line_chart(tickerDF.Close)

    st.header(f"\n:blue[Divident given by {tickerSymbol}]")
    st.bar_chart(tickerDF["Dividends"])
with col2:
    st.header(f"\n:blue[Closing Volume of {tickerSymbol}]")
    st.area_chart(tickerDF.Volume)

    st.header(f"\n:blue[Stock Split of {tickerSymbol}]")
    st.bar_chart(tickerDF["Stock Splits"])

