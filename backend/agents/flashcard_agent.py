from llm import ask_llm

def generate_flashcards(topic):

    prompt = f"""
    Create 8 flashcards for the topic: {topic}
    Each flashcard should be:
    Question: ...
    Answer: ...

    Keep answers short and simple.
    """

    response = ask_llm(prompt)

    return response
