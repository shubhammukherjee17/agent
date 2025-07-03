def generate_code(plan):
    agent_type = plan["agent_type"]
    if agent_type == "ML Classifier":
        code = f'''
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Example dataset
data = pd.read_csv("data.csv")
X = data["text"]
y = data["label"]

# TODO: Add feature extraction here

model = LogisticRegression()
# model.fit(...)
print("Classifier created!")
'''
    else:
        code = "# Placeholder for other agent types"

    return {
        "main.py": code,
        "requirements.txt": "\n".join(plan["recommended_tools"]),
        "README.md": f"# {plan['agent_type']}\n\n{plan['description']}"
    }
