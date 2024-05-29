import streamlit as st
from streamlit_extras.stylable_container import stylable_container


# css styling using the stylable container:
# with stylable_container(
#     key="profile_picture_container",
#     css_styles="""
#     {
#         box-shadow: 3px 3px 10px #3FED43; /* Applies a shadow 2 pixels to the right and bottom with a blur radius of 6 pixels and a light opacity */            font-family: 'Arial', sans-serif; /* Sets the font to Arial with a fallback to any available sans-serif font */         font-size: 20px; /* Sets the font size to 14 pixels */            transition: background-color 0.3s ease, box-shadow 0.3s ease; /* Smoothly animates changes to the background color and box-shadow properties over 0.3 seconds */
#         border: 2px solid #ccc; /* Creates a 2-pixel solid border with a light gray color (#ccc) */
#         border-radius: 10px; /* Rounds the corners of the element with a 15-pixel radius */
#         background-color: #3F9EED; /* Sets the background color to a shade of blue (#3F9EED) */
#         color: #3FED43; /* Sets the text color to a shade of green (#3FED43) */            header-color: #3FED43;
#         padding: 5px; /* Adds 15 pixels of inner spacing between the content and the border */
#         margin: 8px;
#     }
#     """,
# ):
def display_nested_container():
    #let's define the containers 1st
    def profile_holder_container():
        with stylable_container(
            key="profile_holder_container",
            css_styles="""
            {
                box-shadow: 0px 0px 10px #3FED43; /* Applies a shadow 2 pixels to the right and bottom with a blur radius of 6 pixels and a light opacity */            font-family: 'Arial', sans-serif; /* Sets the font to Arial with a fallback to any available sans-serif font */         font-size: 20px; /* Sets the font size to 14 pixels */            transition: background-color 0.3s ease, box-shadow 0.3s ease; /* Smoothly animates changes to the background color and box-shadow properties over 0.3 seconds */
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
            with st.container(height=300, border=False):
                colph1a, colph2a, colph3a = st.columns([25,65,1])
                colph1b, colph2b = st.columns([98,1])
                with colph1a:
                        def profile_picture_container():
                            with stylable_container(
                                key="profile_picture_container",
                                css_styles="""
                                {
                                    border: 2px solid #ccc; /* Creates a 2-pixel solid border with a light gray color (#ccc) */
                                    border-radius: 5px; /* Rounds the corners of the element with a 15-pixel radius */
                                    background-color: #3F9EED; /* Sets the background color to a shade of blue (#3F9EED) */
                                    color: #3FED43; /* Sets the text color to a shade of green (#3FED43) */            header-color: #3FED43;
                                    padding: 5px; /* Adds 15 pixels of inner spacing between the content and the border */
                                    margin: 8px;
                                }
                                """,
                            ):
                                    with st.container(height=100, border=False):
                                        st.markdown("insert profile picture")          
                        profile_picture_container()
                with colph2a:
                    def profile_generalinfo_container():
                            with stylable_container(
                                key="profile_generalinfo_container",
                                css_styles="""
                                {
                                    border: 2px solid #ccc; /* Creates a 2-pixel solid border with a light gray color (#ccc) */
                                    border-radius: 5px; /* Rounds the corners of the element with a 15-pixel radius */
                                    background-color: #3F9EED; /* Sets the background color to a shade of blue (#3F9EED) */
                                    color: #3FED43; /* Sets the text color to a shade of green (#3FED43) */            header-color: #3FED43;
                                    padding: 5px; /* Adds 15 pixels of inner spacing between the content and the border */
                                    margin: 8px;
                                }
                                """,
                            ):
                                    with st.container(height=100, border=False):
                                        st.markdown("insert general profile info here")
                    profile_generalinfo_container()
                with colph1b:
                    def profile_notes_container():
                        with stylable_container(
                            key="profile_generalinfo_container",
                            css_styles="""
                            {
                                border: 2px solid #ccc; /* Creates a 2-pixel solid border with a light gray color (#ccc) */
                                border-radius: 5px; /* Rounds the corners of the element with a 15-pixel radius */
                                background-color: #3F9EED; /* Sets the background color to a shade of blue (#3F9EED) */
                                color: #3FED43; /* Sets the text color to a shade of green (#3FED43) */            header-color: #3FED43;
                                padding: 5px; /* Adds 15 pixels of inner spacing between the content and the border */
                                margin: 8px;
                            }
                            """,
                        ):
                            with st.container(height=120, border=False):
                                st.markdown("insert general profile notes such as injuries or other profile specific dynamic info here")
                    profile_notes_container()

    def stats_holder_container():
        with stylable_container(
            key="stats_holder_container",
            css_styles="""
            {
                box-shadow: 0px 0px 10px #3FED43; /* Applies a shadow 2 pixels to the right and bottom with a blur radius of 6 pixels and a light opacity */            font-family: 'Arial', sans-serif; /* Sets the font to Arial with a fallback to any available sans-serif font */         font-size: 20px; /* Sets the font size to 14 pixels */            transition: background-color 0.3s ease, box-shadow 0.3s ease; /* Smoothly animates changes to the background color and box-shadow properties over 0.3 seconds */
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
            with st.container(height=300, border=False):
                colsh1a, colsh2a, colsh3a = st.columns([40,50,1])
                colsh1b, colsh2b = st.columns([98,1])
                with colsh1a:
                        def stats_winloss_container():
                            with stylable_container(
                                key="stats_winloss_container",
                                css_styles="""
                                {
                                    border: 2px solid #ccc; /* Creates a 2-pixel solid border with a light gray color (#ccc) */
                                    border-radius: 5px; /* Rounds the corners of the element with a 15-pixel radius */
                                    background-color: #3F9EED; /* Sets the background color to a shade of blue (#3F9EED) */
                                    color: #3FED43; /* Sets the text color to a shade of green (#3FED43) */            header-color: #3FED43;
                                    padding: 5px; /* Adds 15 pixels of inner spacing between the content and the border */
                                    margin: 8px;
                                }
                                """,
                            ):
                                    with st.container(height=100, border=False):
                                        st.markdown("insert win/loss record here")          
                        stats_winloss_container()
                with colsh2a:
                    def stats_classmonitoring_container():
                            with stylable_container(
                                key="stats_classmonitoring_container",
                                css_styles="""
                                {
                                    border: 2px solid #ccc; /* Creates a 2-pixel solid border with a light gray color (#ccc) */
                                    border-radius: 5px; /* Rounds the corners of the element with a 15-pixel radius */
                                    background-color: #3F9EED; /* Sets the background color to a shade of blue (#3F9EED) */
                                    color: #3FED43; /* Sets the text color to a shade of green (#3FED43) */            header-color: #3FED43;
                                    padding: 5px; /* Adds 15 pixels of inner spacing between the content and the border */
                                    margin: 8px;
                                }
                                """,
                            ):
                                    with st.container(height=100, border=False):
                                        st.markdown("insert class and weight monitoring info here")
                    stats_classmonitoring_container()
                with colsh1b:
                    def stats_notes_container():
                        with stylable_container(
                            key="stats_notes_container",
                            css_styles="""
                            {
                                border: 2px solid #ccc; /* Creates a 2-pixel solid border with a light gray color (#ccc) */
                                border-radius: 5px; /* Rounds the corners of the element with a 15-pixel radius */
                                background-color: #3F9EED; /* Sets the background color to a shade of blue (#3F9EED) */
                                color: #3FED43; /* Sets the text color to a shade of green (#3FED43) */            header-color: #3FED43;
                                padding: 5px; /* Adds 15 pixels of inner spacing between the content and the border */
                                margin: 8px;
                            }
                            """,
                        ):
                            with st.container(height=120, border=False):
                                st.markdown("insert general improvement/focuses notes such as injuries or other profile specific dynamic info here")
                    stats_notes_container()

    def coach_holder_container():
        with stylable_container(
            key="coach_holder_container",
            css_styles="""
            {
                box-shadow: 0px 0px 10px #3FED43; /* Applies a shadow 2 pixels to the right and bottom with a blur radius of 6 pixels and a light opacity */            font-family: 'Arial', sans-serif; /* Sets the font to Arial with a fallback to any available sans-serif font */         font-size: 20px; /* Sets the font size to 14 pixels */            transition: background-color 0.3s ease, box-shadow 0.3s ease; /* Smoothly animates changes to the background color and box-shadow properties over 0.3 seconds */
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
            with st.container(height=235, border=False):
                colch1a, colch1b = st.columns([100,1])
                colch2a, colch2b = st.columns([100,1])
                with colch1a:
                    def coach_notes_container():
                        with stylable_container(
                            key="coach_notes_container",
                            css_styles="""
                            {
                                border: 2px solid #ccc; /* Creates a 2-pixel solid border with a light gray color (#ccc) */
                                border-radius: 5px; /* Rounds the corners of the element with a 15-pixel radius */
                                background-color: #3F9EED; /* Sets the background color to a shade of blue (#3F9EED) */
                                color: #3FED43; /* Sets the text color to a shade of green (#3FED43) */            header-color: #3FED43;
                                padding: 5px; /* Adds 15 pixels of inner spacing between the content and the border */
                                margin: 8px;
                            }
                            """,
                        ):
                                with st.container(height=80, border=False):
                                    st.markdown("insert coach notes/comments/recommendations")          
                    coach_notes_container()
                with colch2a:
                    def ai_notes_container():
                        with stylable_container(
                            key="ai_notes_container",
                            css_styles="""
                            {
                                border: 2px solid #ccc; /* Creates a 2-pixel solid border with a light gray color (#ccc) */
                                border-radius: 5px; /* Rounds the corners of the element with a 15-pixel radius */
                                background-color: #3F9EED; /* Sets the background color to a shade of blue (#3F9EED) */
                                color: #3FED43; /* Sets the text color to a shade of green (#3FED43) */            header-color: #3FED43;
                                padding: 5px; /* Adds 15 pixels of inner spacing between the content and the border */
                                margin: 8px;
                            }
                            """,
                        ):
                            with st.container(height=75, border=False):
                                st.markdown("insert AI notes/comments/recommendations")
                    ai_notes_container()

    def practice_holder_container():
        with stylable_container(
            key="practice_holder_container",
            css_styles="""
            {
                box-shadow: 0px 0px 10px #3FED43; /* Applies a shadow 2 pixels to the right and bottom with a blur radius of 6 pixels and a light opacity */            font-family: 'Arial', sans-serif; /* Sets the font to Arial with a fallback to any available sans-serif font */         font-size: 20px; /* Sets the font size to 14 pixels */            transition: background-color 0.3s ease, box-shadow 0.3s ease; /* Smoothly animates changes to the background color and box-shadow properties over 0.3 seconds */
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
            with st.container(height=235, border=False):
                st.markdown("practice details")

    def progress_holder_container():
        with stylable_container(
            key="progress_holder_container",
            css_styles="""
            {
                box-shadow: 0px 0px 10px #3FED43; /* Applies a shadow 2 pixels to the right and bottom with a blur radius of 6 pixels and a light opacity */            font-family: 'Arial', sans-serif; /* Sets the font to Arial with a fallback to any available sans-serif font */         font-size: 20px; /* Sets the font size to 14 pixels */            transition: background-color 0.3s ease, box-shadow 0.3s ease; /* Smoothly animates changes to the background color and box-shadow properties over 0.3 seconds */
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
            with st.container(height=235, border=False):
                st.markdown("workout and nutrition details")
    #i want to throw these in there to see what is the height I can get away with without having a scroll on the side for the whole page

    #top half "row"
    col1a, col2a = st.columns([30,50])
    col1b, col2b, col3b, col4b = st.columns([50,20,1,20])

    with col1a:
        profile_holder_container()
    with col2a:
        stats_holder_container()
    with col1b:
        coach_holder_container()
    with col2b:
        practice_holder_container()
    with col4b:
        progress_holder_container()
    "---"
    st.write("above is all of the container and column code all in one block- no calling form other pages, just all here")
    "---"