import streamlit as st
from google import genai
from dotenv import load_dotenv
import os

# Load API key from .env
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

# Create Gemini client
client = genai.Client(api_key=API_KEY)

# Page configuration
st.set_page_config(
    page_title="PATH SUTHRA",
    page_icon="🎓",
    layout="wide"
)

# Title
st.title("🎓 PATH SUTHRA")
st.subheader("AI Career Path Finder for Students")

st.write(
    "Discover suitable career paths based on your skills, "
    "interests and career goals."
)

st.divider()

# Student details
st.header("👨‍🎓 Student Profile")

name = st.text_input("Enter your name")

branch = st.selectbox(
    "Select your branch",
    ["CSE", "IT", "ECE", "EEE", "Mechanical", "Civil"]
)

year = st.selectbox(
    "Year of Study",
    ["1st Year", "2nd Year", "3rd Year", "4th Year"]
)

skills = st.text_area(
    "Enter your skills",
    placeholder="Example: Python, C, SQL, HTML"
)

interests = st.text_area(
    "Enter your interests",
    placeholder="Example: AI, Machine Learning, Web Development"
)

goal = st.text_input(
    "What is your career goal?",
    placeholder="Example: I want to become an AI Engineer"
)

# Career analysis
if st.button("🔍 Find My Career Path"):

    if not name or not skills or not interests:
        st.warning("Please fill in your name, skills and interests.")

    elif not API_KEY:
        st.error("Gemini API key not found. Please check your .env file.")

    else:

        prompt = f"""
You are PATH SUTHRA, an AI career mentor for students.

Analyze the following student profile:

Student Name: {name}
Branch: {branch}
Year: {year}
Skills: {skills}
Interests: {interests}
Career Goal: {goal}

Provide the response in a simple and student-friendly format.

Give:

1. Top 3 suitable career paths
2. Career match explanation
3. Why each career is suitable
4. Existing skills
5. Missing skills / skill gaps
6. Step-by-step learning roadmap
7. Recommended projects
8. Internship preparation
9. Placement preparation
10. Final personalized advice

Be realistic and do not guarantee employment.
"""

        try:

            with st.spinner(
                "🤖 PATH SUTHRA is analyzing your profile..."
            ):

                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=prompt
                )

            st.success("Career analysis completed!")

            st.subheader("🎯 Your Personalized Career Path")

            st.write(response.text)

        except Exception as e:

            st.error("Something went wrong while connecting to Gemini.")

            st.write(str(e)) 