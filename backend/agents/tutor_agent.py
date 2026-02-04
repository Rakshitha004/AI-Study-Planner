from llm import ask_llm

def solve_doubt(question):
    prompt = f"""
Explain the following question in simple words for a Class 8 student:

{question}
"""
    return ask_llm(prompt)


def generate_practice_questions(topic):
    prompt = f"""
Generate 10 practice questions for Class 8.

Topic: {topic}
"""
    return ask_llm(prompt)


def summarize_text(text):
    prompt = f"""
Summarize this content for quick revision:

{text}
"""
    return ask_llm(prompt)
