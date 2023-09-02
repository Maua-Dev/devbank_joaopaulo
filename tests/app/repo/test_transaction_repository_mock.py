import pytest
from src.app.entities.transaction import Transactions
from src.app.enums.transaction_type_enum import ITransactionTypeEnum
from src.app.repo.transaction_repository_mock import TransactionRepositoryMock


class Test_TransactionsRepositoryMock:
    def test_get_all_transactions(self):
        repo = TransactionRepositoryMock()

        transactions = repo.get_all_transactions()

        updated_transactions = repo.transactions

        assert transactions == updated_transactions
    
    def test_create_transaction(self):
        repo = TransactionRepositoryMock()

        transaction = repo.create_transaction(
            Transactions(
                type_transaction= ITransactionTypeEnum.DEPOSIT,    
                value=1000.00,
                current_balance=2000.00,
                timestamp=1917577200.00
            )
        )
        if len(repo.transactions) > 0:
            assert transaction == repo.transactions[len(repo.transactions) - 1]
        else:
            assert transaction == repo.transactions[0]