import streamlit as st

st.title('Streamlit Example')

number = st.slider('Select a number', 1, 100, 50)
st.write('You selected:', number)

if st.button('Say Hello'):
    st.write('Hello, Streamlit!')