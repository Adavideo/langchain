import load_keys
from langchain.chat_models import ChatOpenAI
from langchain import LLMChain
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

chat = ChatOpenAI(temperature=0)

template = "You are a helpful assistant that translates {input_language} to {output_language}."
system_message_prompt = SystemMessagePromptTemplate.from_template(template)
human_template = "{text}"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

# get a chat completion from the formatted messages
#x = chat_prompt.format_prompt(input_language="English", output_language="Spanish", text="I love programming.")
#result = chat(x.to_messages())

chain = LLMChain(llm=chat, prompt=chat_prompt)
result = chain.run(input_language="English", output_language="Spanish", text="I love programming.")

print(result)
