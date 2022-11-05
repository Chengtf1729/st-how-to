import streamlit as st
from streamlit_agraph import agraph, Node, Edge, Config
from PIL import Image
import base64


def svg_img(image_file):
       svg = "data:image/png+xml;base64,"
       with open(image_file, "rb") as img_file:
              svg = svg + base64.b64encode(img_file.read()).decode('UTF-8') 
              return svg

def Network():
       nodes = []
       edges = []

       svg = svg_img("./img/IDD.png")
       nodes.append(Node(id="IDD", size=400, svg=svg))

       svg = svg_img("./img/A00_Why.png")
       nodes.append( Node(id="What is IDD", size=400, svg=svg))
# edges
       edges.append(Edge(source="IDD", label="", target="What is IDD", type="CURVE_SMOOTH")) 

       config = Config(width=1200, height=900, directed=True,nodeHighlightBehavior=True, 
                highlightColor="#F7A7A6", collapsible=True,
                node={'labelProperty':'label'},
                link={'labelProperty': 'label', 'renderLabel': True}
                ) 

       return_value = agraph(nodes=nodes, edges=edges, config=config)


