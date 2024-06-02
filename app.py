import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
import json

load_dotenv()  # Load all our environment variables

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input_text):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input_text)
    return response.text

def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in range(len(reader.pages)):
        page = reader.pages[page]
        text += str(page.extract_text())
    return text

# Prompt Template
input_prompt = """
Hey Act Like a skilled or very experienced ATS (Application Tracking System)
with a deep understanding of the tech field, software engineering, data science, data analyst,
and big data engineer. Your task is to evaluate the resume based on the given job description.
You must consider the job market is very competitive and you should provide
best assistance for improving the resumes. Assign the percentage matching based
on JD and the missing keywords with high accuracy.
resume: {text}
description: {jd}

I want the response in one single string having the structure:
{{"JD Match":"%","MissingKeywords:[]","Profile Summary":""}}
"""

def format_response(response):
    # Assuming the response is a JSON string
    data = json.loads(response)
    
    formatted_response = f"""Profile Summary: 

{data["Profile Summary"]}

JD Match: {data["JD Match"]}

Missing Keywords: {data["MissingKeywords"]}
"""
    return formatted_response

# Streamlit app
st.title("JobFit Analyzer")
st.text("Improve Your Resume ATS")
jd = st.text_area("Paste the Job Description")
uploaded_file = st.file_uploader("Upload Your Resume", type="pdf", help="Please upload the pdf")

submit = st.button("Submit")

if submit:
    if uploaded_file is not None:
        resume_text = input_pdf_text(uploaded_file)
        input_data = input_prompt.format(text=resume_text, jd=jd)
        response = get_gemini_response(input_data)
        formatted_response = format_response(response)
        st.subheader("Evaluation Result")
        st.markdown(formatted_response)
    else:
        st.write("Please upload the resume")
