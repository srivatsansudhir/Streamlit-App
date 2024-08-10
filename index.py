import pandas as pd
import zipfile
import os
import streamlit as st
from pandasai import SmartDataframe

#from pandasai import PandasAI
#from pandasi.llm.openai import OpenAI


zip_file_path = 'CSV_5262024-602.zip'
csv_file_name = 'CSV_5262024-602.csv'


with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extract(csv_file_name)


extracted_csv_path = csv_file_name 


df = pd.read_csv(extracted_csv_path)




st.markdown('''<span style="font-size: 36px;">University Chat Bot</span>''', unsafe_allow_html=True)
st.markdown('''<span style="font-size: 15px;">This is a chat bot that answers questions based on data of 150 top American universities. Try asking "What are the 5 universities with the lowest acceptance rates?"</span>''', unsafe_allow_html=True)
st.markdown('''<span style="font-size: 15px;">Source: nces.ed.gov </span>''', unsafe_allow_html=True)
from pandasai.agent import Agent
from pandasai import Agent



from pandasai.llm import OpenAI
from pandasai.llm import BambooLLM


#llm = OpenAI(api_token='sk-QHqf5RW7K55XqwZefSo9sSIE53MRnAOFj__GvE9g_VT3BlbkFJbDWVqV_KPONoV-EuhLlBlZmlKMYffqbNSSYHvkmegA')
pandas_ai = PandasAI(llm, verbose=True, conversational=False)
llm = BambooLLM(api_key="$2a$10$Dot0CPMnrRHpQsODdO4FkeIwS59gRzLmepKGLiQAn19soUXbO0f0K")

os.environ["PANDASAI_API_KEY"] = "$2a$10$Dot0CPMnrRHpQsODdO4FkeIwS59gRzLmepKGLiQAn19soUXbO0f0K"
os.environ.pop("PANDASAI_API_KEY", None)
sdf = SmartDataframe(df, config={"llm": llm})




question = st.text_input('Enter question ')
response = sdf.chat(question)
#response = pandas_ai(sdf, question)
st.write(response)







