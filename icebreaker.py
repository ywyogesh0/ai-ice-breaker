import os

import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai.chat_models import ChatOpenAI

from third_party_source.linkedin import LinkedInAPI

if __name__ == "__main__":
    load_dotenv()
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    st.header("LinkedIn Profile...")

    # get the profile from LinkedIn
    linkedin_api = LinkedInAPI()
    profile = linkedin_api.get_user_profile(mock=False)

    profile_template = """
     Given the profile {profile} of the person. Please generate the overall summary.
    """

    prompt_template = PromptTemplate(input_variables=["profile"], template=profile_template)
    llm = ChatOpenAI(temperature=0, model="gpt-4.1-mini")
    # llm = ChatOllama(model="llama3")

    chain = prompt_template | llm
    response = chain.invoke(input={"profile": profile})
    st.write(response.text())
