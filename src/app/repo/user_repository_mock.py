from typing import Dict, Optional, List
from ..entities.user import User
from .user_repository_interface import IUserRepository


class ItemRepositoryMock(IUserRepository):
    
    def __init__(self):
        self.user = User(name="Jony", agency="0305", account="22012-4", current_balance= 9000000.00)
        
    def get_user(self) -> User:
        return self.user

    def withdraw_current_balance(self, current_balance: float) -> float:
        self.user.current_balance -= current_balance
        return self.user.current_balance    
    
    def deposit_current_balance(self, current_balance: float) -> float: 
        self.user.current_balance += current_balance
        return self.user.current_balance   