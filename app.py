import streamlit as st

st.write("Hello IK")
st.title("Our Title")
st.title("_Streamlit_ is :blue[cool] :sunglasses:")


prompt = st.chat_input("Ask Anything....")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")
