import streamlit as st
import pandas as pd
import utils.srs_functions as srs
import numpy as np  

tab1, tab2 = st.tabs(["SRS-Total", "SRS-Mean"])

with tab1:
    st.markdown('''
    # Simple Random Sample
    #### Population Total Sample Size Calculator
    ''')

    alpha = st.slider("alpha", 0.01, 0.20, value = 0.05, step = 0.01, key='alpha1',
                      help='Significance level')


    # Create a layout with three columns
    col1, col2, col3 = st.columns(3)

    # Assign each number input to a column
    with col1:
        N = st.number_input("N", min_value=1, value=100, format="%d", step=1, 
                            key='N1', help='Total population size')
    with col2:
        d = st.number_input("d", min_value=1, value=1000, format="%d", step=1, 
                            key='d1', help='Desired precision')
    with col3:
        s = st.number_input("s", value=43.96, 
                            key='s1', help='Standard deviation estimate')

    st.divider()

    if st.button('Calculate Sample Size', key='button1'):
        test = srs.pop_total_sample_size(N=N, d=d, alpha=alpha, s=s)  # ensure the function name matches the imported module
        st.write(f'### Sample Size Required: {test}')

        alpha_range = [round(a, 2) for a in np.arange(0.01, 0.21, 0.01)]
        a_val = [srs.pop_total_sample_size(N=N, d=d, alpha=a, s=s) for a in alpha_range]
        a_chosen = ["#ffa421" if a==alpha else "#1c83e1" for a in alpha_range]

        d_lower = np.linspace(d*0.5, d, 10, dtype=int)
        d_upper = np.linspace(d, d*1.5, 10, dtype=int)



        d_range = np.concatenate((d_lower, d_upper[1:]))
        #[round(a, 2) for a in np.linspace(d_lower, d_upper, 20, dtype=int)]
        d_val = [srs.pop_total_sample_size(N=N, d=d, alpha=alpha, s=s) for d in d_range]
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

with tab2:
    st.markdown('''
    # Simple Random Sample
    #### Population Mean Sample Size Calculator
    ''')

    alpha = st.slider("alpha", 0.01, 0.20, value = 0.10, step = 0.01, key='alpha2',
                      help='Significance level')


    # Create a layout with three columns
    col1, col2, col3 = st.columns(3)

    # Assign each number input to a column
    with col1:
        N = st.number_input("N", min_value=1, value=1000, format="%d", step=1, 
                            key='N2', help='Total population size')
    with col2:
        d = st.number_input("d", min_value=1, value=2, format="%d", step=1, 
                            key='d2', help='Desired precision')
    with col3:
        s = st.number_input("s", value=10, 
                            key='s2', help='Standard deviation estimate')

    st.divider()

    if st.button('Calculate Sample Size', key='button2'):
        test = srs.pop_mean_sample_size(N=N, d=d, alpha=alpha, s=s)  # ensure the function name matches the imported module
        st.write(f'### Sample Size Required: {test}')

        alpha_range = [round(a, 2) for a in np.arange(0.01, 0.21, 0.01)]
        a_val = [srs.pop_mean_sample_size(N=N, d=d, alpha=a, s=s) for a in alpha_range]
        a_chosen = ["#ffa421" if a==alpha else "#1c83e1" for a in alpha_range]

        if d >= 20:
            d_lower = np.linspace(d*0.5, d, 10, dtype=int)
            d_upper = np.linspace(d, d*1.5, 10, dtype=int)
        else:
            d_lower = np.linspace(d*0.5, d, 10).round(2)
            d_upper = np.linspace(d, d*1.5, 10).round(2)



        d_range = np.concatenate((d_lower, d_upper[1:]))
        #[round(a, 2) for a in np.linspace(d_lower, d_upper, 20, dtype=int)]
        d_val = [srs.pop_mean_sample_size(N=N, d=d, alpha=alpha, s=s) for d in d_range]
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



