from typing import Dict, List

from src.app.repo.transaction_repository_interface import ITransactionRepository


from ..entities.transaction import Transaction


class TransactionRepositoryMock(ITransactionRepository):
    transactions: Dict[int, Transaction]

    def __init__(self):
        self.transactions = {
            1: Transaction(types=TransactionType.deposit, value=100.0, current_balance=20200.0, timestamp=5692328190.830605),
            2: Transaction(types=TransactionType.withdraw, value=200.0, current_balance=500000.0, timestamp=3692328190.830605),
            3: Transaction(types=TransactionType.deposit, value=2500.0, current_balance=7050.0, timestamp=2692328190.830605),
            4: Transaction(types=TransactionType.deposit, value=20.0, current_balance=7850.0, timestamp=14695628190.830605),
            5: Transaction(types=TransactionType.withdraw, value=2.0, current_balance=66950.0, timestamp=1692357190.830605),
            6: Transaction(types=TransactionType.deposit, value=2000.0, current_balance=53340.0, timestamp=25672328190.830605),
            7: Transaction(types=TransactionType.deposit, value=2000.0, current_balance=4500.0, timestamp=36978628190.830605),
            8: Transaction(types=TransactionType.withdraw, value=2000.0, current_balance=54440.0, timestamp=76967828190.830605),
            9: Transaction(types=TransactionType.deposit, value=2000.0, current_balance=58940.0, timestamp=669238779190.830605)
        }

    def create_transaction(self, transaction: Transaction, transaction_id: int):
        self.transactions[transaction_id] = transaction
        return transaction

    def get_transaction(self, transaction_id: int):
        return self.transactions.get(transaction_id, None)

    def get_all_transactions(self) -> List[Transaction]:
        return self.transactions.values()

    












