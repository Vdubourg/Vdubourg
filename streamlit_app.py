import streamlit as st 
import pandas as pd 
voc=pd.read_cvc("https://docs.google.com/spreadsheets/d/e/2PACX-1vRRceq5Hbua-3E4NFGHWXcPNkFWPqIxaW1DqqQWbjuOP-dLhpx035VW6L8j3y6bxBlKwPN__RvILUSP/pub?output=csv")
st.dataframe(voc)
