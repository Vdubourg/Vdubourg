import streamlit as st 
name= st.text_input ("您的名字")
st.write("哈樓"+ name)
input="Lapin"
list_possibilities=["兔子","女人","男人"] 
st.write("traduit lapin")
_correct_answer="兔子"
st.write("traduis"+input)
for i in range(len(list_possibilities)):
 st.button(list_possibilities[i])
import streamlit as st 
import pandas as pd 
voc=pd.read_cvc('https://docs.google.com/spreadsheets/d/e/2PACX-1vRRceq5Hbua-3E4NFGHWXcPNkFWPqIxaW1DqqQWbjuOP-dLhpx035VW6L8j3y6bxBlKwPN__RvILUSP/pub?output=csv')
st.dataframe(voc)
