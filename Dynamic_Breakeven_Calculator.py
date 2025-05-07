
import streamlit as st
import pandas as pd

st.title('Dynamic Breakeven Calculator')

# Monthly Breakeven Calculator
st.header('Monthly Breakeven Calculator')
monthly_cost = st.number_input('Enter Monthly Operating Cost (EGP)', value=250000)
session_price = st.number_input('Enter Price per Session (EGP)', value=4000)

if st.button('Calculate Monthly Breakeven'):
    breakeven_sessions = monthly_cost / session_price
    daily_sessions = breakeven_sessions / 30
    st.write('### Monthly Breakeven Sessions:', breakeven_sessions)
    st.write('### Daily Sessions Needed:', daily_sessions)

# Capital Breakeven Calculator
st.header('Capital Breakeven Calculator')
capital_cost = st.number_input('Enter Capital Investment (EGP)', value=3500000)

if st.button('Calculate Capital Breakeven'):
    if breakeven_sessions > 0:
        capital_breakeven = capital_cost / (session_price * breakeven_sessions)
        st.write('### Capital Breakeven (Months):', capital_breakeven)
    else:
        st.write('Please calculate the Monthly Breakeven first.')

st.write("Developed by your assistant for instant breakeven analysis.")
