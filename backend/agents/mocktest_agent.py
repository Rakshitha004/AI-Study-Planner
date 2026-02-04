from llm import ask_llm

def generate_mock_test(topic):

    prompt = f"""
    Create 5 multiple choice questions for the topic: {topic}

    Format:
    Q1: question
    A) option
    B) option
    C) option
    D) option
    Answer: A
    """

    return ask_llm(prompt)
