import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def exchange_main():
    data = {
        'Year': [2018, 2019, 2020, 2021, 2022, 2023],
        'Car_Trailer': [17582178, 17451506, 16488546, 17983076, 18516600, 18983693],
        'Food_Beverage': [11694806, 12067362, 12700786, 13398623, 13705942, 13787136],
        'Sound_Image': [51637544, 51983260, 53310591, 57788476, 60192109, 58359341],
        'Furniture_Others': [2919399, 3104649, 3262250, 3483009, 3502261, 3339708],
        'Chemistry': [40265239, 40187213, 38342495, 41256268, 40984440, 41210138]
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

    industries = ['Car_Trailer', 'Food_Beverage', 'Sound_Image', 'Furniture_Others', 'Chemistry']
    predictions = {}

    for industry in industries:
        predictions[industry] = predict_emissions(df, industry, target_years)

    future_df = pd.DataFrame({'Year': target_years})

    for industry in industries:
        future_df[industry] = predictions[industry]

    combined_df = pd.concat([df, future_df])

    st.title('제조업종별 연도별 전력 소비량 (2018-2030)')

    fig, ax = plt.subplots(figsize=(15, 10))

    for industry in industries:
        ax.plot(combined_df['Year'], combined_df[industry], marker='o', linestyle='-', label=f'{industry}')

    ax.set_xlabel('연도')
    ax.set_ylabel('전력 소비량 (MWh)')
    ax.legend()
    ax.grid(True)

    st.pyplot(fig)

    # for industry in industries:
    #     st.write(f"{industry}의 2030년 예측 전력 소비량: {predictions[industry][-1]:.2f} MWh")

if __name__ == '__main__':
    exchange_main()