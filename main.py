from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage, AIMessage

openai_api_key = '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'

chat = ChatOpenAI(temperature=.7, openai_api_key=openai_api_key)

prompt = """
Today is Monday, tomorrow is Wednesday.

What is wrong with that statement?
"""

print(chat(
    [
        SystemMessage(content="You are a nice AI bot that helps a user figure out what to eat in one short sentence"),
        HumanMessage(content="I like tomatoes, what should I eat?")
    ]
))
