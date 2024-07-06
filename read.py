import streamlit as st
import time as t

st.title("Streamlit Tutorial")

st.header("This is a header")

st.subheader("this is a subheader")

st.info("This is an information")

st.warning("This is a warning")

st.error("This is an error")

st.success("This a message for success")

st.markdown("""
    # This is a markdown header
## This is a markdown subheader

    * Bullet point 1
    * Bullet point 2
    * Bullet point 3
:moon: :smile: :smile: :snowman:
""")

#Widgets

st.checkbox("I am studying!!")

if st.checkbox('learning Streamlit'):
    st.info("You are learning Streamlit")
    st.image('image1.png')

# # widgets
st.button("Yo!")

if st.button('Click'):
    st.image('image2.jpeg')

st.radio('Pick your Gender',['Male', 'Female'])

n=st.selectbox('Select your country', ['USA', 'India', 'UK'])
# print(n)
if n=='India':
    st.write('You selected India')
elif n=='UK':
    st.write('You selected UK')
else:
    st.write('You selected USA')


x=st.multiselect('Select your Color',['black','blue','green','yellow','brown','orange','white'])

# print(x)

st.select_slider("Rating",['good','normal','bad',"worst"])
st.slider('Select your number',0,50,step=5)

st.number_input("Choose your Number",0,100,step=5)
st.text_input("Enter your Text Here")

st.date_input("Choose your Date of Birth",format='DD/MM/YYYY')
st.time_input("Select your Time of arrival")

st.progress(39)

# with st.spinner("please wait for some time"):
#     t.sleep(10)
#     st.success("Finished!")

# st.balloons()


st.sidebar.header("This is the sidebar")
email=st.sidebar.text_input("Enter mail address")
password=st.sidebar.text_input("Password",type='password')

if st.sidebar.button("Verify"):
    if email=='mail@gmail.com' and password=='password':
        st.sidebar.success("Logged In Successfully")
    else:
        st.sidebar.error("Invalid Credentials")

st.audio('audio1.wav')

import pandas as pd
import numpy as np

data=pd.DataFrame(np.random.randn(30,2),columns=['x', 'y'])
st.header("Bar Chart")
st.bar_chart(data)

st.header("Line Chart")
st.line_chart(data)

st.header("Area Chart")
st.area_chart(data)