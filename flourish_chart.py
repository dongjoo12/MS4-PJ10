import streamlit as st

def exchange_main():
    # Define the URL
    url = "https://public.flourish.studio/visualisation/18828305/"

    # Use the components.v1.html function to display the webpage
    st.components.v1.html(
        f'<iframe src="{url}" width="100%" height="600" style="border:none;"></iframe>',
        height=600
    )

if __name__ == '__main__':
    exchange_main()