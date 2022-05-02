import streamlit
import pandas as pd

my_fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')


streamlit.title('My Mom\'s new Healthy Dinner')

streamlit.header('Breakfast Menu')

streamlit.text('Omega 3 & Blueberry Oatmeal')

streamlit.text('Kale, Spinach & Rocket Smoothie')

streamlit.text('Hard-Boiled Free-Range Egg')

streamlit.header('Build your own smoothie')

streamlit.dataframe(my_fruit_list')
