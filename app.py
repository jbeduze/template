import streamlit as st


#custom font site wide
with open( "config/style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

st.title("This is my title")

st.header('this is my header')

st.subheader("this is my subtitle")

st.write('This is my text "st.write"')

st.markdown('This is my "st.markdown"')

st.text('This is my "st.text"')