import bus_car_st
import pred_consumption_of_cars
import Population_of_Korea
import needed_people
import Power_Capacity_trends_by_Type
import Predict_annual_carbon_emissions
import flourish_chart
import streamlit as st
import matplotlib.pyplot as plt
import warnings
import pandas as pd
from scipy.interpolate import interp1d
from sklearn.linear_model import LinearRegression
import numpy as np
plt.rc('font', family='Malgun Gothic')
warnings.filterwarnings('ignore')


st.sidebar.header('login')
user_id = st.sidebar.text_input('input id', value='streamlit', max_chars=15)
user_password = st.sidebar.text_input('input password', value='', type='password')

if user_password == '1234':
    st.sidebar.header('Zero - Tanso List')
    opt_data = ['탄소 배출량 예측(2018-2030)', '자동차vs버스 배출량 비교', 'pred_consumption_of_cars', 'Population_of_Korea(2018-2030)', 'needed_people', 'Power_Capacity_trends_by_Type', 'flourish_chart']
    menu = st.sidebar.selectbox('select menu', opt_data, index=0)
    st.sidebar.write('selected menu:', menu)

    if menu == '탄소 배출량 예측(2018-2030)':
        st.subheader('탄소 배출량 예측(2018-2030)')
        Predict_annual_carbon_emissions.exchange_main()

    elif menu == '자동차vs버스 배출량 비교':
        st.subheader('버스 vs 자동차 비교')
        bus_car_st.exchange_main()

    elif menu == 'pred_consumption_of_cars':
        st.subheader('pred_consumption_of_cars')
        pred_consumption_of_cars.exchange_main()

    elif menu == 'Population_of_Korea(2018-2030)':
        st.subheader('Population_of_Korea(2018-2030)')
        Population_of_Korea.exchange_main()

    elif menu == 'needed_people':
        st.subheader('needed_people(2024-2030)')
        needed_people.exchange_main()
    
    elif menu == 'Power_Capacity_trends_by_Type':
        st.subheader('Power_Capacity_trends_by_Type')
        Power_Capacity_trends_by_Type.exchange_main()

    elif menu == 'flourish_chart':
        st.subheader('flourish_chart')
        flourish_chart.exchange_main()

    else:
        st.subheader('Zero - Tanso\'s result')