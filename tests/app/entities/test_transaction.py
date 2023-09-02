import pytest

from src.app.entities.transaction import Transaction
from src.app.enums.transaction_type_enum import ITransactionTypeEnum
from src.app.errors.entity_errors import ParamNotValidated

class Test_Transaction:
    def test_transaction(self):
        transaction = Transaction(types=ITransactionTypeEnum.deposit, value=100.0, current_balance=2000.0, timestamp=1692328190.830605)

        assert transaction.types == ITransactionTypeEnum.deposit
        assert transaction.value == 100.0
        assert transaction.current_balance == 2000.0
        assert transaction.timestamp == 1692328190.830605

    def test_types_none(self):
        with pytest.raises(ParamNotValidated):
            Transaction(value=100.0, current_balance=2000.0, timestamp=1692328190.830605)
    
    def test_types_invalid(self):
        with pytest.raises(ParamNotValidated):
            Transaction(types=True, value=100.0, current_balance=2000.0, timestamp=1692328190.830605)
    
    
    def test_value_none(self):
        with pytest.raises(ParamNotValidated):
            Transaction(types=ITransactionTypeEnum.deposit, current_balance=2000.0, timestamp=1692328190.830605)
    
    def test_value_negative(self):
        with pytest.raises(ParamNotValidated):
            Transaction(types=ITransactionTypeEnum.deposit, value= -100.0, current_balance=2000.0, timestamp=1692328190.830605)
   
    def test_value_invalid(self):
        with pytest.raises(ParamNotValidated):
            Transaction(types=ITransactionTypeEnum.deposit, value=True, current_balance=2000.0, timestamp=1692328190.830605)
    
    
    def test_current_balance_none(self):
        with pytest.raises(ParamNotValidated):
            Transaction(types=ITransactionTypeEnum.deposit, value=100.0, timestamp=1692328190.830605)
    
    def test_current_balance_invalid(self):
        with pytest.raises(ParamNotValidated):
            Transaction(types=ITransactionTypeEnum.deposit, value=100.0, current_balance=True, timestamp=1692328190.830605)
    
    def test_current_balance_negative(self):
        with pytest.raises(ParamNotValidated):
            Transaction(types=ITransactionTypeEnum.deposit, value=100.0, current_balance= -2000.0, timestamp=1692328190.830605)
    
    def test_timestamp_none(self):
        with pytest.raises(ParamNotValidated):
            Transaction(types=ITransactionTypeEnum.deposit, value=100.0, current_balance=2000.0)
    
    def test_timestamp_invalid(self):
        with pytest.raises(ParamNotValidated):
            Transaction(types=ITransactionTypeEnum.deposit, value=100.0, current_balance=2000.0, timestamp=True)
    
    def test_timestamp_negative(self):
        with pytest.raises(ParamNotValidated):
            Transaction(types=ITransactionTypeEnum.deposit, value=100.0, current_balance=2000.0, timestamp= -1692328190.830605)
    