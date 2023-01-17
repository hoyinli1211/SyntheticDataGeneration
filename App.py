import streamlit as st
from faker import Faker
import pandas as pd

#Sidebar
st.sidebar.title("Instructions:")
st.sidebar.markdown("1. Select the data type from the dropdown menu")
st.sidebar.markdown("2. Select the language from the checkbox menu")
st.sidebar.markdown("3. Enter the number of records to generate")
st.sidebar.markdown("4. Click the 'Generate Data' checkbox to generate the synthetic data")

def faker_introduction():
  st.title("Faker Introduction")
  st.markdown("Faker is a Python package that generates synthetic data for various purposes such as testing and data analysis. It can be used to generate fake names, addresses, email addresses, etc.")
  st.markdown("Generating synthetic data can be useful for testing and data analysis purposes, as it allows you to work with a large dataset without compromising on the privacy of real users.")

def create_data(choice, n):
  data = pd.DataFrame()
  # Iterate through the selected data types
  for data_type in data_type_choice:
      new_col = []
      if data_type == "name":
          for _ in range(num_records):
              name = fake.name()
              new_col.append(name)
          data = pd.concat([data, pd.DataFrame({'Name': new_col})], axis=1)
      elif data_type == "address":
          for _ in range(num_records):
              address = fake.address()
              new_col.append(address)
          data = pd.concat([data, pd.DataFrame({'Address': new_col})], axis=1)
      elif data_type == "email":
          for _ in range(num_records):
              email = fake.email()
              new_col.append(email)
          data = pd.concat([data, pd.DataFrame({'Email': new_col})], axis=1)
  return data

#Main Page
st.title("Data Profiling Report")
tabs = st.tabs(["Note","Configuration & Synthetic Data Generation"])

tab_note = tabs[0]

with tab_note:
    faker_introduction()

tab_main = tabs[1]

with tab_main:

  fake = Faker()
  # Get the list of providers for the selected locale
  data_type_choice = dir(fake)
  
  # Ask the user to select data types
  data_type_choice = st.multiselect("Select data types", data_type_choice)

  # Use the `number_input` widget to gather the user's desired number of records
  num_records = st.number_input("Enter the number of records to generate", min_value=1)
  
  if st.checkbox("Generate Data"):
    df=create_data(data_type_choice,num_records)
    st.write('Synthetic Data',df)
    
               
