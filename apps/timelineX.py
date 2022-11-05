import streamlit as st
from streamlit_timeline import timeline
from streamlit_folium import st_folium
import folium
from folium.features import DivIcon

def Montage():

    with open('./data/example.json', "r") as f:
        data = f.read()

# render timeline
    timeline(data, height=800)

def Folium():
    # center on Liberty Bell, add marker
# Singapore1.3521° N, 103.8198°
    m = folium.Map(location=[-42.8826, 147.3257], zoom_start=7)

    html = """
        <h1>Title</h1>
        <a href='https://www1.bca.gov.sg'>Liberty</a>
        """

    iframe = folium.IFrame(html=html, width=500, height=300)
    popup = folium.Popup(iframe, max_width=1200)
    folium.Marker(
            [-41.4391, 147.1358], 
            popup='<a href="https://www.google.com" target="_blank">Launceston</a>', 
            tooltip="Launceston"
        ).add_to(m)

    folium.Marker(
            [-41.14, 148.3], 
            popup='<a href="https://www.google.com" target="_blank">Bay of Fires</a>', 
            tooltip="Bay of Fires"
        ).add_to(m)


    folium.Marker(
            [-41.0575, 144.6598], 
            popup='<a href="https://www.google.com" target="_blank">Edge of the World</a>', 
            tooltip="Edge of the World"
        ).add_to(m)


    folium.Marker(
            [-41.2538, 146.12], 
            popup='<a href="https://www.google.com" target="_blank">Maze Lavender Farm</a>', 
            tooltip="Maze Lavender Farm"
        ).add_to(m)

    
    folium.Marker(
            [-41.413179, 146.453119], 
            popup='<a href="https://www.google.com" target="_blank">Liffey Falls</a>',
#            icon=DivIcon(
#                icon_size=(50,20),
#                icon_anchor=(0,0),
#                html='<div style="font-size: 12pt">Liffey Falls</div>'
#                ) ,
            tooltip="Liffey Falls",
           
        ).add_to(m)


        # call to render Folium map in Streamlit
    st_data = st_folium(m, width = 725)

def Video():
    
    FILENAME = "./data/Media1.mp4"
    video_file = open(FILENAME, 'rb') #enter the filename with filepath

    video_bytes = video_file.read() #reading the file

    st.video(video_bytes) #displaying the video

#displaying a video by simply passing a Youtube link

    st.video("https://youtu.be/yVV_t_Tewvs")

