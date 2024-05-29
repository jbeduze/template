import streamlit as st
from nested_container_template import display_nested_container
from container_template import display_container

st.set_page_config(
    page_title="Template App",
    page_icon="None",
    layout="wide",
    
)

# Initialize the session state for the CSS
if 'site_css' not in st.session_state:
    with open("config/style.css") as css:
        st.session_state['site_css'] = css.read()

tab1, tab2, tab3 = st.tabs(["Main", "customizing", "Containers"])

with tab1:
    # Apply the CSS site-wide
    st.markdown(f'<style>{st.session_state["site_css"]}</style>', unsafe_allow_html=True)

    st.title("This is my title")

    st.header('this is my header')

    st.subheader("this is my subtitle")

    st.write('This is my text "st.write"')

    st.markdown('This is my "st.markdown"')

    st.text('This is my "st.text"')

with tab3:
    with st.expander("See example of a dashboard with nested containers"):
        display_nested_container()
    with st.expander ("See example of how to use the stylable containers as a part of streamlit_extras", expanded=True):
        display_container()