import typing
from .client import Client

class Workspaces:
    """Typeform Workspaces API client"""

    def __init__(self, client: Client):
        """Constructor for Typeform Workspaces class"""
        self.__client = client

    def create(self, data: dict = {}) -> dict:
        """Creates a workspace"""
        return self.__client.request('post', '/workspaces', data=data)

    def delete(self, uid: str) -> str:
        """
        Deletes the workspace with the given workspace_id.
        Return a `str` based on success of deletion, `OK` on success, otherwise an error message.
        """
        return self.__client.request('delete', '/workspaces/%s' % uid)

    def get(self, uid: str) -> dict:
        """Retrieves a workspace by the given workspace_id."""
        return self.__client.request('get', '/workspaces/%s' % uid)

    def list(self, page: int = None, pageSize: int = None, search: str = None) -> dict:
        """
        Retrieve all workspaces you have access to.
        """
        return self.__client.request('get', '/workspaces', params={
            'page': page,
            'page_size': pageSize,
            'search': search
        })

    def update(self, uid: str, data: dict = {}) -> str:
        """
        Updates an existing workspace.
        Returns a `str` based on success of change, `OK` on success, otherwise an error message.
        """
        return self.__client.request('patch', '/workspaces/%s' % uid, data=data)
