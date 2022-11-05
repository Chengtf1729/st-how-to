import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
from apps import agraphX
 

selected = option_menu (None,["Agraph", "Select Box","TreeMap", "Circlify"],
    icons=["newspaper", "book", "envelope", "clipboard-data"],
    default_index=0,
    orientation="horizontal",
)

if selected == "Agraph":
    agraphX.Network()


