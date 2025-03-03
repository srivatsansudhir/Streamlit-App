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




st.markdown('''<span style="font-size: 36px;">University Interface</span>''', unsafe_allow_html=True)
st.markdown('''<span style="font-size: 15px;">This is a interface that answers questions based on 2022 data of 150 top American universities from QS World University Rankings. Try asking "What are the 5 universities with the lowest acceptance rates?", "What are the top 10 universities with the highest median SAT math scores?", "What are the top 15 universities with the lowest tuition?", "What are the top 20 universities with the highest percentage of Asian undergraduates?", or "What are the top 30 universities with the highest number of applicants?"</span>''', unsafe_allow_html=True)
st.markdown('''<span style="font-size: 15px;">Source: nces.ed.gov </span>''', unsafe_allow_html=True)
from pandasai.agent import Agent
from pandasai import Agent



from pandasai.llm import OpenAI
from pandasai.llm import BambooLLM




llm = BambooLLM(api_key="$2a$10$GrS2vGaJQxEpWrx4duq8AOUJ.omXTmPLHaV7rhIhAi352RtHdMCRO")

os.environ["PANDASAI_API_KEY"] = "$2a$10$GrS2vGaJQxEpWrx4duq8AOUJ.omXTmPLHaV7rhIhAi352RtHdMCRO"
os.environ.pop("PANDASAI_API_KEY", None)
sdf = SmartDataframe(df, config={"llm": llm})




#question = st.text_input('Enter question ')
#response = sdf.chat(question)


#st.write(response)







