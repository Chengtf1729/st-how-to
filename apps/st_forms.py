import streamlit as st

def appForm():
    st.subheader("Form")
    with st.form("my_form"):
        text1 = st.text_input("Text 1", "")
        text2 = st.text_input("Text 2", "")
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.write(text1, text2)

def appSelectBox():
    st.subheader("Single Select")
    option = st.selectbox("Choose options",
        ('Email', 'Phone', 'SMS'))
    st.write('You have selected', option)

    st.subheader("Mutiselect")
    options = st.multiselect("Options",
    ['Green', 'Yellow', 'Blue', 'Red'])
    st.write("You have selected", options)

    if 'Yellow' in options:
        st.subheader("OK")

