import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d

def exchange_main():
    st.title('Population of Korea from 2018 to 2030')

    years = np.array([2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030])
    populations = np.array([51585058, 51764822, 51836239, 51769539, 51672569, 51712619, 51751065, 51684564, 51609121, 51534551, 51459877, 51384052, 51305713])

    f = interp1d(years, populations)

    years_interp = np.arange(2018, 2031)

    populations_interp = f(years_interp)

    fig, ax = plt.subplots()
    ax.plot(years_interp[:7], populations_interp[:7], 'bo-', label='Actual')
    ax.plot(years_interp[6:], populations_interp[6:], 'ro--', label='Predicted')
    ax.set_title('Population of Korea from 2018 to 2030')
    ax.set_xlabel('Year')
    ax.set_ylabel('Population')
    ax.grid(True)
    ax.legend()
    ax.ticklabel_format(useOffset=False, style='plain')
    ax.set_ylim(50000000, 52000000)
    st.pyplot(fig)

    for i in range(2025, 2031):
        decrease = populations_interp[i-2018] - populations_interp[i-2018-1]
        st.write(f"The population of Korea decreases by {abs(decrease):.0f} from {i-1} to {i}.")

if __name__ == "__main__":
    exchange_main()
