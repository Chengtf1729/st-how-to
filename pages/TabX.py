import streamlit as st
import numpy as np

tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with tab2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
    

tabA, tabB = st.tabs(["📈 Chart", "🗃 Data"])
data = np.random.randn(10, 1)

tabA.subheader("A tab with a chart")
tabA.line_chart(data)

tabB.subheader("A tab with the data")
tabB.write(data)
