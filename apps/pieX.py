import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
 
  
def Matplot():
    data = {'C':20, 'C++':15, 'Java':30,
        'Python':35}
    courses = list(data.keys())
    values = list(data.values())
  
    fig = plt.figure(figsize = (10, 5))
 
# creating the bar plot
    plt.bar(courses, values, color ='maroon',
        width = 0.4)
 
    plt.xlabel("Courses offered")
    plt.ylabel("No. of students enrolled")
    plt.title("Students enrolled in different courses")

    st.write(fig)

    fig = plt.figure(figsize = (10, 5))
 
# creating the bar plot
    plt.barh(courses, values, color ='maroon')
 
    plt.xlabel("Courses offered")
    plt.ylabel("No. of students enrolled")
    plt.title("Students enrolled in different courses")

    st.pyplot(fig)

# multiple bar chart
    st.subheader("Multiple Bar Chart")
    # set width of bar
    barWidth = 0.25
    fig = plt.figure(figsize = (10, 5))
 
# set height of bar
    IT = [12, 30, 1, 8, 22]
    ECE = [28, 6, 16, 5, 10]
    CSE = [29, 3, 24, 25, 17]
 
# Set position of bar on X axis
    br1 = np.arange(len(IT))
    br2 = [x + barWidth for x in br1]
    br3 = [x + barWidth for x in br2]
 
# Make the plot
    plt.bar(br1, IT, color ='r', width = barWidth,
        edgecolor ='grey', label ='IT')
    plt.bar(br2, ECE, color ='g', width = barWidth,
        edgecolor ='grey', label ='ECE')
    plt.bar(br3, CSE, color ='b', width = barWidth,
        edgecolor ='grey', label ='CSE')
 
# Adding Xticks
    plt.xlabel('Branch', fontweight ='bold', fontsize = 15)
    plt.ylabel('Students passed', fontweight ='bold', fontsize = 15)
    plt.xticks([r + barWidth for r in range(len(IT))],
        ['2015', '2016', '2017', '2018', '2019'])
 
    plt.legend()
    st.pyplot(fig)

# stacked bar
    st.subheader("Stacked Bar")
    fig = plt.figure(figsize = (10, 5))
    x = ['A', 'B', 'C', 'D']
    y1 = [10, 20, 10, 30]
    y2 = [20, 25, 15, 25]
  
# plot bars in stack manner
    plt.bar(x, y1, color='r')
    plt.bar(x, y2, bottom=y1, color='b')
    st.pyplot(fig)

# using dataframe
    # create data

    fig = plt.figure(figsize = (10, 5))
    ax = fig.add_subplot(111)
    df = pd.DataFrame([['A', 10, 20, 10, 26], ['B', 20, 25, 15, 21], ['C', 12, 15, 19, 6],
                   ['D', 10, 18, 11, 19]],
                  columns=['Team', 'Round 1', 'Round 2', 'Round 3', 'Round 4'])

    df.plot(x='Team', kind='bar', stacked=True,ax = ax,
        title='Stacked Bar Graph by dataframe')

    st.pyplot(fig)

def Expressplot():
    
    data_canada = px.data.gapminder().query("country == 'Canada'")
    fig = px.bar(data_canada, x='year', y='pop')
    st.write(fig)

    st.subheader("Long format")
    long_df = px.data.medals_long()
    fig = px.bar(long_df, x="nation", y="count", color="medal", title="Long-Form Input")
    st.dataframe(long_df)
    st.write(fig)

    st.subheader("Wide format")
    wide_df = px.data.medals_wide()
    fig = px.bar(wide_df, x="nation", y=["gold", "silver", "bronze"], title="Wide-Form Input", text_auto=True)
    st.dataframe(wide_df)
    st.write(fig)

    st.subheader("Colored Bar")
    df = px.data.gapminder().query("country == 'Canada'")
    fig = px.bar(df, x='year', y='pop',
             hover_data=['lifeExp', 'gdpPercap'], color='lifeExp',
             labels={'pop':'population of Canada'}, height=400)
    st.write(fig)

def Goplot():
    
    countries=['India', 'Australia', 'Japan', 'America', 'Russia']
    values = [4500, 2500, 1053, 500, 3200]

    go_fig = go.Figure()

    obj = go.Bar(x = countries, y = values)
    go_fig.add_trace(obj)

    st.write(go_fig)

    st.subheader("Grouped Bar")
    go_fig = go.Figure()
    obj = go.Bar(x = countries, y = values)
    go_fig.add_trace(obj)
    go_fig.add_trace(obj)

    st.write(go_fig)

    st.subheader("Stacked Bar")
    go_fig = go.Figure()
    obj = go.Bar(x = countries, y = values, text=values)

    go_fig.add_trace(obj)
    go_fig.add_trace(obj)

    go_fig.update_layout(barmode='stack') #Barmode value
    st.write(go_fig)
