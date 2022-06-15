import streamlit
import pandas as pd
import requests 
my_fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')


streamlit.title('My Mom\'s new Healthy Dinner')

streamlit.header('Breakfast Menu')

streamlit.text('Omega 3 & Blueberry Oatmeal')

streamlit.text('Kale, Spinach & Rocket Smoothie')

streamlit.text('Hard-Boiled Free-Range Egg')

streamlit.header('Build your own smoothie')

my_fruit_list = my_fruit_list.set_index('Fruit')
fruit_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_Show = my_fruit_list.loc[fruit_selected]
# streamlit.dataframe(my_fruit_list)
streamlit.dataframe(fruits_to_Show)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruity_response)
