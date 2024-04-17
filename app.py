# streamlit is used to rum python programmes on the local host and then deploy them.

import streamlit as st

st.title("Hello, My name is Ayush Budhlakoti")     # Adds a title
st.header("I'm a Computer Science Student at Graphic Era Hill University")   # Adds a subheader
st.subheader("Currently I'm studying machine learning with Pyhton")   # Adds a header
st.text("My average CGPA is 8.75")   #    Adds plain text

st.markdown("# Hello")       # size 6
st.markdown("## Hello")      # size 5
st.markdown("### Hello")     # size 4
st.markdown("#### Hello")    # size 3
st.markdown("##### Hello")   # size 2
st.markdown("Hello")         # size 1

st.success("Success")           # green color
st.info("INformation")          # blue
st.warning("Warning")           # yellow
st.error("Error !!! ")          # red

st.exception(ZeroDivisionError("Division not possible"))   # specific type of errorHandling
st.help(ZeroDivisionError)                                  # help gives a brief refrence about the fumction
st.help(Warning)

st.write("range(1,10)")    # writes as text
st.write(range(1,10))      # writes as code
st.write(1+2+3)            # solves the equation

st.code("x=10 \n"
        "for i in range(1,x): \n"   # writes in the code format
        "\tprint(i)")

st.checkbox("Male")            # checkbox
st.checkbox("Female")          # no two checkboxes can have same values
st.checkbox("Prefer not to say")   # can select multiple checkboxes

if(st.checkbox("Adult")):
    st.write("You are an adult")   # checkbox with a value (output)

st.radio('Select your Name : ', ('Ayush','Maksood','Ankit') )     # can select only one radioButton at a time

r=st.radio('Select your gender : ', ('Male','Female','Other') )   # radioButton with output
if(r=='Male'):
    st.write("You are a male")
elif(r=='Female'):
    st.write('You are a female')     # printing message according to the value of radio button
else:
    st.write("You are gay / lesbian")

st.subheader("Select your name: ")
st.selectbox("Name",["Ayush","Joshi","Ankit","Maksood"])  # can select a single item from a drop down menu

st.subheader("Select your Profession: ")
ans=st.selectbox("Specialization: ",["Data Analyst","Programmer","Developer","Hacker"])
st.write("oh.. you are a ",ans)    # select box with outputs

st.subheader("Select your Skills: ")
ans2=st.multiselect("Skills: ",["DSA","C","C++","Machine Learning"])   # can select multiple items from a multi-selectBox
st.write("Your skills are: ",len(ans),ans2)

st.subheader("Button: ")
st.button("I'm a button...click me")   # creates a clickable button

if(st.button("i'm a button with output")):
    st.write("Thanks for clicking me")    #  prints message on creating button

st.header("Volume changing slider")
volume=st.slider("Change volume",0,100,step=1)  # creates a slider starting from 0 to 100 and increment by 1
st.write("The current volume is: ",volume,'%')

st.header("Text input: ")
username=st.text_input("Enter your username: ")   # taking text input
password=st.text_input("Enter your password: ",type='password')  # taking password input

st.header("Text Area: ") 
st.text_area("Introduce yourself in 500 words: ")   # can add a paragraph

st.header("Input number/data/time: ")
st.number_input("Enter your age: ",18,110)   # inputs a number
st.date_input("Enter your DOB: ")            # inputs the data using a calender
st.time_input("Enter current time: ")        # inputs the time in 24-hr format

