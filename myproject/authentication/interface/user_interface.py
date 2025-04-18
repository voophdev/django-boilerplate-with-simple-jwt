from abc import abstractmethod, ABC
from authentication.models import Users
from typing import List, Optional

class UsersInterface(ABC):

    @abstractmethod
    def get_user(email: str, values: Optional[List[str]] = None) -> Users:
        pass