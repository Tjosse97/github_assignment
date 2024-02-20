import streamlit as st
import pandas as pd

st.markdown("# Kart Configurations 🏎️")
st.sidebar.markdown("# Kart Configurations 🏎️")

st.write("What Kart Configuration is Best?")

### Part 1
df_kart = pd.read_csv('data/kart_stats.csv')

st.dataframe(df_kart.style
             .highlight_max(color='lightgreen', axis=0,subset=['Body','Weight','Acceleration','Ground Speed', 'Water Speed', 'Air Speed'])
             .highlight_min(color='lightpink', axis=0,subset=['Body','Weight','Acceleration','Ground Speed', 'Water Speed', 'Air Speed'])
)

##### PART 2
st.write("Scatter Chart")
st.scatter_chart(df_kart, x='Body',y=['Ground Speed', 'Water Speed', 'Air Speed'])

st.write("Area Chart")
st.area_chart(df_kart, x='Body', y=['Ground Speed', 'Water Speed', 'Air Speed'])

##### PART 3
choose_kart = st.selectbox("Pick Your Kart!", df_kart['Body'])

df_single_kart = df_kart.loc[df_kart['Body'] == choose_kart]

df_single_kart = df_single_kart.drop(columns=['Body'])

df_unp_kart = df_single_kart.unstack().rename_axis(['category','row number']).reset_index().drop(columns='row number').rename({0:'strength'}, axis=1)

st.bar_chart(df_unp_kart, x='category', y='strength')

