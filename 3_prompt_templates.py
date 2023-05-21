from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain

prompt = PromptTemplate(
    input_variables=["product"],
    template="What is a good name for a company that makes {product}?",
)

llm = OpenAI(temperature=0.9)
chain = LLMChain(llm=llm, prompt=prompt)

respuesta = chain.run("colorful socks")
print(respuesta)
