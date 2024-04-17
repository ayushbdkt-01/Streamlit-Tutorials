import streamlit as st
import pandas as pd
import numpy as np
import matplotlib as plt
import altair as alt

st.header("1. Altair Scatter plot")
chartData=pd.DataFrame(np.random.randn(500,5), columns=['a','b','c','d','e'])
chart=alt.Chart(chartData).mark_circle().encode(x='a',y='b',size='c', tooltip=['a','b','c','d','e'])
st.altair_chart(chart)

st.header("2.Interactive Chart")
df=pd.read_csv("C:\\Users\\ayush\\Desktop\\Topic 2 Jupyter\\customers.csv")
l=df.columns.tolist()
choices=st.multiselect("Choose your favouriate: ",l)
newDf=df[choices]
st.line_chart(newDf.head())
st.area_chart(newDf.head())