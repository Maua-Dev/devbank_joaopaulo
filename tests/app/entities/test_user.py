import pytest
from src.app.entities.user import User
from src.app.errors.entity_errors import ParamNotValidated


class Test_User:
    def test_user(self):
        user = User(name="Jão", agency="0000", account="00000-0", current_balance=1000.0)

        assert user.name == "Jão"
        assert user.agency == "0000"
        assert user.account == "00000-0"
        assert user.current_balance == 1000.0

    def test_name_none(self):
        with pytest.raises(ParamNotValidated):
            user = User(agency="0000", account="00000-0", current_balance=1000.0)

    def test_name_invalid(self):
        with pytest.raises(ParamNotValidated):
            user = User(name=True, agency="0000", account="00000-0", current_balance=1000.0)

    def test_name_size(self):
        with pytest.raises(ParamNotValidated):
            user = User(name="Jo", agency="0000", account="00000-0", current_balance=1000.0)

    def test_agency_none(self):
        with pytest.raises(ParamNotValidated):
            user = User(name="Jão", account="00000-0", current_balance=1000.0)

    def test_agency_invalid(self):
        with pytest.raises(ParamNotValidated):
            user = User(name="Jão", agency=0000, account="00000-0", current_balance=1000.0)
            
    def test_agency_size(self):
        with pytest.raises(ParamNotValidated):
            user = User(name="Jão", agency="123456", account="00000-0", current_balance=1000.0)

    def test_account_none(self):
        with pytest.raises(ParamNotValidated):
            user = User(name="Jão", agency="0000", current_balance=1000.0)

    def test_account_invalid(self):
        with pytest.raises(ParamNotValidated):
            user = User(name="Jão", agency="0000", account=True, current_balance=1000.0)

    def test_account_wrong_format(self):
        with pytest.raises(ParamNotValidated):
            user = User(name="Jão", agency="0000", account="000000", current_balance=1000.0)

    def test_account_size(self):
        with pytest.raises(ParamNotValidated):
            user = User(name="Jão", agency="0000", account="00000-00", current_balance=1000.0)

    def test_current_balance_none(self):
        with pytest.raises(ParamNotValidated):
            user = User(name="Jão", agency="0000",account="00000-0")

    def test_current_balance_invalid(self):
        with pytest.raises(ParamNotValidated):
            user = User(name="Jão", agency="0000", account="00000-0", current_balance=True)

    def test_current_balance_negative_value(self):
        with pytest.raises(ParamNotValidated):
            user = User(name="Jão", agency="0000", account="00000-0", current_balance=-1000.0)
            