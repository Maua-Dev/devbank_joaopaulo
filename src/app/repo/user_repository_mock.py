from typing import Dict
from ..entities.user import User


class UserRepositoryMock(IUserRepository):
    users: Dict[int, User]

    def __init__(self):
        self.users = {
            1: User(name="Jão", agency="0000", account="00000-0", current_balance=10000000000000000000000000.0),
            2: User(name="Vitor", agency="0000", account="00000-0", current_balance=560.7),
            3: User(name="Nicão", agency="0000", account="00000-0", current_balance=22.17),
            4: User(name="Lucas Milas", agency="0000", account="00000-0", current_balance=10.5)
        }

    # def deposit(self,)