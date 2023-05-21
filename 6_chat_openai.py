import load_keys
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

chat = ChatOpenAI(temperature=0, verbose=True)

'''
# Un solo mensaje
result = chat([HumanMessage(content="Translate this sentence from English to Spanish. I love programming.")])
print(result)

# Varios mensajes
messages = [
    SystemMessage(content="You are a helpful assistant that translates English to Spanish."),
    HumanMessage(content="I love programming.")
]
result = chat(messages)
print(result)
'''

# Dos tandas de mensajes.
batch_messages = [
    [
        SystemMessage(content="You are a helpful assistant that translates English to Spanish."),
        HumanMessage(content="I love programming.")
    ],
    [
        SystemMessage(content="You are a helpful assistant that translates English to Spanish."),
        HumanMessage(content="I love artificial intelligence.")
    ],
]
result = chat.generate(batch_messages)
tokens = result.llm_output['token_usage']
print(tokens)
print("_____")
print(result)
