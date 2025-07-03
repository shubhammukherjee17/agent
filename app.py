import streamlit as st
from agent_planner import plan_agent
from code_generator import generate_code

st.set_page_config(page_title="Meta-AI Agent Builder", layout="centered")
st.title("🧠 Build Your Own AI Agent")

user_input = st.text_area("Describe the AI agent you want to build:", height=150)

if st.button("Build Agent"):
    with st.spinner("Planning your AI agent..."):
        plan = plan_agent(user_input)
        st.subheader("🛠 Suggested Plan")
        st.json(plan)

        st.subheader("📄 Generated Code")
        code_files = generate_code(plan)
        for filename, content in code_files.items():
            st.code(content, language="python")
