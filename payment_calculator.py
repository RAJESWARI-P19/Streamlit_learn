import streamlit as st

st.title('Enter your name')

name=st.text_input('First Name')

name2=st.text_input('Last Name')

st.write('Your name is:',name + ' '+ name2)

