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


streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','kiwi')
streamlit.write('The user entered', fruit_choice)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)


fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)

import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_row = my_cur.fetchall()
streamlit.header("The fruit list contains")
streamlit.dataframe(my_data_row)

