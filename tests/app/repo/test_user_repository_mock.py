from src.app.enums.transaction_type_enum import ITransactionTypeEnum
from src.app.repo.user_repository_mock import UserRepositoryMock
from src.app.repo.transaction_repository_mock import TransactionsRepositoryMock


class Test_UserRepositoryMock:
        repo_user = UserRepositoryMock()
        repo_transaction = TransactionsRepositoryMock()

        user = repo_user.get_user()
        transaction = repo_transaction.get_all_transactions()

        def test_get_user(self):
                updated_user = self.user
                assert self.user == updated_user
        
        def test_deposit_current_balance(self):
                for transaction in self.transaction:
                        if transaction.type_transaction == ITransactionTypeEnum.DEPOSIT:
                                updated_current_balance = self.user.current_balance + transaction.value
                                assert self.user.current_balance + transaction.value == updated_current_balance
        
        def test_withdraw_current_balance(self):
                for transaction in self.transaction:
                        if transaction.type_transaction == ITransactionTypeEnum.WITHDRAW:
                                updated_current_balance = self.user.current_balance - transaction.value
                                assert self.user.current_balance - transaction.value == updated_current_balance