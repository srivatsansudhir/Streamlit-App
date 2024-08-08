import pandas as pd
import zipfile
import os
import streamlit as st
from pandasai import SmartDataframe


zip_file_path = 'CSV_5262024-602.zip'
csv_file_name = 'CSV_5262024-602.csv'


with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extract(csv_file_name)


extracted_csv_path = csv_file_name 


df = pd.read_csv(extracted_csv_path)
st.write("csv read")
#st.write(df.to_string()) 


from pandasai.agent import Agent
from pandasai import Agent
from pandasai.llm import OpenAI
from pandasai.llm import BambooLLM
llm = BambooLLM(api_key="$2a$10$x3EcWszIfXWOuK74XI.tEON6eWJIsRtAzj4e6Y4Q0TS1tyxwrFMXe")

os.environ["PANDASAI_API_KEY"] = "$2a$10$x3EcWszIfXWOuK74XI.tEON6eWJIsRtAzj4e6Y4Q0TS1tyxwrFMXe"


agent = Agent(SmartDataframe(df,{"enable_cache": False}),config={"llm": llm})
st.write("created frame")
#question=input("What would you like to know? ")
response = agent.chat('Which 10 universities have the most total applicants?')
st.write(response)







