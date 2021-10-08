import webbrowser

import keyring
import requests
from requests.auth import HTTPBasicAuth

from ghubunix.auth.auth import Authenticator
from ghubunix.constants import GITHUB_API, GITHUB_USER_ENDPOINT
from ghubunix.models.config import Config

# Constants
PERSONAL_ACCESS_TOKEN_URL = "https://github.com/settings/tokens"
GITHUB = "github"


class PersonalAcessTokenAuthenticator(Authenticator):
    def __init__(self, username: str):
        """Create a Pesonal Access Token Authenticator

        Args:
            username(str): GitHub Username
        """
        self.username = username

    def authenticate(self) -> None:
        """Authenticate user.
        Opens the browser to create personal access token.
        Gets token from the user.
        """
        print(f"Create your personal access token at {PERSONAL_ACCESS_TOKEN_URL}.")
        print("Check GitHub's documentation for more info on Personal Access Tokens.\n")
        print("Opening github settings to create Personal Access Token in your browser")
        webbrowser.open(PERSONAL_ACCESS_TOKEN_URL)
        self.token = str(input("Enter your personal access token: "))

    def store_token(self):
        """Stores token in keyring"""
        keyring.set_password(GITHUB, self.username, self.token)

    def retrieve_token(self, in_place: bool = False):
        """Retrieve token from keyring

        Args:
            in_place(bool): Set token to the calling object
        """
        token = keyring.get_password(GITHUB, self.username)
        if in_place:
            self.token = token
        return token

    def verify(self):
        """Verify token by making a request to the GitHub User API"""
        response = requests.get(
            GITHUB_API + GITHUB_USER_ENDPOINT,
            auth=HTTPBasicAuth(self.username, self.token),
            headers={"Accept": "application/vnd.github.v3+json"},
        )
        return response.status_code == 200

    @staticmethod
    def from_config(config: Config):
        """Load authenticator from Config. Sets username and loads token from keyring

        Args:
            config(Config): Config object to load from
        """
        authenticator = PersonalAcessTokenAuthenticator(config.username)
        authenticator.retrieve_token(in_place=True)
        return authenticator

    def to_config(self, config: Config = None):
        """Update config variables and token in keyring

        Args:
            config(Config): Config object to update values in
        """
        data = {"username": self.username}
        self.store_token()
        if not config:
            return Config(**data)
        else:
            config.username = self.username
        return config
