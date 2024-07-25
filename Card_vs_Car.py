import streamlit as st
import matplotlib.pyplot as plt

def exchange_main():
    # st.title("Cost and Emission Comparison")

    climate_companion_card_cost = 65000
    car_maintenance_cost = 142000 # 자동차 유지비 10만원 (최소치), 주유비 4만 2천원 , 플러스 알파 금액

    cost_ratio = car_maintenance_cost / climate_companion_card_cost

    bus_emission = 27.7
    car_emission = 210

    average_commuting_distance = 20 # 20km
    average_commuting_time = 1.2 # 1시간 20분 출퇴근 시간 합친 시간

    bus_total_emission = bus_emission * average_commuting_distance * average_commuting_time
    car_total_emission = car_emission * average_commuting_distance * average_commuting_time

    emission_ratio = car_total_emission / bus_total_emission

    st.write(f"기후동행카드가 자동차보다 {cost_ratio:.2f}배 저렴합니다.")
    st.write(f"버스의 탄소 배출량이 자동차보다 {emission_ratio:.2f}배 적습니다.")

    fig1 = plt.figure(figsize=(10, 5))
    plt.bar(['Bus', 'Car'], [bus_total_emission, car_total_emission], color=['b', 'r'])
    plt.title('Emission Comparison')
    plt.ylabel('Emission (g)')
    st.pyplot(fig1)
    st.write('버스와 자동차의 배출량 비교')
    st.write('자동차의 탄소 배출량은 210g, 버스의 탄소 배출량은 27.7g')
    st.write('평균 출퇴근 거리 20km, 평균 출퇴근 시간 1시간 20분으로 가정')
    st.write('계산식 : 버스 배출량 * 출퇴근 거리 * 출퇴근 시간 | 자동차 배출량 * 출퇴근 거리 * 출퇴근 시간')

    st.write('-------------------------------------------------------------------')

    fig2 = plt.figure(figsize=(10, 5))
    plt.bar(['Climate Companion Card', 'Car + α'], [climate_companion_card_cost, car_maintenance_cost], color=['b', 'r'])
    plt.title('Cost Comparison')
    plt.ylabel('Cost (KRW)')
    st.pyplot(fig2)
    st.write('서울시 기후동행카드 금액과 자동차 유지비용인 최저 금액 10만원과 매일 20km 이동 거리 주유비의 한 달 가격 비교')
    st.write('자동차는 보험료, 수리 등의 추가 비용이 발생 가능하여 보이는 차트 이외의 추가 금액을 반영해야 한다.(차트에는 반영 X)')
    st.write('주유비 조건 : 평균 출퇴근 20km, 연비 24.4km/l, 휘발유 가격 1,700원/l')
    st.write('주유비 계산식 : (20km * 30일) / 24.4km * 1,700원')

if __name__ == "__main__":
    exchange_main()
