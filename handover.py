import streamlit as st
import time
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import bus_car_st
import Predict_annual_carbon_emissions

st.set_page_config(page_title='탄소 배출량 분석과 예측',  layout='wide', page_icon=':ambulance:')

#this is the header
t1, t2 = st.columns((0.07,1)) 
t2.title("2030년까지의 탄소 배출량 감소 목표: 현실적인 분석과 예측")
t2.markdown(" **| MS AI SCHOOL 1차 프로젝트 |**  14반 12번 박혜인, 14반 15번 신동주, 15반 06번 김신실, 15반 28번 장예연, 15반 31번 허인석")

## Data
with st.spinner('Updating Report...'):
    #Metrics setting and rendering
    # m1, m2, m3, m4, m5 = st.columns((1,1,1,1,1))
    # m1.write('')
    # m2.metric(label ='Total Outstanding Handovers',value = 0, delta = '0 Compared to 1 hour ago', delta_color = 'inverse')
    # m3.metric(label ='Current Handover Average',value = "0 Mins", delta = '0 Compared to 1 hour ago', delta_color = 'inverse')
    # m4.metric(label = 'Time Lost today (Above 15 mins)',value = "0 Hours", delta = '0 Compared to yesterday')
    # m1.write('')
    
    # Number of Completed Handovers by Hour
    st.write('-------------------------------------------------------------------')
    st.subheader('탄소 배출량 예측(2018-2030)')
    Predict_annual_carbon_emissions.exchange_main()
    st.write('-------------------------------------------------------------------')

    # g1, g2, g3 = st.columns((1,1,1))
    # fig = px.bar(template = 'seaborn')
    # fig.update_traces(marker_color='#264653')
    # fig.update_layout(title_text="Number of Completed Handovers by Hour",title_x=0,margin= dict(l=0,r=10,b=10,t=30), yaxis_title=None, xaxis_title=None)
    # g1.plotly_chart(fig, use_container_width=True) 
    
    # Predicted Number of Arrivals
    # fig = px.bar(template = 'seaborn')
    # fig.update_traces(marker_color='#7A9E9F')
    # fig.update_layout(title_text="Predicted Number of Arrivals",title_x=0,margin= dict(l=0,r=10,b=10,t=30), yaxis_title=None, xaxis_title=None)
    # g2.plotly_chart(fig, use_container_width=True)  
    
    # Average Completed Handover Duration by hour
    # fig = px.bar(template = 'seaborn', color_continuous_scale=px.colors.diverging.Temps)
    # fig.update_layout(title_text="Average Completed Handover Duration by hour",title_x=0,margin= dict(l=0,r=10,b=10,t=30), yaxis_title=None, xaxis_title=None, legend=dict(orientation="h",yanchor="bottom",y=0.9,xanchor="right",x=0.99))
    # g3.plotly_chart(fig, use_container_width=True) 
      
    # Waiting Handovers table
    cw1, cw2 = st.columns((2.5, 1.7))
    fig = go.Figure(
            data = [go.Table (columnorder = [0,1,2,3,4,5,6,7,8,9], columnwidth = [30,10,10,10,10,15,15,15,15,15],
                header = dict(
                 font=dict(size=12, color = 'white'),
                 fill_color = '#264653',
                 line_color = 'rgba(255,255,255,0.2)',
                 align = ['left','center'],
                 height=20
                 )
              , cells = dict(
                  font=dict(size=12),
                  align = ['left','center'],
                  fill_color = [],
                  line_color = 'rgba(255,255,255,0.2)',
                  height=20))])
    fig.update_layout(title_text="Current Waiting Handovers",title_font_color = '#264653',title_x=0,margin= dict(l=0,r=10,b=10,t=30), height=480)                                                           
    cw1.plotly_chart(fig, use_container_width=True)    
    
    # Current Waiting Table
    fig = go.Figure(
            data = [go.Table (columnorder = [0,1,2,3], columnwidth = [15,40,20,20],
                header = dict(
                 font=dict(size=12, color = 'white'),
                 fill_color = '#264653',
                 align = 'left',
                 height=20
                 )
              , cells = dict(
                  font=dict(size=12),
                  align = 'left',
                  fill_color='#F0F2F6',
                  height=20))]) 
    fig.update_layout(title_text="Current Waiting Callsigns",title_font_color = '#264653',title_x=0,margin= dict(l=0,r=10,b=10,t=30), height=480)
    cw2.plotly_chart(fig, use_container_width=True)
       
with st.spinner('Report updated!'):
    time.sleep(1)     
    
# Performance Section  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>이거 사용할 예정
with st.expander("Previous Performance"):
    fig = go.Figure(
            data = [go.Table (columnorder = [0,1,2,3,4,5,6,7,8,9,10,11,12], columnwidth = [18,12],
                header = dict(
                 font=dict(size=11, color = 'white'),
                 fill_color = '#264653',
                 line_color = 'rgba(255,255,255,0.2)',
                 align = ['left','center'],
                 height=20
                 )
              , cells = dict(
                  font=dict(size=10),
                  align = ['left','center'],
                  fill_color = [],
                  line_color = 'rgba(255,255,255,0.2)', 
                  height=20))])
    fig.update_layout(title_text="Hospital Handovers Completed in the Past 24 Hours",title_font_color = '#264653',title_x=0,margin= dict(l=0,r=10,b=10,t=30), height=400)                                                               
    st.plotly_chart(fig, use_container_width=True)      
    p1,p2 = st.columns((3, 1.7))   
