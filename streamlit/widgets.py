import streamlit as st
import pandas as pd

st.title("Steamlit text input")
user_input = st.text_input("Enter some text:", "Type here...")

age = st.slider("Select your age:", 0, 100,25)
st.write(f"You are {age} years old.")

if user_input == "wael":
    st.success("Welcome Wael!")

st.write("You entered:", user_input)

#file uploader (any type of files)
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    st.write("File uploaded successfully!")
    st.write("Filename:", uploaded_file.name)
# To read file as bytes:
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    st.write("File size (in bytes):", len(bytes_data))

# To read csv file:
csv_file = st.file_uploader("Upload a CSV file", type="csv")
if csv_file is not None:
    df = pd.read_csv(csv_file)
    st.write("CSV file content:")
    st.dataframe(df)
    st.write("Number of rows:", df.shape[0])
    st.write("Number of columns:", df.shape[1])
    