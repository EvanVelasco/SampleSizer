import streamlit as st
import pandas as pd
import utils.srs_functions as srs
import numpy as np 


def show_tab3():
    st.markdown('''
    # Simple Random Sample
    #### Population Proportion Sample Size Calculator
    ''')

    alpha = st.slider("alpha", 0.01, 0.20, value = 0.05, step = 0.01, key='alpha3',
                        help='Significance level')


    # Create a layout with three columns
    col1, col2, col3 = st.columns(3)

    # Assign each number input to a column
    with col1:
        N = st.number_input("N", min_value=1, value=None, format="%d", step=1, 
                            key='N3', help='Total population size')
    with col2:
        d = st.number_input("d", min_value=0.01, value=0.03, step=0.01, 
                            key='d3', help='Desired precision')
    with col3:
        p = st.number_input("p", value=0.5, 
                            key='p3', help='Proportion estimate')

    st.divider()

    if st.button('Calculate Sample Size', key='button3'):
        if N:
            is_finite=True
        else:
            is_finite=False

        test = srs.proportion_sample_size(p, d, alpha, N, is_finite)  # ensure the function name matches the imported module
        st.write(f'### Sample Size Required: {test}')

        alpha_range = [round(a, 2) for a in np.arange(0.01, 0.21, 0.01)]
        a_val = [srs.proportion_sample_size(p, d, alpha, N, is_finite) for a in alpha_range]
        a_chosen = ["#ffa421" if a==alpha else "#1c83e1" for a in alpha_range]

        if d >= 20:
            d_lower = np.linspace(d*0.5, d, 10, dtype=int)
            d_upper = np.linspace(d, d*1.5, 10, dtype=int)
        else:
            d_lower = np.linspace(d*0.5, d, 10).round(2)
            d_upper = np.linspace(d, d*1.5, 10).round(2)



        d_range = np.concatenate((d_lower, d_upper[1:]))
        #[round(a, 2) for a in np.linspace(d_lower, d_upper, 20, dtype=int)]
        d_val = [srs.proportion_sample_size(p, d, alpha, N, is_finite) for d in d_range]
        d_chosen = ["#ffa421" if i==d else "#1c83e1" for i in d_range]

        data_a = {
            'alpha': alpha_range,
            'required_sample_size': a_val,
            'chosen': a_chosen
        }

        data_d = {
            'd': d_range,
            'required_sample_size': d_val,
            'chosen': d_chosen
        }

        df_a = pd.DataFrame(data_a)
        df_d = pd.DataFrame(data_d)


        st.write('#### Req. Sample Size by Alpha')
        # Plotting the bar chart using Streamlit's built-in function
        st.bar_chart(df_a, x='alpha', y='required_sample_size', color='chosen',
                    x_label = 'Alpha', y_label = 'Req. Sample Size')

        st.write('#### Req. Sample Size by d')
        # Plotting the bar chart using Streamlit's built-in function
        st.bar_chart(df_d, x='d', y='required_sample_size', color='chosen',
                    x_label = 'd', y_label = 'Req. Sample Size')



