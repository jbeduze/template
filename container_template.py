import streamlit as st
from streamlit_extras.stylable_container import stylable_container
def display_container():
    def simple_container():
        with stylable_container(
            key="Simple_Container",
            css_styles="""
            {
            /*container qualities*/    
                box-shadow: 0px 0px 10px #3FED43; /* Applies a shadow 2 pixels to the right and bottom with a blur radius of 6 pixels and a light opacity */            font-family: 'Arial', sans-serif; /* Sets the font to Arial with a fallback to any available sans-serif font */         font-size: 20px; /* Sets the font size to 14 pixels */            transition: background-color 0.3s ease, box-shadow 0.3s ease; /* Smoothly animates changes to the background color and box-shadow properties over 0.3 seconds */
                border: 2px solid #ccc; /* Creates a 2-pixel solid border with a light gray color (#ccc) */
                border-radius: 15px; /* Rounds the corners of the element with a 15-pixel radius */
                background-color: #3F9EED; /* Sets the background color to a shade of blue (#3F9EED) */
            /*text qualities*/
                color: #3FED43; /* Sets the text color to a shade of green (#3FED43) */
                width:105%;
                padding: 15px; /* Adds 15 pixels of inner spacing between the content and the border */
                margin: 10px; /* Adds 10 pixels of outer spacing between this element and other elements */
            }
            """,
        ):
            st.markdown("this is the most basic way to utilize stylable_containers and shows all the different elements we can plug into the widget you set with it")
            
    simple_container()

    #This example combines variables with the
    def variable_container(varheader, varsubheader, varmarkdown, vartext):
        with stylable_container(
            key="variable_Container",
            css_styles="""
            {
                box-shadow: 3px 3px 10px #3FED43; /* Applies a shadow 2 pixels to the right and bottom with a blur radius of 6 pixels and a light opacity */            font-family: 'Arial', sans-serif; /* Sets the font to Arial with a fallback to any available sans-serif font */         font-size: 20px; /* Sets the font size to 14 pixels */            transition: background-color 0.3s ease, box-shadow 0.3s ease; /* Smoothly animates changes to the background color and box-shadow properties over 0.3 seconds */
                border: 2px solid #ccc; /* Creates a 2-pixel solid border with a light gray color (#ccc) */
                border-radius: 10px; /* Rounds the corners of the element with a 15-pixel radius */
                background-color: #3F9EED; /* Sets the background color to a shade of blue (#3F9EED) */
                color: #3FED43; /* Sets the text color to a shade of green (#3FED43) */            header-color: #3FED43;
                padding: 5px; /* Adds 15 pixels of inner spacing between the content and the border */
                margin: 8px;
            }
            """,
        ):
            #containers as the firsdt element act as sizing for the stylable container, you can then input columns to fill the containers with all kinds of content
            with st.container(height=200, border=False):
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.header(varheader)
                    st.subheader(varsubheader)
                    st.markdown(varmarkdown)
                    st.text(vartext)
                with col3:
                    title = st.text_input("Movie title", "Life of Brian")
                    st.write("The current movie title is", title)
                    st.button("Button")

    #display built out container and insert the verbiage for the variable elements
    variable_container(varheader="Header", varsubheader="subheader", varmarkdown="Markdown", vartext="text")




    #alright now let's try nesting containers
    def inner_container_1():
        with stylable_container(
            key="inner_Container",
            css_styles="""
            {
                box-shadow: 3px 3px 10px #3FED43; /* Applies a shadow 2 pixels to the right and bottom with a blur radius of 6 pixels and a light opacity */            font-family: 'Arial', sans-serif; /* Sets the font to Arial with a fallback to any available sans-serif font */         font-size: 20px; /* Sets the font size to 14 pixels */            transition: background-color 0.3s ease, box-shadow 0.3s ease; /* Smoothly animates changes to the background color and box-shadow properties over 0.3 seconds */
                border: 2px solid #ccc; /* Creates a 2-pixel solid border with a light gray color (#ccc) */
                border-radius: 10px; /* Rounds the corners of the element with a 15-pixel radius */
                background-color: #3F9EED; /* Sets the background color to a shade of blue (#3F9EED) */
                color: #3FED43; /* Sets the text color to a shade of green (#3FED43) */            header-color: #3FED43;
                padding: 5px; /* Adds 15 pixels of inner spacing between the content and the border */
                margin: 8px;
            }
            """,
        ):
            #containers as the first element act as sizing for the stylable container, you can then input columns to fill the containers with all kinds of content
            with st.container(height=200, border=False):
                st.markdown("content within inner/nested container")


    def holder_container():
        with stylable_container(
            key="holder_Container",
            css_styles="""
            {
                box-shadow: 3px 3px 10px #3FED43; /* Applies a shadow 2 pixels to the right and bottom with a blur radius of 6 pixels and a light opacity */            font-family: 'Arial', sans-serif; /* Sets the font to Arial with a fallback to any available sans-serif font */         font-size: 20px; /* Sets the font size to 14 pixels */            transition: background-color 0.3s ease, box-shadow 0.3s ease; /* Smoothly animates changes to the background color and box-shadow properties over 0.3 seconds */
                border: 2px solid #ccc; /* Creates a 2-pixel solid border with a light gray color (#ccc) */
                border-radius: 10px; /* Rounds the corners of the element with a 15-pixel radius */
                background-color: #3F9EED; /* Sets the background color to a shade of blue (#3F9EED) */
                color: #3FED43; /* Sets the text color to a shade of green (#3FED43) */            header-color: #3FED43;
                padding: 5px; /* Adds 15 pixels of inner spacing between the content and the border */
                margin: 8px;
            }
            """,
        ):
            #containers as the first element act as sizing for the stylable container, you can then input columns to fill the containers with all kinds of content
            with st.container(height=400, border=False):
                col1, col2 = st.columns([1,2])
                with col1:
                    inner_container_1()
                with col2:
                    st.text("content within the outer holder container")

    #displaying holder container
    holder_container()


    #setting up containers as classes

    css_styles = {
        "holder_soft_modern": """
            {
                box-shadow: 3px 3px 10px #274060;
                font-family: 'Arial', sans-serif;
                font-size: 20px;
                transition: background-color 0.3s ease, box-shadow 0.3s ease;
                border: 2px solid #ccc;
                border-radius: 10px;
                background-color: #274060;
                color: #FFFFFF;
                padding: 5px;
                margin: 8px;
            }
        """,
        "content_soft_modern": """
            {
                font-family: 'Arial', sans-serif;
                font-size: 20px;
                transition: background-color 0.3s ease;
                border: 2px solid #ccc;
                border-radius: 10px;
                background-color: #8AB6D6;
                color: #000000;
                padding: 5px;
                margin: 8px;
            }
        """,
        "holder_bold_vibrant": """
            {
                box-shadow: 3px 3px 10px #1B4D3E;
                font-family: 'Arial', sans-serif;
                font-size: 20px;
                transition: background-color 0.3s ease, box-shadow 0.3s ease;
                border: 2px solid #ccc;
                border-radius: 10px;
                background-color: #1B4D3E;
                color: #FFFFFF;
                padding: 5px;
                margin: 8px;
            }
        """,
        "content_bold_vibrant": """
            {
                font-family: 'Arial', sans-serif;
                font-size: 20px;
                transition: background-color 0.3s ease;
                border: 2px solid #ccc;
                border-radius: 10px;
                background-color: #66BB6A;
                color: #000000;
                padding: 5px;
                margin: 8px;
            }
        """
    }

