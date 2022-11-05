import streamlit as st
from streamlit_option_menu import option_menu
from apps import barX
 

selected = option_menu (None,["Matplotlib", "Plotly Express","Plotly Go"],
    icons=["newspaper", "book", "envelope"],
    default_index=0,
    orientation="horizontal",
)

if selected == "Matplotlib":
    barX.Matplot()

if selected == "Plotly Express":
    barX.Expressplot()

if selected == "Plotly Go":
    barX.Goplot()
    


