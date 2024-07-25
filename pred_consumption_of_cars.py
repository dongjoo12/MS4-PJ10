import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def exchange_main():
    # st.title("자동차의 연간 전력 소비량 예측 (2018-2030)")

    data = {
        'Year': [2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
        'Car_Trailer': [12900114, 11959143, 14787834, 16471822, 17041508, 17588169, 18334334, 18468778, 18276571, 17903597, 17582178, 17451506, 16488546, 17983076, 18516600, 18983693]
    }

    df = pd.DataFrame(data)

    def predict_emissions(df, industry, target_years):
        X = df[['Year']]
        y = df[industry]
        
        model = LinearRegression()
        model.fit(X, y)
        
        future_years = np.array(target_years).reshape(-1, 1)
        future_consumption = model.predict(future_years)
        
        return future_consumption

    target_years = list(range(2024, 2031))

    car_trailer_predictions = predict_emissions(df, 'Car_Trailer', target_years)

    future_df = pd.DataFrame({'Year': target_years, 'Car_Trailer': car_trailer_predictions})
    full_df = pd.concat([df, future_df])
    filtered_df = full_df[(full_df['Year'] >= 2018) & (full_df['Year'] <= 2030)]

    fig, ax = plt.subplots(figsize=(12, 8))
    ax.plot(filtered_df['Year'][:6], filtered_df['Car_Trailer'][:6], marker='o', linestyle='-', label='Power Consumption')
    ax.plot(future_df['Year'], future_df['Car_Trailer'], marker='o', linestyle=':', color='red', label='Predicted Power Consumption')
    ax.set_title('Prediction of annual electricity consumption of cars (2018-2030)')
    ax.set_xlabel('Year')
    ax.set_ylabel('Electricity consumption (MWh)')
    ax.legend()
    ax.grid(True)

    st.pyplot(fig)

    st.write(f"2030년 자동차의 예상 전기 소비량 : {car_trailer_predictions[-1]:.2f} MWh")

if __name__ == "__main__":
    exchange_main()
