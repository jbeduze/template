import streamlit as st

# Initialize the session state for the CSS
if 'site_css' not in st.session_state:
    with open("config/style.css") as css:
        st.session_state['site_css'] = css.read()


# Apply the CSS site-wide
st.markdown(f'<style>{st.session_state["site_css"]}</style>', unsafe_allow_html=True)

st.title("This is my title")

st.header('this is my header')

st.subheader("this is my subtitle")

st.write('This is my text "st.write"')

st.markdown('This is my "st.markdown"')

st.text('This is my "st.text"')