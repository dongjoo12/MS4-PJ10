import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def exchange_main():
    kepco_data = pd.read_csv('greenhouseEM.csv', delimiter=',', encoding='utf-8')

    # 발전 전력량 그래프 설정
    plt.figure(figsize=(12, 12))

    # 각각의 발전 유형에 대한 라인 플롯 (발전 전력량)
    plt.subplot(2, 1, 1)
    plt.plot(kepco_data['Year'], kepco_data['Hydro_Gen'], label='Hydro Generation', marker='o')
    plt.plot(kepco_data['Year'], kepco_data['Thermal_Gen'], label='Thermal Generation', marker='o')
    plt.plot(kepco_data['Year'], kepco_data['Combined_Gen'], label='Combined Generation', marker='o')
    plt.plot(kepco_data['Year'], kepco_data['Nuclear_Gen'], label='Nuclear Generation', marker='o')
    plt.plot(kepco_data['Year'], kepco_data['Renewable_Gen'], label='Renewable Generation', marker='o')
    plt.plot(kepco_data['Year'], kepco_data['District_Gen'], label='District Generation', marker='o')
    plt.plot(kepco_data['Year'], kepco_data['Internal_Comb_Gen'], label='Internal Combustion Generation', marker='o')
    plt.plot(kepco_data['Year'], kepco_data['Other_Gen'], label='Other Generation', marker='o')
    plt.plot(kepco_data['Year'], kepco_data['Purchased_Gen'], label='Purchased Generation', marker='o')

    # 그래프 제목 및 레이블 설정 (발전 전력량)
    plt.title('Power Generation Trends by Type (2018-2023)')
    plt.xlabel('Year')
    plt.ylabel('Power Generation (MWh)')
    plt.legend()
    plt.grid(True)

    # 설비 용량 그래프 설정
    plt.subplot(2, 1, 2)
    plt.plot(kepco_data['Year'], kepco_data['Hydro_Cap'], label='Hydro Capacity', marker='o')
    plt.plot(kepco_data['Year'], kepco_data['Thermal_Cap'], label='Thermal Capacity', marker='o')
    plt.plot(kepco_data['Year'], kepco_data['Combined_Cap'], label='Combined Capacity', marker='o')
    plt.plot(kepco_data['Year'], kepco_data['Nuclear_Cap'], label='Nuclear Capacity', marker='o')
    plt.plot(kepco_data['Year'], kepco_data['Renewable_Cap'], label='Renewable Capacity', marker='o')
    plt.plot(kepco_data['Year'], kepco_data['District_Comb_Cap'], label='District Combustion Capacity', marker='o')
    plt.plot(kepco_data['Year'], kepco_data['Internal_Comb_Cap'], label='Internal Combustion Capacity', marker='o')
    plt.plot(kepco_data['Year'], kepco_data['Other_Cap'], label='Other Capacity', marker='o')

    # 그래프 제목 및 레이블 설정 (설비 용량)
    plt.title('Power Capacity Trends by Type (2018-2023)')
    plt.xlabel('Year')
    plt.ylabel('Power Capacity (MW)')
    plt.legend()
    plt.grid(True)

    # 그래프 출력
    ax = plt.tight_layout()

    st.set_option('deprecation.showPyplotGlobalUse', False)
    
    # Display the plots
    st.pyplot(ax)

if __name__ == '__main__':
    exchange_main()
