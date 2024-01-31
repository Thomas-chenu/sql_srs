import streamlit as st
import pandas as pd
import duckdb

st.write("Hello World")

data = {"a": [1, 2, 3], "b": [4, 5, 6]}
df = pd.DataFrame(data)

tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
    query_sql = st.text_area(label='entrez votre input')
    result = duckdb.sql(query_sql).df()
    st.write(f"Vous avez entre la query suivante : {query_sql}")
    st.dataframe(result)
