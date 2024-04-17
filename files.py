import streamlit as st
import pandas as pd

st.subheader("Taking any type of file")
st.file_uploader("Upload the file here: ")

st.subheader("Dealing with CSV files")
df=st.file_uploader("Upload your CSV file here",type=['csv', 'xlsx'])
if df is not None:
    st.dataframe(df)
df=pd.read_csv('C:\\Users\\ayush\\Desktop\\Topic 2 Jupyter\\Streamlit\\biodata.csv')
st.write("Showing the dataFrame: ")
if df is not None:
    st.table(df.head())

st.subheader("Dealing with images")
photo=df=st.file_uploader("Upload your images here",type=['jpeg', 'png','jpg'])
if photo is not None:
    st.image(photo)
st.image('C:\\Users\\ayush\\Desktop\\Topic 2 Jupyter\\Streamlit\\photo.jpg')

st.subheader("Dealing with videos")
video=df=st.file_uploader("Upload your videos here",type=['mp4', 'mkv'])
if video is not None:
    st.video(video)
st.video('C:\\Users\\ayush\\Desktop\\Topic 2 Jupyter\\Streamlit\\video.mp4',start_time=2)

st.subheader("Dealing with audio")
song=df=st.file_uploader("Upload your videos here",type=['mp3','mp5', 'mp4','m4a'])
if song is not None:
    st.audio(song.read())
st.video('C:\\Users\\ayush\\Desktop\\Topic 2 Jupyter\\Streamlit\\audio.m4a',start_time=2)