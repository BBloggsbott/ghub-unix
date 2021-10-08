from abc import ABC, abstractclassmethod

from ghubunix.models.config import Config


class Authenticator(ABC):
    """Abstract class for Authenticators"""

    @abstractclassmethod
    def authenticate(self):
        """Perform authentication"""
        pass

    @abstractclassmethod
    def store_token(self):
        """Store Authentication tokens"""
        pass

    @abstractclassmethod
    def retrieve_token(self):
        """Retrieve stored tokens"""
        pass

    @staticmethod
    @abstractclassmethod
    def from_config(config: Config):
        """Load authenticator from config"""
        pass

    @abstractclassmethod
    def to_config(self, config: Config):
        pass

    @abstractclassmethod
    def verify(self):
        """Verify Authentication"""
        pass
