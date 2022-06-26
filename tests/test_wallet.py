import pytest
from src.wallet import Wallet, InsufficientAmount


@pytest.fixture
def empty_wallet():
    return Wallet()


@pytest.fixture
def wallet():
    return Wallet(100)


def test_default_initial_amount(empty_wallet):
    assert empty_wallet.balance == 0


def test_wallet_add_cash(wallet):
    wallet.add_cash(20)
    assert wallet.balance == 120


def test_wallet_spend_cash(wallet):
    wallet.spend_cash(80)
    assert wallet.balance == 20


def test_wallet_spend_cash_exception(wallet):
    with pytest.raises(InsufficientAmount):
        wallet.spend_cash(120)
