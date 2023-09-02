from fastapi.exceptions import HTTPException
import pytest
from src.app.entities.transaction import Transactions
from src.app.enums.transaction_type_enum import ITransactionTypeEnum

from src.app.main import get_all_transactions, get_user,deposit,withdraw


class TestMain:

        def test_get_user(self):
            response = get_user()
            
            check_response = {
                'name': 'Jão',
                'agency': '0305',
                'account': '22012-4',
                'current_balance':9000000.00
            }
            assert type(response) == dict
            assert response == check_response

        def test_get_history(self):
            response = get_all_transactions()
            assert type(response) == dict
    
        def test_deposit(self):
            dict_values={
            "2": 5,
            "5": 0,
            "10": 0,
            "20": 3,
            "50": 1,
            "100": 0,
            "200": 0,
            }        
            response = deposit(dict_values)
            assert type(response) == dict

        def test_withdraw(self):
            dict_values={
            "2": 5,
            "5": 0,
            "10": 0,
            "20": 3,
            "50": 1,
            "100": 0,
            "200": 0,
        }  
        response = withdraw(dict_values)

        assert type(response) == dict