from pydantic import BaseModel


class Config(BaseModel):
    """Data model for Config"""

    username: str
