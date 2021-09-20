import streamlit as st

st.title('My first Streamlit app')

a = 12.34
st.write(a)


st.markdown(r'''Raw strings can be very useful: we can
- create
- bullet
- lists

and other Markdown things like horizontal lines

---
''')


st.markdown(r'''
$$
i\hbar\frac{\partial}{\partial t} \Psi(x,t) = \left [ - \frac{\hbar^2}{2m}\frac{\partial^2}{\partial x^2} + V(x,t)\right ] \Psi(x,t)
$$
''')


st.markdown(r'''
```c
int main() {
  return 0;
}
```
''')

if st.checkbox('Tick me to see'):
  st.write(42)


selection = st.selectbox('Choose an option', ["Nothing here", "or here", "but something here"])

if selection == "but something here":
  st.write("You found me!")
else:
  st.write("Try again")


float_val = st.slider("Pick a float", min_value=1.0, max_value=10.0, value=5.0, step=0.1, format="%.1f")
st.write(float_val)

st.sidebar.write("Adding text to the sidebar...")
