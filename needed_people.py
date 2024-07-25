import streamlit as st
import matplotlib.pyplot as plt

def exchange_main():
    # st.title("몇 명이 더 참여해야 할까?")

    # 인구 데이터
    population = {
        2023: 51712619,
        2024: 51751065,
        2025: 51684564,
        2026: 51609121,
        2027: 51534551,
        2028: 51459877,
        2029: 51384052,
        2030: 51305713
    }

    # 탄소 배출량 (g)
    car_emission = 210
    bus_emission = 27.7

    # 버스에 탈 수 있는 사람 수
    bus_capacity = 50

    # 목표 탄소 감소량 (MMT)
    target_reduction = 12.74 * 10**9  # g

    # 각 연도별로 필요한 사람 수를 계산
    people_needed = {}
    for year, pop in population.items():
        # 자동차와 버스의 탄소 배출량 차이를 계산
        emission_diff = car_emission - bus_emission / bus_capacity
        # 목표 탄소 감소량을 달성하기 위해 필요한 사람 수를 계산
        people_needed[year] = target_reduction / emission_diff

    st.write('조건 : 자동차 탄소 배출량 = 210g, 버스 탄소 배출량 = 27.7g, 버스 최대 탑승 인원 = 50 명')
    st.write('목표 탄소 감소량 = 12.74 MMT')
    st.write('계산식 : 배출량 차이 = 자동차 탄소 배출량 - 버스 탄소 배출량 / 버스 최대 탑승 인원 (210g - 27.7g / 50 명)')
    st.write('매년 추가 인원 : 목표 탄소 감소량 / 배출량 차이 (12.74 MMT / 209.5g)')
    
    st.write(f'매년 추가 목표 이용객 수 : {int(people_needed[year])}') # 매년 골
    st.write(f'매일 추가 목표 이용객 수 : {int(people_needed[year]/365)}') # 매일 목표인데, 단순 계산으로 함 (이유는 정확하게 계산하지 않아도 됨. 어차피 초과 달성하면 더 좋기 때문)

    # # 결과를 시각화
    # fig, ax = plt.subplots(figsize=(10, 6))
    # ax.plot(list(people_needed.keys()), list(people_needed.values()), marker='o')
    # ax.set_xlabel('Year')
    # ax.set_ylabel('Number of People Needed to Switch from Car to Bus')
    # ax.grid(True)
    # st.pyplot(fig)

if __name__ == "__main__":
    exchange_main()
