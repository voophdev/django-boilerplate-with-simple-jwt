from authentication.models import Users
from authentication.interface.user_interface import UsersInterface
from typing import List, Optional

class UsersService:

    def __init__(self, repository: UsersInterface):
        self.repository = repository

    def get_user(self, email: str, values: Optional[List[str]] = None) -> Users:
        return self.repository.get_user(email=email, values=values)