from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
import Constants

# Use of langchain agents
def langchain_agent():
    llm = OpenAI(temperature=0.5, openai_api_key=Constants.OPENAI_API_KEY)

    tools = load_tools(["wikipedia", "llm-math"], llm=llm)

    agent = initialize_agent(
            tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
            )

    results = agent.run("What is the average age of  dog? Multiply the age by 3")
    print(results)


if __name__ == "__main__":
    langchain_agent()
    #print(generate_pet_name("cat","white"))
