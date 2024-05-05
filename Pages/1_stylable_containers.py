import streamlit as st
from streamlit_extras.stylable_container import stylable_container


#defining the stylable containers
#everything will be labelled in hexidecimal, I will also provide an example in all rgba
def simple_container(varheader_s, varbody_s, vartext_s):
    with stylable_container(
        css_style= """
        {
            background-color: #3F9EED; /* Sets the background color to a shade of blue (#3F9EED) */
            color: #3FED43; /* Sets the text color to a shade of green (#3FED43) */
            border-radius: 15px; /* Rounds the corners of the element with a 15-pixel radius */
            padding: 15px; /* Adds 15 pixels of inner spacing between the content and the border */
            margin: 10px; /* Adds 10 pixels of outer spacing between this element and other elements */
            border: 2px solid #ccc; /* Creates a 2-pixel solid border with a light gray color (#ccc) */
            box-shadow: 2px 2px 6px rgba(0, 0, 0, 0.1); /* Applies a shadow 2 pixels to the right and bottom with a blur radius of 6 pixels and a light opacity */
            font-family: 'Arial', sans-serif; /* Sets the font to Arial with a fallback to any available sans-serif font */
            font-size: 14px; /* Sets the font size to 14 pixels */
            transition: background-color 0.3s ease, box-shadow 0.3s ease; /* Smoothly animates changes to the background color and box-shadow properties over 0.3 seconds */
        }
        """,
    ):
        st.header(varheader_s)
        st.markdown(varbody_s)
        st.text(vartext_s)

#this container will include columns and contaiiners within it, hang onto your seats
def complex_container(varheader_c, varbody_c, vartext_c):
    with stylable_container(
        css_style= """
        {
            background-color: #3F9EED; /* Sets the background color to a shade of blue (#3F9EED) */
            color: #3FED43; /* Sets the text color to a shade of green (#3FED43) */
            border-radius: 15px; /* Rounds the corners of the element with a 15-pixel radius */
            padding: 15px; /* Adds 15 pixels of inner spacing between the content and the border */
            margin: 10px; /* Adds 10 pixels of outer spacing between this element and other elements */
            border: 2px solid #ccc; /* Creates a 2-pixel solid border with a light gray color (#ccc) */
            box-shadow: 2px 2px 6px rgba(0, 0, 0, 0.1); /* Applies a shadow 2 pixels to the right and bottom with a blur radius of 6 pixels and a light opacity */
            font-family: 'Arial', sans-serif; /* Sets the font to Arial with a fallback to any available sans-serif font */
            font-size: 14px; /* Sets the font size to 14 pixels */
            transition: background-color 0.3s ease, box-shadow 0.3s ease; /* Smoothly animates changes to the background color and box-shadow properties over 0.3 seconds */
        }
        """,
    ):
        st.header(varheader_c)
        st.markdown(varbody_c)
        st.text(vartext_c)

