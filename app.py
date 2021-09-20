import streamlit as st


from distributions import normal_distribution, fun_widgets, basics

with st.expander('Basics', expanded=False):
    basics()

st.title('Statistical distributions')

dist_selector = st.sidebar.selectbox(
    "Pick a distribution:",
    ("Beta", "Normal"),
    index=1
)

st.header(dist_selector)

if dist_selector == 'Normal':
    normal_distribution()


fun_widgets()