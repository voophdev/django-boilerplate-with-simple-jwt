from authentication.models import Users
from authentication.interface.user_interface import UsersInterface
from typing import List, Optional

class UsersRepository(UsersInterface):

    def get_user(self, email: str, values: Optional[List[str]] = None) -> Users:
        
        if values:
            return Users.objects.filter(email=email).values(*values)
        
        return Users.objects.filter(email=email)