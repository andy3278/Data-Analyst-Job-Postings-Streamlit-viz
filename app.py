import streamlit as st
import pandas as pd
from google.oauth2 import service_account
from gsheetsdb import connect

import streamlit as st
from st_files_connection import FilesConnection

# Create connection object and retrieve file contents.
# Specify input format is a csv and to cache the result for 600 seconds.
conn = st.experimental_connection('gcs', type=FilesConnection)
df = conn.read("bucket-fro-streamlit/gsearch_jobs.csv", input_format="csv", ttl=600)

# Print results.
for row in df.itertuples():
    st.write(f"{row.title} \n {row.company_name}:")