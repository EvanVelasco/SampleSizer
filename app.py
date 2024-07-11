import streamlit as st
import pandas as pd
import srs_functions as srs
import numpy as np

st.write('''
# Simple Random Sample
#### Population Total Sample Size Calculator
''')


alpha = st.slider("alpha", 0.0, 0.20, value = 0.05, step = 0.01)


# Create a layout with three columns
col1, col2, col3 = st.columns(3)

# Assign each number input to a column
with col1:
    N = st.number_input("N", min_value=1, value=100, format="%d", step=1, help='Total population size')
with col2:
    d = st.number_input("d", min_value=1, value=1000, format="%d", step=1, help='Desired precision')
with col3:
    s = st.number_input("s", value=43.96, help='Standard deviation estimate')

#test = srs.pop_mean_sample_size(N=N, d=d, alpha=alpha, s=s)


if st.button('Calculate Sample Size'):
    test = srs.pop_total_sample_size(N=N, d=d, alpha=alpha, s=s)  # ensure the function name matches the imported module
    st.text(test)

    alpha_range = [round(a, 2) for a in np.arange(0.01, 0.21, 0.01)]
    val = [srs.pop_total_sample_size(N=N, d=d, alpha=a, s=s) for a in alpha_range]

    data = {
        'alpha': alpha_range,
        'required_sample_size': val
    }

    df = pd.DataFrame(data)

    st.title('Required Sample Size by Alpha')
    # Plotting the bar chart using Streamlit's built-in function
    st.bar_chart(df.set_index('alpha'))




