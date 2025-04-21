import os

import requests
from dotenv import load_dotenv


class LinkedInAPI:
    def __init__(self):
        self.api_key = os.getenv("LINKEDIN_API_KEY")
        self.profile_url = os.getenv("LINKEDIN_PROFILE_URL")
        self.api_endpoint = os.getenv("LINKEDIN_API_ENDPOINT")
        self.mock_profile_url = os.getenv("LINKEDIN_MOCK_PROFILE_URL")

    def get_user_profile(self, mock):
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }

        if mock:
            response = requests.get(
                self.mock_profile_url,
                headers=headers,
                timeout=10
            )
        else:
            params = {
                'apikey': self.api_key,
                'linkedInUrl': self.profile_url,
            }
            response = requests.get(
                self.api_endpoint,
                params=params,
                headers=headers,
                timeout=10
            )

        if response.status_code == 200:
            # fetch person from json
            return response.json().get('person')
        else:
            raise Exception(f"Error fetching profile: {response.status_code} - {response.text}")


if __name__ == "__main__":
    # load environment variables from .env file
    load_dotenv()
    # create an instance of LinkedInAPI
    linkedin_api = LinkedInAPI()

    try:
        profile_info = linkedin_api.get_user_profile(mock=True)
        print(profile_info)
    except Exception as e:
        print(e)
