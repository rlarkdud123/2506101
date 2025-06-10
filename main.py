import streamlit as st
st.title("첫 app")
st.write("hello")
name=st.text_input("이름 입력")
if name:
  if name=="김가영":
    st.successs("반갑습니다. 김가영님!")
  else:
    st.warning("누구세요?")
