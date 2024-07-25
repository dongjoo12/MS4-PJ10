import streamlit as st
from PIL import Image

def exchange_main():
    image = Image.open('CLaire.png')

    st.image(image)

if __name__ == '__main__':
    exchange_main()