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
import streamlit_caculater
import needed_people
import App_image
import delivery

st.set_page_config(layout="wide")

# st.sidebar.header('home')
main_button = st.sidebar.button('🏡', key='main_button')

st.sidebar.header('목차')

texts = ['📉분석', '💡제안', '🎉결론']
options = ['🌏미래 탄소 배출량 예측', '⚡발전 유형별 전력 용량 추세', '🏭산업별 탄소 배출량 예측', '🚗자동차의 연간 전력 소비량 예측']
options2 = ['🚌자동차 vs 버스 배출량 비교', '💳기후동행카드 vs 자동차 이용', '👨‍👩‍👧필요한 이용객 수', '🚚배송업 탄소 배출량 비교', '🧮탄소 배출량 계산기']
options3 = ['🌳목표', '📱구현 어플 이미지']

if 'button_clicked' not in st.session_state:
    st.session_state.button_clicked = False
if 'selected_text' not in st.session_state:
    st.session_state.selected_text = None

for i, text in enumerate(texts):
    if st.sidebar.button(text, key=f'button_{i}'):
        st.session_state.button_clicked = True
        st.session_state.selected_text = text

if main_button:
    st.session_state.button_clicked = False
    st.session_state.selected_text = None

if st.session_state.button_clicked:
    if st.session_state.selected_text == '📉분석':
        menu = st.sidebar.selectbox('메뉴 선택', options, index=0, key='select_1')
        # st.write('선택한 메뉴', menu)

        if menu == '🌏미래 탄소 배출량 예측':
            st.subheader('🌏미래 탄소 배출량 예측')
            Predict_annual_carbon_emissions.exchange_main()

        elif menu == '⚡발전 유형별 전력 용량 추세':
            st.subheader('⚡발전 유형별 전력 용량 추세')
            Power_Capacity_trends_by_Type.exchange_main()

        elif menu == '🏭산업별 탄소 배출량 예측':
            st.subheader('🏭산업별 탄소 배출량 예측')
            Industry_predict_emission.exchange_main()
        
        elif menu == '🚗자동차의 연간 전력 소비량 예측':
            st.subheader('🚗자동차의 연간 전력 소비량 예측')
            pred_consumption_of_cars.exchange_main()

    # elif st.session_state.selected_text == '본론':
    #     menu = st.sidebar.selectbox('메뉴 선택', options2, index=0, key='select_2')
    #     st.write('선택한 메뉴', menu)

    #     elif menu == '🌏미래 탄소 배출량 예측(2018-2030)':
    #         st.subheader('🌏탄소 배출량 예측(2018-2030)')
    #         Predict_annual_carbon_emissions.exchange_main()

    elif st.session_state.selected_text == '💡제안':
        menu = st.sidebar.selectbox('메뉴 선택', options2, index=0, key='select_2')
        # st.write('선택한 메뉴', menu)

        if menu == '🚌자동차 vs 버스 배출량 비교':
            st.subheader('🚌자동차 vs 버스 배출량 비교')
            bus_car_st.exchange_main()

        elif menu == '💳기후동행카드 vs 자동차 이용':
            st.subheader('💳기후동행카드 vs 자동차 이용')
            Card_vs_Car.exchange_main()

        elif menu == '👨‍👩‍👧필요한 이용객 수':
            st.subheader('👨‍👩‍👧필요한 이용객 수')
            needed_people.exchange_main()

        elif menu == '🚚배송업 탄소 배출량 비교':
            st.subheader('🚚배송업 탄소 배출량 비교')
            delivery.exchange_main()

        elif menu == '🧮탄소 배출량 계산기':
            st.subheader('🧮탄소 배출량 계산기')
            streamlit_caculater.exchange_main()

    elif st.session_state.selected_text == '🎉결론':
        menu = st.sidebar.selectbox('메뉴 선택', options3, index=0, key='select_3')
        # st.write('선택한 메뉴', menu)

        if menu == '🌳목표':
            st.subheader('🌳목표')
            flourish_chart.exchange_main()

        elif menu == '📱구현 어플 이미지':
            st.subheader('📱구현 어플 이미지')
            App_image.exchange_main()

if not st.session_state.button_clicked or main_button:
    st.title("ㅈㄹㅌㅅ(제로탄소)")

    st.subheader('팀원')

    st.dataframe({'반': ['14반 12번', '14반 15번', '15반 06번', '15반 28번', '15반 31번'], '이름': ['박혜인', '신동주', '김신실', '장예연', '허인석']})

    st.write('-------------------------------------------------------------------')

    st.header("🏖️제로탄소의 여정")

    markdown1 = """
    1. 이산화탄소 배출량을 예측한다.
    2. 이산화탄소를 줄일 수 있는지 확인해본다.
    3. 이산화탄소를 현실적으로 줄일 수 없음을 확인하고 제안한다.
    4. 제안이 성공적으로 실행 되었을 때의 효과를 보여준다.
    """

    st.markdown(markdown1)

    st.write('-------------------------------------------------------------------')

    st.header('전 세계 이산화 탄소 배출량 지도')
    img = 'world-emissions-co2_2023.png'
    st.image(img)

markdown2 = """탄소 줄이기, 우리 모두의 챌린지!"""

st.sidebar.title("구호")
st.sidebar.info(markdown2)
logo = "https://img.etnews.com/photonews/2104/1399265_20210404153632_843_0001.jpg"
st.sidebar.image(logo)