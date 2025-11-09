import streamlit as st
import pandas as pd
import numpy as np

#tital of the app
st.title("My First Streamlit App")

#display a simple text
st.write("Hello, welcome to my Streamlit app!")
#display a dataframe
data = {
    'Column 1': [1, 2, 3, 4, 5],
    'Column 2': ['A', 'B', 'C', 'D', 'E']
}
df = pd.DataFrame(data)
st.write("Here is a sample dataframe:")
st.dataframe(df)

#display a line chart
chart_data = pd.DataFrame(
    np.random.randn(20, 4),
    columns=['a', 'b', 'c','d']
)
st.line_chart(chart_data)

#interactive widget
option = st.selectbox(
    'Select a number to see its square:',
    list(range(1, 11))
)
st.write(f'The square of {option} is {option ** 2}.')