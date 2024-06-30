#weekly test(28-06-2024)
import streamlit as st

# Set the title of the app
st.title('My :green[Streamlit] App')

# Button
if st.button("Click Me!"):
    st.write("Choose your lucky number!")

# Slider
slider_value = st.slider("Select a number", 0, 100, 50)
st.write(f"Your lucky number: {slider_value}")

# Display an image with a caption
st.image("images.png", caption="STREAMLIT", width=500)
