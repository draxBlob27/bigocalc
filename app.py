import streamlit as st
from dotenv import load_dotenv, find_dotenv
import os
import openai

load_dotenv(find_dotenv())

client = openai.OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.environ.get("GROQ_API_KEY")
)


st.title("Big O Calc")

with st.form(key="my_form"):
    query = st.text_area("Enter Query", height=350)

    submit_button = st.form_submit_button(label="Run")

    SYSTEM_PROMPT = '''You are assistant of a student, who is coding. Your job is to give analysis of time and"
                    and space complexity of the code provided. Give response in detail as example below:
                    The time complexity of the given solution is O(n), where n is the number of elements in 
                    the input vector `nums`. This is because the algorithm iterates through the vector once, 
                    performing constant-time operations (finding the minimum and maximum) for each element.
                    The space complexity is O(1), as the solution uses a fixed amount of extra space regardless 
                    of the input size. 
                    It only utilizes a few integer variables (`maxDiff` and `minTillNow`) to keep track of the 
                    maximum difference and the minimum value encountered so far, without requiring any 
                    additional data structures that scale with the input size.'''
response = client.chat.completions.create(
    model= "llama-3.3-70b-versatile", 
    messages=[
        {"role":"system", "content":SYSTEM_PROMPT},
        {"role":"user", "content":query}
    ]
)

st.write(response.choices[0].message.content)