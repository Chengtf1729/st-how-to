import streamlit as st
from apps import hello

link = '[GitHub](/BarPlot)'
st.markdown(link, unsafe_allow_html=True)

hello.hello()

