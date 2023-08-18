from typing import Tuple
import datetime

from ..errors.entity_errors import ParamNotValidated
from ..enums.transaction_type_enum import TransactionType


class Transaction:
    types: TransactionType
    value: float
    current_balance: float
    timestamp: float

    def __init__(self, types=TransactionType, value=float, current_balance=float, timestamp=float):

        validation_types = self.validate_type(types)
        if validation_types [0] is False:
            raise ParamNotValidated("types", validation_types[1])
        self.types = types 

        validation_value = self.validate_value(value)
        if validation_value[0] is False:
            raise ParamNotValidated("value", validation_value[1])
        self.value = value

        validation_current_balance = self.validate_current_balance(current_balance)
        if validation_current_balance[0] is False:
            raise ParamNotValidated("current_balance", validation_current_balance[1])
        self.current_balance = current_balance

        validation_timestamp = self.validate_timestamp(timestamp)
        if validation_timestamp[0] is False:
            raise ParamNotValidated("timestamp", validation_timestamp[1])
        self.timestamp = timestamp

    @staticmethod
    def validate_type(types: TransactionType) -> Tuple[bool, str]:
        if types is None:
            return (False, "Type is required")
        if type(types) != TransactionType:
            return (False, "Type must be a ENUM")
        # if types == TransactionType.withdraw:
        #     if value > current_balance:
        #         return (False, "Value can't be greater than current_balance")
        #     elif value < current_balance:
        #         return (True, "")
        # if types == TransactionType.deposit:
        #     if value >= 2*current_balance:
        #         return (False, "suspicious deposit")
        #     elif value < 2*current_balance:
        #         return (True, "")
        return (True, "")

    @staticmethod
    def validate_value(value: float) -> Tuple[bool, str]:
        if value is None:
            return (False, "Value is required")
        if type(value) != float:
            return (False, "Value must be a float")
        if value < 0.0:
            return (False, "Value must be must be positive numbers")
        return (True, "")

    @staticmethod
    def validate_current_balance (current_balance: float) -> Tuple[bool, str]:
        if current_balance is None:
            return (False, "current_balance is required")
        if type(current_balance) != float:
            return (False, "current_balance must be a float")
        if current_balance < 0.0:
            return (False, "current_balance must be positive numbers")
        return (True, "")
    
    
    @staticmethod
    def validate_timestamp(timestamp: float) -> Tuple[bool, str]:
        if timestamp is None:
            return (False, "Timestamp is required")
        if type(timestamp) != float:
            return (False, "Timestamp must be a float")
        if timestamp < 0.0:
            return (False, "Timestamp is must be positive numbers")
        return (True, "")
        
