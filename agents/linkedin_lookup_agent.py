import streamlit as st
from dotenv import load_dotenv
from langchain import hub
from langchain.agents import create_react_agent, AgentExecutor
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool
from langchain_openai.chat_models import ChatOpenAI

import lookup_tool

load_dotenv()

st.header("LinkedIn Profile Lookup Agent")


def lookup_linkedin_profile_url(input_text: str) -> str:
    """
    Lookup the LinkedIn profile URL from the given input_text.
    """

    # create llm instance
    llm = ChatOpenAI(temperature=0, model="gpt-4.1-mini")

    # agent_tools for agent
    tools_for_agent = [
        Tool(
            name="search_linkedin_profile_url",
            description="Search the LinkedIn profile URL from the given input text.",
            func=lookup_tool.search_linkedin_profile_url
        )
    ]

    # create input prompt template
    input_prompt_template = """
    You are a LinkedIn profile lookup agent. Your task is to find the LinkedIn profile URL from the given text {text}.
    Only return the LinkedIn profile URL. If you cannot find the LinkedIn profile URL, return "No LinkedIn profile found".
    """

    # create input prompt template instance
    input_prompt_template_instance = PromptTemplate(input_variables=["text"], template=input_prompt_template)

    # create react prompt template for agent
    react_prompt_template = hub.pull("hwchase17/react")

    # create agent
    agent = create_react_agent(
        llm=llm,
        tools=tools_for_agent,
        prompt=react_prompt_template
    )

    # create agent executor
    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools_for_agent,
        verbose=True
    )

    # run agent executor
    result = agent_executor.invoke(
        input={"input": input_prompt_template_instance.format(text=input_text)}
    )

    return result["output"]


# Streamlit app to get LinkedIn profile URL
if __name__ == "__main__":
    # get text from user
    user_text = st.text_input("Enter the text to lookup LinkedIn profile URL:")

    if user_text:
        # lookup LinkedIn profile URL
        linkedin_profile_url = lookup_linkedin_profile_url(user_text)
        st.write(f"LinkedIn Profile URL: {linkedin_profile_url}")
