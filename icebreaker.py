import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai.chat_models import ChatOpenAI

from agents.linkedin_lookup_agent import lookup_linkedin_profile_url
from third_party_sources.linkedin_scrapin import LinkedInScrapInAPI


def generate_summary(user_text: str):
    """
    Generate a summary of the LinkedIn profile based on the user input text.
    """

    # lookup LinkedIn profile URL
    linkedin_profile_url = lookup_linkedin_profile_url(user_text)

    # get the profile from LinkedInScrapInAPI
    linkedin_scrapin_api = LinkedInScrapInAPI()
    profile = linkedin_scrapin_api.get_user_profile(url=linkedin_profile_url, mock=False)

    profile_template = """
        Given the profile {profile} of the person. Please generate the overall summary.
       """

    prompt_template = PromptTemplate(input_variables=["profile"], template=profile_template)
    llm = ChatOpenAI(temperature=0, model="gpt-4.1-mini")
    # llm = ChatOllama(model="llama3")

    chain = prompt_template | llm
    response = chain.invoke(input={"profile": profile})

    return response.text()


if __name__ == "__main__":
    load_dotenv()
    st.header("LinkedIn Profile Summary...")

    # get text from user
    input_text = st.text_input("Enter the text to generate LinkedIn profile Summary:")

    if input_text:
        # generate LinkedIn profile summary
        summary = generate_summary(input_text)
        # display the summary
        st.write(f"Summary: {summary}")
