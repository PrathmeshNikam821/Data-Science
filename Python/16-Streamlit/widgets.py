import streamlit as st

st.title("Stramlit text input ")
name=st.text_input("Enter your name ")

if name:
  st.write(f"Hello {name}")
  
age=st.slider("Enter your age ",0,100,25)

st.write(f"your age is {age}")

options = ['Python ' , 'java' , 'c++']

choice = st.selectbox("Choose your favourite laguage", options)
st.write(f"You have selected {choice}")
