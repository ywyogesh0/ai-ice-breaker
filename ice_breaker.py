from langchain_core.prompts import PromptTemplate
from langchain_openai.chat_models import ChatOpenAI

from agents.linkedin_lookup_agent import lookup_linkedin_profile_url
from output_parsers.linkedin_profile_output_parser import profile_parser, LinkedInProfileOutputParser
from third_party_sources.linkedin_scrapin import LinkedInScrapInAPI


def generate_linkedin_profile_information(user_text: str) -> LinkedInProfileOutputParser:
    """
    Generate LinkedIn profile information based on user input.
    """

    # lookup LinkedIn profile URL
    linkedin_profile_url = lookup_linkedin_profile_url(user_text)

    # get the profile from LinkedInScrapInAPI
    linkedin_scrapin_api = LinkedInScrapInAPI()
    profile = linkedin_scrapin_api.get_user_profile(url=linkedin_profile_url, mock=False)

    profile_template = """
        Given the profile {profile} of the person. Please generate the below features:
        1. The public profile URL.
        2. The public profile picture URL.
        3. The name of the profile.
        4. The location of the profile.
        5. A short summary of the profile.
        6. The current job of the profile.
        7. The current company of the profile.
        8. The two interesting facts.
        9. The two core skills.
        10. The two companies with overall years work experience.
        11. The two certifications.
        
        {format_instructions}
       """

    prompt_template = PromptTemplate(
        input_variables=["profile"],
        template=profile_template,
        partial_variables={"format_instructions": profile_parser.get_format_instructions()},
    )
    llm = ChatOpenAI(temperature=0, model="gpt-4.1-mini")
    # llm = ChatOllama(model="llama3")

    chain = prompt_template | llm | profile_parser
    response = chain.invoke(input={"profile": profile})

    return response
