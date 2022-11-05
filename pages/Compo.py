import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
from apps import st_forms
 

selected = option_menu (None,["Forms", "Select Box","TreeMap", "Circlify"],
    icons=["newspaper", "book", "envelope", "clipboard-data"],
    default_index=0,
    orientation="horizontal",
)

if selected == "Forms":
    st_forms.appForm()

if selected == "Select Box":
    st_forms.appSelectBox()
