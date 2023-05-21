import load_keys
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.llms import OpenAI

# Load the language model we're going to use to control the agent.
llm = OpenAI(temperature=0)

# Load some tools to use.
# `llm-math` uses an LLM, so we need to pass that in.
tools = load_tools(["serpapi", "llm-math"], llm=llm)

# Finally, let's initialize an agent with the tools, the language model,
# and the type of agent we want to use.
agent_type = AgentType.ZERO_SHOT_REACT_DESCRIPTION
agent = initialize_agent(tools, llm, agent=agent_type, verbose=True)

# Now let's test it out!
question = "What was the high temperature in SF yesterday in Fahrenheit? What is that number raised to the .023 power?"
agent.run(question)
