from abc import ABC, abstractmethod
from typing import List

from ..entities.transaction import Transaction


class ITransactionRepository(ABC):

    @abstractmethod
    def create_transaction(self, transaction: Transaction, transaction_id: int) -> Transaction:
        pass
    
    @abstractmethod
    def get_transaction(self, transaction_id: int):
        pass

    @abstractmethod
    def get_all_transactions(self) -> List[Transaction]:
        pass

    