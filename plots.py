import numpy as np
import pandas as pd
import seaborn as sbn
import streamlit as st
import matplotlib.pyplot as plt
st.header("1. Charts with randon numbers")
chartData=pd.DataFrame(np.random.randn(20,3), columns=['Line1','Line2', 'Line 3'])

st.subheader("1.1 Line Chart")
st.line_chart(chartData)

st.subheader("1.2 Area Chart")
st.area_chart(chartData)

st.subheader("1.3 Bar Chart")
st.bar_chart(chartData)

st.header("2. Visualization with Matplotlib and Seaborn")

st.subheader("2.1 Loading the dataFrame")
df=pd.read_csv("C:\\Users\\ayush\\Desktop\\Topic 2 Jupyter\\Streamlit\\biodata.csv")
st.dataframe(df.head())

st.subheader("Distribution Plot with Matplotlib")
fig=plt.figure(figsize=(15,8))
df['Name'].value_counts().plot(kind='bar')
st.pyplot(fig)

st.subheader("Distribution Plot with Seaborn")
fig=plt.figure(figsize=(15,8))
sbn.displot(df['Name'])
st.pyplot(fig)
st.pyplot()

# st.header('3. Multiple Graphs in one column')
# coll, col2 =st.columns(2)
# with coll:
#     coll=header ='KDE = False'
#     fig1 = plt.figure(figsize = (5,5))
#     sbn.displot(df ['Name'], kde = False)
#     st.pyplot(fig1)
# with col2:
#     col2.header= 'Hist = False'
#     fig2 = plt.figure(figsize = (5,5))
#     sbn.displot(df['Name'], hist = False)
#     st.pyplot(fig2)

# st.header("4. Changing the styles")
# coll, col2 =st.columns(2)
# with coll:
#     coll=header ='KDE = False'
#     fig1 =plt.figure(figsize = (5,5))
#     sbn.set_style('darkgrid')
#     sbn.set_context("Notebook")
#     sbn.displot(df ['Name'], kde = False)
#     st.pyplot(fig1)
# with col2:
#     col2.header= 'Hist = False'
#     fig2= plt.figure()
#     sbn.set_theme(context='poster', style='darkgrid')
#     sbn.displot(df['Name'], hist = False)
#     st.pyplot(fig2)



st.header("5. Exploring other graphs")

st.subheader("5.1 Scatter Plots")
fig,ax=plt.subplots(figsize=(15,8))
ax.scatter(*np.random.random(size=(2,100)))
st.pyplot(fig)

st.subheader("5.2 Count Plots")
fig,ax=plt.subplots(figsize=(15,8))
sbn.countplot(data=df, x='Name')
st.pyplot(fig)

st.subheader("5.3 Box Plots")
fig,ax=plt.subplots(figsize=(15,8))
sbn.boxplot(data=df, x='Name', y='Name')
st.pyplot(fig)

st.subheader("5.4 Violin Plots")
fig,ax=plt.subplots(figsize=(15,8))
sbn.violinplot(data=df, x='Name', y='Name')
st.pyplot(fig)


