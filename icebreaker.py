import os

import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai.chat_models import ChatOpenAI

if __name__ == "__main__":
    load_dotenv()
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    st.header("Prompt Summary Application...")

    summary = """
    M.S. Dhoni: The Untold Story is a 2016 Indian Hindi-language biographical sports drama film directed and co-written by Neeraj Pandey. It is based on the life of former Test, ODI and T20I captain of the Indian national cricket team, Mahendra Singh Dhoni. The film stars the late Sushant Singh Rajput as MS Dhoni, along with Disha Patani, Kiara Advani, and Anupam Kher. The film chronicles the life of Dhoni from a young age through a series of life events.
The idea of the biopic was put forward by Dhoni's manager, Arun Pandey, after encountering an incident at an airport after the 2011 Cricket World Cup Final. Development began two years later, with the consent of Dhoni. Neeraj Pandey was later approached to helm the film while he was working on Baby. Pandey recruited a number of people for researching into Dhoni's background and his life events. Dhoni eventually became a consultant on the film.
    """

    summary_template = """
     Given the summary {summary} of the person. Please generate the overall achievements in his or her lifetime.
    """

    prompt_template = PromptTemplate(input_variables=["summary"], template=summary_template)
    llm = ChatOpenAI(temperature=0, model="gpt-4.1-mini")
    # llm = ChatOllama(model="llama3")

    chain = prompt_template | llm
    response = chain.invoke(input={"summary": summary})
    st.write(response.text())
