import os

import requests
from dotenv import load_dotenv


class LinkedInScrapInAPI:
    def __init__(self):
        self.api_key = os.getenv("LINKEDIN_SCRAPIN_API_KEY")
        self.api_endpoint = os.getenv("LINKEDIN_SCRAPIN_API_ENDPOINT")
        self.mock_profile_url = os.getenv("LINKEDIN_SCRAPIN_MOCK_PROFILE_URL")

    def get_user_profile(self, url: str = None, mock: bool = False):
        """
        Fetches the LinkedIn profile information using the LinkedIn Scrapin API.
        :param url: The LinkedIn profile URL to fetch. If None, a mock profile is fetched.
        :param mock: If True, fetches a mock profile. If False, fetches the actual profile.
        """

        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }

        if mock:
            response = requests.get(
                url=self.mock_profile_url,
                headers=headers,
                timeout=10
            )
        else:
            params = {
                'apikey': self.api_key,
                'linkedInUrl': url,
            }
            response = requests.get(
                url=self.api_endpoint,
                params=params,
                headers=headers,
                timeout=10
            )

        if response.status_code == 200:
            # fetch person from json
            return response.json().get('person')
        else:
            # raise an exception if the request was unsuccessful
            raise Exception(f"Error fetching profile: {response.status_code} - {response.text}")


if __name__ == "__main__":
    # load environment variables from .env file
    load_dotenv()

    # create an instance of LinkedInScrapInAPI
    linkedin_scrapin_api = LinkedInScrapInAPI()

    try:
        profile_info = linkedin_scrapin_api.get_user_profile(mock=True)
        print(profile_info)
    except Exception as e:
        print(e)
