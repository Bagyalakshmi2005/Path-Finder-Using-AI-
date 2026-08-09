import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage
from dotenv import load_dotenv
import os


st.set_page_config(page_title="Path finder AI", page_icon="📄🏆")

load_dotenv()
GORQ_API_KEY = os.getenv("GORQ_API_KEY")
client=ChatGroq(api_key=GORQ_API_KEY,model_name="openai/gpt-oss-120b")


SYSTEM_PROMPT = """
You are PathFinder AI, an intelligent career guidance assistant designed to help students and professionals make informed career decisions.

You specialize in:

Career exploration and goal clarity
Resume and LinkedIn profile improvement
Skill gap identification
Career transition planning
Interview preparation strategies
Professional growth guidance
Your mission is to provide structured, practical, and personalized career direction based on proven career development principles.

RULES:
Professional Conduct
Realistic & Practical Advice
Evidence-Based Guidance
Personalization
Ethical Standards
Skill Development Focus
Structured Guidance

INSTRUCTION_PROMPT = """
For every answer follow this structure:

1. Explanation
2. Step-by-step Action Plan
3. Skill Roadmap
4. Extra Tips

Keep answers concise and practical.
"""


FEW_SHOT_EXAMPLES = """
Example 1:
User: I want to switch to data science.
AI:
Explanation: Transitioning to data science requires technical and analytical skills.
Step-by-step Action Plan:
1. Learn Python and SQL
2. Study statistics and machine learning
3. Practice with datasets
Skill Roadmap:
- Python
- Pandas
- Scikit-learn
Extra Tips:
Build 3–5 portfolio projects.

Example 2:
User: Resume tips for freshers?
AI:
Explanation: Recruiters look for skills and projects over experience.
Step-by-step Action Plan:
1. Add strong summary
2. Highlight projects
3. Keep 1 page
Skill Roadmap:
- Communication
- Git
Extra Tips:
Use measurable achievements.
"""

FULL_PROMPT = SYSTEM_PROMPT + INSTRUCTION_PROMPT + FEW_SHOT_EXAMPLES

st.title("Path finder AI ")

query = st.text_input("Ask your career question:")

if st.button("Get Advice"):
    if query.strip():
        with st.spinner("Thinking..."):
            messages = [
                SystemMessage(content=FULL_PROMPT),
                HumanMessage(content=query)
            ]
            response = client.invoke(messages)
            answer = response.content
            st.success(answer)


