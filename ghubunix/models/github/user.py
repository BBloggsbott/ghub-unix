from pydantic import BaseModel


class Plan(BaseModel):
    name: str
    space: int
    private_repos: int
    collaborators: int


class User(BaseModel):
    """Response model for GitHub's user API"""

    login: str
    id: int
    node_id: str
    avatar_url: str
    gravatar_id: str
    url: str
    html_url: str
    followers_url: str
    following_url: str
    gists_url: str
    starred_url: str
    subscriptions_url: str
    organizations_url: str
    repors_url: str
    events_url: str
    received_events_url: str
    trype: str
    site_admin: bool
    name: str
    company: str
    blog: str
    location: str
    email: str
    hireable: bool
    bio: str
    twitter_username: str
    public_repos: int
    public_gists: int
    followers: int
    following: int
    created_at: str
    updated_at: str
    private_gists: int
    total_private_repos: int
    owned_private_repos: int
    disk_usage: int
    collaborators: int
    two_factor_authentication: bool
    plan: Plan
