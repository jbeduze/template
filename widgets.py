import streamlit as st

def display_widgets():
    @st.experimental_dialog("Experimental Dialog Widget")
    def test_widget():
        st.write("Here's the test of the experimental dialog box. It's a decorator at this point where it has to exist above a function and activate when the function is called.")
        reason = st.text_input("Why are you testing this?", value=st.session_state.get("reason", ""))
        if st.button("Submit"):
            st.session_state.reason = reason
            st.experimental_rerun()

    if "show_dialog" not in st.session_state:
        st.session_state.show_dialog = False

    if st.button("Open experimental dialog"):
        st.session_state.show_dialog = True

    if st.session_state.show_dialog:
        test_widget()

    if "reason" in st.session_state:
        st.write(f"You tested the dialog because: {st.session_state.reason}")
