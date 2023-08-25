import pytest

from src.app.entities.transaction import Transaction
from src.app.enums.transaction_type_enum import TransactionType
from src.app.errors.entity_errors import ParamNotValidated

class Test_Transaction:
    def test_transaction(self):
        transaction = Transaction(types=TransactionType.deposit, value=100.0, current_balance=2000.0, timestamp=1692328190.830605)

        assert transaction.types == TransactionType.deposit
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
            Transaction(types=TransactionType.deposit, current_balance=2000.0, timestamp=1692328190.830605)
    
    def test_value_negative(self):
        with pytest.raises(ParamNotValidated):
            Transaction(types=TransactionType.deposit, value= -100.0, current_balance=2000.0, timestamp=1692328190.830605)
   
    def test_value_invalid(self):
        with pytest.raises(ParamNotValidated):
            Transaction(types=TransactionType.deposit, value=True, current_balance=2000.0, timestamp=1692328190.830605)
    
    
    def test_current_balance_none(self):
        with pytest.raises(ParamNotValidated):
            Transaction(types=TransactionType.deposit, value=100.0, timestamp=1692328190.830605)
    
    def test_current_balance_invalid(self):
        with pytest.raises(ParamNotValidated):
            Transaction(types=TransactionType.deposit, value=100.0, current_balance=True, timestamp=1692328190.830605)
    
    def test_current_balance_negative(self):
        with pytest.raises(ParamNotValidated):
            Transaction(types=TransactionType.deposit, value=100.0, current_balance= -2000.0, timestamp=1692328190.830605)
    
    # def test_current_balance_lowerthandeposit(self):
    #     with pytest.raises(ParamNotValidated):
    #         Transaction(types=TransactionType.deposit, value=600.0, current_balance= 250.0, timestamp=1692328190.830605)
            
    def test_timestamp_none(self):
        with pytest.raises(ParamNotValidated):
            Transaction(types=TransactionType.deposit, value=100.0, current_balance=2000.0)
    
    def test_timestamp_invalid(self):
        with pytest.raises(ParamNotValidated):
            Transaction(types=TransactionType.deposit, value=100.0, current_balance=2000.0, timestamp=True)
    
    def test_timestamp_negative(self):
        with pytest.raises(ParamNotValidated):
            Transaction(types=TransactionType.deposit, value=100.0, current_balance=2000.0, timestamp= -1692328190.830605)
    