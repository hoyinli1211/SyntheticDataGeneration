import streamlit as st
from faker import Faker

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
  for _ in range(n):
    for data_type in data_type_choice:
      if data_type == "person":
        name = fake.name()
        address = fake.address()
        data = data.append({'Name': name, 'Address': address}, ignore_index=True)
      elif data_type == "address":
        address = fake.address()
        data = data.append({'Address': address}, ignore_index=True)
      elif data_type == "email":
        email = fake.email()
        data = data.append({'Email': email}, ignore_index=True)
      else:
        Nothing
  return data

#Main Page
st.title("Data Profiling Report")
tabs = st.tabs(["Note","Configuration & Synthetic Data Generation"])

tab_note = tabs[0]

with tab_note:
    faker_introduction()

tab_main = tabs[1]

with tab_main:
  # Create an instance of the Faker class
  fake = Faker()

  # Use the `selectbox` widget to gather the user's data type choice
  data_types = dir(F)
  data_type_choice = st.multiselect("Select the data type", data_types)

  # Use the `multiselectbox` widget to gather the user's language choice
  languages = fake.locales
  language_choice = st.multiselect("Select the language", languages)

  # Use the `number_input` widget to gather the user's desired number of records
  num_records = st.number_input("Enter the number of records to generate", min_value=1)
  
  columns = []
  data = pd.DataFrame(columns=columns)
  
  if st.checkbox("Generate Data"):
    df=create_data(data_type_choice,num_records)
    st.write('Synthetic Data',df)
    
               