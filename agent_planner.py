def plan_agent(user_input):
    # Very simple logic for MVP; later we can use GPT
    if "chatbot" in user_input.lower():
        agent_type = "LLM-based Chatbot"
        tools = ["OpenAI API", "LangChain"]
    elif "classify" in user_input.lower():
        agent_type = "ML Classifier"
        tools = ["scikit-learn", "pandas"]
    else:
        agent_type = "Rule-based Agent"
        tools = ["Python only"]

    return {
        "agent_type": agent_type,
        "recommended_tools": tools,
        "description": user_input
    }
