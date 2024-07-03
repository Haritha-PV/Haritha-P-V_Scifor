import streamlit as st

# set the title of the app
st.header('STREAMLIT',divider='rainbow')
st.subheader('_Streamlit_ is :blue[cool] :sunglasses:')
st.title('My :red[Streamlit] App')

# Display an image with a caption
st.image("coding.jpg", caption="deploying", width=800)

# Display a reset button
st.button("Reset", type="primary")
if st.button("Say hello"):
    st.write("Have a nice day!")
else:
    st.write(':smile:')

# Link button to the documentation
st.link_button("Documentation", "https://docs.streamlit.io/")