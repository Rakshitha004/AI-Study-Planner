from llm import ask_llm

def generate_mindmap(topic: str):
    prompt = f"""
Create a simple hierarchical mindmap for the topic:
{topic}

Format like:
Topic
 - Subtopic
   - Child

Keep concise.
"""

    result = ask_llm(prompt)
    return result
