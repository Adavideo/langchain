import load_keys
from langchain import OpenAI, ConversationChain

llm = OpenAI(temperature=0)
conversation = ConversationChain(llm=llm, verbose=True)

user_input = "."
while user_input !="":
    user_input=input("user: ")
    output = conversation.predict(input=user_input)
    print(output)
