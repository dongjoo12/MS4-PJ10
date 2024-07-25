import streamlit as st
from PIL import Image

def exchange_main():
    image = Image.open('image_28.png')

    st.image(image)

    image2 = Image.open('Ali.gif')

    st.image(image2)

    image3 = Image.open('calculate.png')

    st.image(image3)

if __name__ == '__main__':
    exchange_main()