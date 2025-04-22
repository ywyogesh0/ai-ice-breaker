from dotenv import load_dotenv
from langchain_community.tools.tavily_search import TavilySearchResults

load_dotenv()


def search_linkedin_profile_url(input_text: str):
    """
    Search for the LinkedIn profile URL from the given input_text.
    """

    tavily_search = TavilySearchResults()
    search_result = tavily_search.run(tool_input=f"{input_text}")
    return search_result


if __name__ == "__main__":
    text = "Yogesh Walia living in London & Working at Publicis Sapient as a Manager Data Engineer"
    result = search_linkedin_profile_url(text)
    print(result)
