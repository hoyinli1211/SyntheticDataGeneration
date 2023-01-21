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

# Create a dictionary to map data types to their corresponding methods in the Faker class
fake = Faker()
data_type_mapping = {
  #customer profile related
  "name": fake.name,
  "first_name": fake.first_name,
  "last_name": fake.last_name,
  "prefix": fake.prefix,
  "suffix": fake.suffix,
  "job": fake.job,
  "address": fake.address,
  "email": fake.email,
  "phone_number": fake.phone_number,
  "date_of_birth": fake.date_of_birth,
  "gender": fake.random_element(elements=("male", "female")),
  "ssn": fake.ssn,
  "username": fake.user_name,
  "password": fake.password,
  "url": fake.url,
  "company_suffix": fake.company_suffix,
  "company": fake.company,
  #transaction related
  "tran_date": fake.date_this_decade,
  "tran_datetime": fake.date_time,
  "tran_amount": fake.random_int(1, 100000),
  "tran_CD": fake.random_element(elements=("debit", "credit")),
  "tran_status": fake.random_element(elements=("approved", "declined", "pending")),
  "tran_type": fake.random_element(elements=("ATM", "FPS", "CHATs", "SWIFT", "CHEQUE", "Others")),
  "tran_channel": fake.random_element(elements=("Internet Banking","Mobile Banking","Branch/ATM")),
  "ctp_name": fake.name
}  

def create_data(type, choice, n):

  type = data_type_mapping
  # Create an empty dataframe
  data = {}

  # Iterate through the selected data types
  for data_type in choice:
      method = type[data_type]
      data[data_type] = [method() for _ in range(n)]
  df = pd.DataFrame(data)
  return df

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
  data_type_choice = list(data_type_mapping.keys())
  
  # Ask the user to select data types
  data_type_choice = st.multiselect("Select data types", data_type_choice)

  # Use the `number_input` widget to gather the user's desired number of records
  num_records = st.number_input("Enter the number of records to generate", min_value=1)
  
  if st.button("Generate Data"):
    df=create_data(data_type_mapping, data_type_choice, num_records)
    st.write('Synthetic Data',df)
    
               
