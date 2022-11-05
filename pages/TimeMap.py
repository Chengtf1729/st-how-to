import streamlit as st
from streamlit_option_menu import option_menu
from apps import timelineX
 

selected = option_menu (None,["Timeline", "Folium","Play Video"],
    icons=["newspaper", "book", "envelope"],
    default_index=0,
    orientation="horizontal",
)

if selected == "Timeline":
    timelineX.Montage()

if selected == "Folium":
    timelineX.Folium()

if selected == "Play Video":
    timelineX.Video()
    
    


