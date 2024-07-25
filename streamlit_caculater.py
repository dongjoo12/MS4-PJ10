import streamlit as st

def exchange_main():
    # 배출 계수 (kg CO2e per km per kg)
    CO2_EMISSION_FACTOR = {
        'ship': 0.03,    # 해운 (가정치)
        'airplane': 0.25, # 항공 (가정치)
        'truck': 0.1     # 트럭 (가정치)
    }

    # 탄소 배출량 계산 함수
    def calculate_emission(distance, transport_mode, weight):
        emission_factor = CO2_EMISSION_FACTOR.get(transport_mode, 0)
        return distance * emission_factor * weight

    # Streamlit UI
    # st.set_page_config(page_title="주문상품 탄소 배출량 계산기", page_icon="🌍", layout="centered")

    # HTML 및 CSS 스타일 추가
    st.markdown("""
        <style>
        .stApp {
            background-color: #f5f5f5;
            font-family: Arial, sans-serif;
        }
        .header {
            background-color: #4CAF50;
            color: white;
            padding: 10px;
            text-align: center;
            border-radius: 10px;
        }
        
        .note {
            color: #ff5722;
            font-weight: bold;
        }
        </style>
        <div class="header">
            <h1>탄소 배출량 계산기</h1>
        </div>
        <div class="box">
    """, unsafe_allow_html=True)

    # 추후 거리를 자동 인식하는 기능을 구현할 예정
    st.write("**거리 자동 인식 기능은 추후 추가될 예정입니다. 현재는 고정된 출발지와 도착지를 사용합니다.**")

    # 사용자 입력
    transport_mode = st.selectbox('운송 수단을 선택하세요', ['ship', 'airplane', 'truck'])
    weight = st.number_input('상품의 무게를 입력하세요 (kg)', min_value=0.0, step=0.1)

    if st.button('탄소 배출량 계산'):
        fixed_distance = 300  # 예시로 300km를 사용
        emission = calculate_emission(fixed_distance, transport_mode, weight)
        st.write(f"운송 수단: {transport_mode}")
        st.write(f"거리: {fixed_distance} km")
        st.write(f"상품의 무게: {weight} kg")
        st.write(f"예상 탄소 배출량: {emission:.2f} kg CO2e")

    st.markdown("</div>", unsafe_allow_html=True)

if __name__ == '__main__':
    exchange_main()