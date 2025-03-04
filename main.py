# source chatbot/bin/activate
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

    # string that holds AI LLM preset
template = """
    Answer the question below:
    Here is the conversation history: {content}

    Question: {question}

    Answer:
"""

model = OllamaLLM(model="llama3")                   #how we detirmine what local LLM we use
prompt = ChatPromptTemplate.from_template(template) #this is a method?
chain = prompt|model

def handle_convo():
    content = ""
    print("Welcome to the Glebgamer AI ChatBot, type 'exit' to quit")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        result = chain.invoke({"content": content, "question": user_input})
        print("Glebgamers Robot: ", result)
        content += f"\n User: {user_input}\nAI: {result}"

if __name__ == "__main__":
    handle_convo()