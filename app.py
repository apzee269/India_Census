import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

data = pd.read_csv("India.csv")

list_of_states = data['State'].unique().tolist()
list_of_states.insert(0,'Overall India')

st.sidebar.title('India Data Visualization')
selected_state = st.sidebar.selectbox('Select A State',list_of_states)

primary = st.sidebar.selectbox('Select Primary Parameter',sorted(data.columns[5:]))
secondary = st.sidebar.selectbox('Select Secondary Parameter',sorted(data.columns[5:]))

plot = st.sidebar.button('Plot Graph')

if plot:
    if selected_state == 'Overall India':
        fig = px.scatter_mapbox(data, lat='Latitude', lon='Longitude', zoom=3, size = primary,mapbox_style="carto-positron")

        st.plotly_chart(fig)
    else:
        state_data = data[data['State'] == selected_state]
        fig = px.scatter_mapbox(state_data, lat='Latitude', lon='Longitude', zoom=3, size=primary, color=secondary,
                                mapbox_style="carto-positron")

        st.plotly_chart(fig)
