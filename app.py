import streamlit as st
import pandas as pd


df = pd.read_csv('data/gsearch_jobs.csv')
st.write(df.head(15))