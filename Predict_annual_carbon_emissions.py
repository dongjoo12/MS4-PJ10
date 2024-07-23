import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

def exchange_main():
    st.title('KEPCO Carbon Emissions Analysis')

    # Load data
    kepco_data = pd.read_csv('KEPCO_data.csv', delimiter=',', encoding='utf-8')

    # Carbon emission factors in kg CO2 per MWh
    emission_factors = {
        'Hydro_Gen': 0,
        'Thermal_Gen': 900,
        'Combined_Gen': 450,
        'Nuclear_Gen': 0,
        'Renewable_Gen': 0,
        'District_Gen': 900,
        'Internal_Comb_Gen': 700,
        'Other_Gen': 700
    }

    # Calculate annual carbon emissions
    def calculate_emissions(row, factors):
        emissions = 0
        for key, factor in factors.items():
            emissions += row[key] * factor
        return emissions

    kepco_data['Carbon_Emissions'] = kepco_data.apply(calculate_emissions, axis=1, factors=emission_factors)

    # Convert emissions to million metric tons (MMT) for readability
    kepco_data['Carbon_Emissions_MMT'] = kepco_data['Carbon_Emissions'] / 1e6

    # Display the calculated emissions
    st.dataframe(kepco_data[['Year', 'Carbon_Emissions_MMT']])

    # Plot historical emissions
    plt.figure(figsize=(10, 6))
    plt.plot(kepco_data['Year'], kepco_data['Carbon_Emissions_MMT'], marker='o', linestyle='-')
    plt.title('Annual Carbon Emissions of KEPCO (2018-2023)')
    plt.xlabel('Year')
    plt.ylabel('Carbon Emissions (MMT)')
    plt.grid(True)
    st.pyplot(plt.gcf())

    # Linear regression for future projections
    X = kepco_data[['Year']]
    y = kepco_data['Carbon_Emissions_MMT']

    model = LinearRegression()
    model.fit(X, y)

    # Predict future emissions
    future_years = np.array([2024, 2025, 2026, 2027, 2028, 2029, 2030]).reshape(-1, 1)
    future_emissions = model.predict(future_years)

    # Plot future projections
    plt.figure(figsize=(10, 6))
    plt.plot(kepco_data['Year'], kepco_data['Carbon_Emissions_MMT'], marker='o', linestyle='-', label='Historical')
    plt.plot(future_years, future_emissions, marker='x', linestyle='--', label='Projected')
    plt.axhline(y=kepco_data.loc[kepco_data['Year'] == 2018, 'Carbon_Emissions_MMT'].values[0] * 0.6, color='r', linestyle='--', label='Target (60% of 2018)')
    plt.title('Projected Carbon Emissions of KEPCO (2018-2030)')
    plt.xlabel('Year')
    plt.ylabel('Carbon Emissions (MMT)')
    plt.legend()
    plt.grid(True)
    st.pyplot(plt.gcf())

    # Check if the goal is achievable
    target_2030_emissions = kepco_data.loc[kepco_data['Year'] == 2018, 'Carbon_Emissions_MMT'].values[0] * 0.6
    projected_2030_emissions = future_emissions[-1]

    st.write(f"Target 2030 Emissions: {target_2030_emissions:.2f} MMT")
    st.write(f"Projected 2030 Emissions: {projected_2030_emissions:.2f} MMT")

    if projected_2030_emissions <= target_2030_emissions:
        st.write("KEPCO is on track to meet the 40% reduction goal by 2030.")
    else:
        st.write("KEPCO needs to implement additional measures to meet the 40% reduction goal by 2030.")

if __name__ == '__main__':
    exchange_main()