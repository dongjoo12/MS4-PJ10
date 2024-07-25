import streamlit as st
from termcolor import colored
import pandas as pd
import pygwalker as pyg

# import py-file list
import bus_car_st
import pred_consumption_of_cars
import Population_of_Korea
import Industry_predict_emission
import Power_Capacity_trends_by_Type
import Predict_annual_carbon_emissions
import flourish_chart
import Card_vs_Car


st.set_page_config(layout="wide")

st.sidebar.header('home')
main_button = st.sidebar.button('🏡main', key='main_button')

st.sidebar.header('목차')

texts = ['⚡Power_Capacity_trends_by_Type', '🏭산업별 탄소 배출량 예측', '🚗자동차의 연간 전력 소비량 예측', '🌏미래 탄소 배출량 예측(2018-2030)', '👨‍👩‍👧Population_of_Korea(2018-2030)', '🚌자동차 vs 버스 배출량 비교', '🎫기후동행카드 vs 자동차 이용', '🌳목표', '🧮탄소 배출량 계산기']

button_clicked = False

for i, text in enumerate(texts):
    if st.sidebar.button(text, key=f'button_{i}'):  # Add a unique key for each button
        button_clicked = True

        # if text == '⚡Power_Capacity_trends_by_Type':
        #     st.subheader('Power_Capacity_trends_by_Type')
        #     Power_Capacity_trends_by_Type.exchange_main()

        if text == '🏭산업별 탄소 배출량 예측':
            st.subheader('Industry_predict_emission')
            Industry_predict_emission.exchange_main()
        
        elif text == '🚗자동차의 연간 전력 소비량 예측':
            st.subheader('pred_consumption_of_cars')
            pred_consumption_of_cars.exchange_main()

        elif text == '🌏미래 탄소 배출량 예측(2018-2030)':
            st.subheader('탄소 배출량 예측(2018-2030)')
            Predict_annual_carbon_emissions.exchange_main()

        # elif text == '👨‍👩‍👧Population_of_Korea(2018-2030)':
        #     st.subheader('Population_of_Korea(2018-2030)')
        #     Population_of_Korea.exchange_main()
        
        elif text == '🚌자동차 vs 버스 배출량 비교':
            st.subheader('버스 vs 자동차 비교')
            bus_car_st.exchange_main()

        elif text == '🎫기후동행카드 vs 자동차 이용':
            st.subheader('Card_vs_Car')
            Card_vs_Car.exchange_main()

        elif text == '🌳목표':
            st.subheader('flourish_chart')
            flourish_chart.exchange_main()

        elif text == '🧮탄소 배출량 계산기':
            st.subheader('탄소 배출량 계산기')


if not button_clicked or main_button:
    st.title("ㅈㄹㅌㅅ(제로탄소)")

    # : 14반 12번 박혜인, 14반 15번 신동주, 15반 06번 김신실, 15반 28번 장예연, 15반 31번 허인석
    st.subheader("""팀원""")

    st.dataframe({'반': ['14반 12번', '14반 15번', '15반 06번', '15반 28번', '15반 31번'], '이름': ['박혜인', '신동주', '김신실', '장예연', '허인석']})

    st.write('-------------------------------------------------------------------')

    st.header("🏖️프로젝트의 여정")

    markdown1 = """
    1. 이산화탄소 배출량을 예측한다.
    2. 이산화탄소를 줄일 수 있는지 확인해본다.
    3. 이산화탄소를 현실적으로 줄일 수 없음을 확인하고 제안한다.
    4. 제안이 성공적으로 실행 되었을 때의 효과를 보여준다.
    """

    st.markdown(markdown1)

    st.write('-------------------------------------------------------------------')

    st.header('누가 더 많이 배출할까?')
    img = 'world-emissions-co2_2023.png'
    st.image(img)

markdown2 = """
탄소 줄이기, 우리 모두의 챌린지!
"""

st.sidebar.title("About")
st.sidebar.info(markdown2)
logo = "https://img.etnews.com/photonews/2104/1399265_20210404153632_843_0001.jpg"
st.sidebar.image(logo)
