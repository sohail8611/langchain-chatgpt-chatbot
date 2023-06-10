
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate, SystemMessagePromptTemplate, AIMessagePromptTemplate, HumanMessagePromptTemplate

from langchain.schema import AIMessage,HumanMessage,SystemMessage

chat = ChatOpenAI(temperature=0,model='gpt-3.5-turbo')

messages = [
    SystemMessage(content="You are a helpful assistant"),
]

while True:
    user_input = input("you: ")
    messages.append(HumanMessage(content=user_input))
    ai_response = chat(messages=messages).content
    print("ai: ",ai_response)
    messages.append(AIMessage(content=ai_response))

