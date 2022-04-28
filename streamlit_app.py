import streamlit
import pandas


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

#display fruityvice api response

streamlit.header('Fruityvice Fruit Advice')
fruit_choice =streamlit.text_input('What fruit would you like information about?', 'kiwi')
streamlit.write('The user entered' + fruit_choice)
                
import requests
fruityvice_response = requests.get('https://fruityvice.com/api/fruit/'+ fruit_choice)

                                                   
                                                   
#streamlit.text(fruityvice_response.json()) #writes data to screen

#normalize
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#output to screen as table
streamlit.dataframe(fruityvice_normalized )




