import numpy as np
import streamlit as st

def fun_widgets():
    with st.expander('Widgets'):
        st.button('Hit me')
        st.checkbox('Check me out')
        st.radio('Radio', [1,2,3])
        st.selectbox('Select', [1,2,3])
        st.multiselect('Multiselect', [1,2,3])
        st.slider('Slide me', min_value=0, max_value=10)
        st.select_slider('Slide to select', options=[1,'2'])
        st.text_input('Enter some text')
        st.number_input('Enter a number')
        st.text_area('Area for textual entry')
        st.date_input('Date input')
        st.time_input('Time entry')
        st.file_uploader('File uploader')
        st.color_picker('Pick a color')


    with st.container():
        st.write("This is inside the container")
        # You can call any Streamlit command, including custom components:
        st.bar_chart(np.random.randn(50, 3))
        
    st.write("This is outside the container")


    col1, col2 = st.columns(2)
    col1.subheader('Columnisation')
    col1.text('Column here')
    col2.text('More here')


    st.balloons()