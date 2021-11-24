import typing
from .client import Client

class Workspaces:
    """Typeform Workspaces API client"""

    def __init__(self, client: Client):
        """Constructor for Typeform Workspaces class"""
        self.__client = client

    def list(self, page: int = None, pageSize: int = None, search: str = None) -> dict:
        """
        Retrieve all workspaces you have access to.
        """
        return self.__client.request('get', '/workspaces', params={
            'page': page,
            'page_size': pageSize,
            'search': search
        })
