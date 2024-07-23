import streamlit as st
import matplotlib.pyplot as plt

def exchange_main():
    # 한국 에너지공단 정보 (단위 : g)
    co2_emission_per_km_bus_grams = 27.7
    co2_emission_per_km_car_grams = 210

    num_passengers = 1  # 50

    total_co2_emission_bus = co2_emission_per_km_bus_grams
    total_co2_emission_car = co2_emission_per_km_car_grams * num_passengers

    labels = ['Bus', 'Car']
    values = [total_co2_emission_bus, total_co2_emission_car]

    fig, ax = plt.subplots()
    ax.bar(labels, values, color=['blue', 'red'])
    ax.set_ylabel('CO2 emission (g per km)')
    ax.set_title('CO2 Bus vs Car')

    st.pyplot(fig)

if __name__ == '__main__':
    exchange_main()