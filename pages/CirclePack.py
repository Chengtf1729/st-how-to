import streamlit as st
from streamlit_option_menu import option_menu
from apps import circlifyX
 

selected = option_menu (None,["Bubble", "Circle Pack"],
    icons=["newspaper", "book"],
    default_index=0,
    orientation="horizontal",
)

if selected == "Bubble":
    circlifyX.Bubble()

if selected == "Circle Pack":
    circlifyX.CirclePack()
    


