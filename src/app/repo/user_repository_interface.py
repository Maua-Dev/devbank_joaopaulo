from abc import ABC, abstractmethod
from typing import List, Optional, Tuple
from ..entities.user import User


class IUserRepository(ABC):
    
    
    @abstractmethod
    def get_user(self) -> User:
        pass
    
    @abstractmethod 
    def deposit_current_balance(self, current_balance:float) ->float:
        pass
    
    @abstractmethod
    def withdraw_current_balance(self, current_balance:float) ->float:
        pass