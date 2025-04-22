from typing import List

from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field


class LinkedInProfileOutputParser(BaseModel):
    """
    Output parser for LinkedIn profile data.
    """

    profile_url: str = Field(description="The LinkedIn profile URL.")
    profile_picture_url: str = Field(description="The profile picture URL of the LinkedIn profile.")
    name: str = Field(description="The name of the LinkedIn profile.")
    location: str = Field(description="The location of the LinkedIn profile.")
    short_summary: str = Field(description="The short summary of the LinkedIn profile.")
    current_job: str = Field(description="The current job of the LinkedIn profile.")
    current_company: str = Field(description="The current company of the LinkedIn profile.")
    facts: List[str] = Field(description="Two interesting facts of the LinkedIn profile.")
    skills: List[str] = Field(description="Two core skills of the LinkedIn profile.")
    experience: List[str] = Field(description="Two Companies with overall years experience of the LinkedIn profile.")
    certifications: List[str] = Field(description="Two certifications of the LinkedIn profile.")


profile_parser = PydanticOutputParser(pydantic_object=LinkedInProfileOutputParser)
