import streamlit as st
import time
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
# py files
import bus_car_st
import pred_consumption_of_cars
import Population_of_Korea
import needed_people
import Power_Capacity_trends_by_Type
import Predict_annual_carbon_emissions
import flourish_chart

st.set_page_config(page_title='탄소 배출량 분석과 예측',  layout='wide', page_icon=':ambulance:')

t1, t2 = st.columns((0.07,1)) 
t2.title("2030년까지의 탄소 배출량 감소 목표: 현실적인 분석과 예측")
t2.markdown(" **| MS AI SCHOOL 1차 프로젝트 |**")
t2.markdown(" **|제로탄소|** **|팀원 : 14반 12번 박혜인, 14반 15번 신동주, 15반 06번 김신실, 15반 28번 장예연, 15반 31번 허인석|**")

with st.expander('1 탄소 배출량 예측(2018-2030)'):
    Predict_annual_carbon_emissions.exchange_main()

with st.expander('2 자동차vs버스 배출량 비교'):
    bus_car_st.exchange_main()

with st.expander('3 pred_consumption_of_cars'):
    pred_consumption_of_cars.exchange_main()

with st.expander('4 Population_of_Korea(2018-2030)'):
    Population_of_Korea.exchange_main()

with st.expander('5 needed_people'):
    needed_people.exchange_main()

with st.expander('6 Power_Capacity_trends_by_Type'):
    Power_Capacity_trends_by_Type.exchange_main()

with st.expander('7 flourish_chart'):
    flourish_chart.exchange_main()