import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError



streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

#insert drop down
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado', 'Strawberries'])

#display table data
streamlit.dataframe(my_fruit_list)

#Define function
def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get('https://fruityvice.com/api/fruit/'+ fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized

#display fruityvice api response
streamlit.header('Fruityvice Fruit Advice')

try:               
  fruit_choice =streamlit.text_input('What fruit would you like information about?' )
  if not fruit_choice:
      streamlit.error("Please select a fruit to get information. ")
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)
      
except URLError as e:
      streamlit.error()
      


streamlit.header("The fruit load list contains:")
#Snowflake related functions
def get_fruit_load_list():
    with  my_cnx.cursor() as my_cur:
        my_cur.execute("SELECT * from fruit_load_list")
        return my_cur.fetchall()  
    
    
 #add button to fruit load
if streamlit.button('Get Fruit Load List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = get_fruit_load_list()
    streamlit.dataframe(my_data_rows)

#allow user to add frui to the list
def insert_rom_snowflake(new_fruit):
    with my_cnx.cursor() as my_cur:
         my_cur.execute("insert into fruit_load_list values ('from streamlit')")
         return streamlit.write('Thanks for adding ' + add_my_fruit)
        
add_my_fruit =streamlit.text_input('What fruit would you like to add?', 'jackfruit')
if streamlit.button('Add afruit to the list'):
     my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
     back_from_function = insert_row_snowflake(add_my_fruit)
     streamlit.text(back_from_function)





