#!/usr/bin/env python3
"""
================================================================================
LESSON 14: PYTEST — IDIOMATIC FUNCTION-BASED TESTING IN PYTHON
================================================================================

In Lesson 13, we learned `unittest` (Python's built-in class-based framework).
`pytest` is the most popular third-party testing framework in Python because it 
is simpler, requires less boilerplate code, and provides powerful features like:

1. Plain `assert` statements (No `self.assertEqual`, `self.assertTrue`, etc.).
2. Function-based tests (No need to subclass `unittest.TestCase`).
3. `@pytest.fixture`: Modular, reusable setup/teardown functions.
4. `@pytest.mark.parametrize`: Clean, readable data-driven testing.
5. `@pytest.mark.asyncio`: Native async test support.
"""

import pytest
import importlib
from unittest.mock import MagicMock, AsyncMock

# Dynamic import of 13_unit_testing module
unit_test_module = importlib.import_module("13_unit_testing")
BankAccount = unit_test_module.BankAccount
InsufficientFundsError = unit_test_module.InsufficientFundsError
ShoppingCart = unit_test_module.ShoppingCart
PaymentGatewayService = unit_test_module.PaymentGatewayService
fetch_user_data = unit_test_module.fetch_user_data

# ================================================================================
# PART 1: NATIVE PYTEST FIXTURES & BASIC ASSERTS
# ================================================================================

# In pytest, fixtures are declared using @pytest.fixture decorator.
# Any test function that names `account` as an argument receives the returned object!
@pytest.fixture
def account():
    """Provides a fresh BankAccount instance before each test function."""
    return BankAccount(owner="Alice", balance=100.0)


def test_initial_balance(account):
    """In pytest, we use plain Python `assert` statements."""
    assert account.balance == 100.0
    assert account.owner == "Alice"


def test_deposit_valid_amount(account):
    new_balance = account.deposit(50.0)
    assert new_balance == 150.0
    assert "Deposited $50.00" in account.transaction_history


def test_withdraw_valid_amount(account):
    new_balance = account.withdraw(40.0)
    assert new_balance == 60.0


# ================================================================================
# PART 2: TESTING EXCEPTIONS IN PYTEST
# ================================================================================

def test_deposit_negative_amount_raises_error(account):
    """pytest uses `with pytest.raises(ExceptionClass):`."""
    with pytest.raises(ValueError, match="Deposit amount must be positive!"):
        account.deposit(-10.0)


def test_withdraw_insufficient_funds_raises_custom_exception(account):
    with pytest.raises(InsufficientFundsError):
        account.withdraw(500.0)


# ================================================================================
# PART 3: PARAMETRIZED TESTING WITH @pytest.mark.parametrize
# ================================================================================

@pytest.mark.parametrize("deposit_amount, expected_balance", [
    (10.0, 110.0),
    (25.5, 125.5),
    (100.0, 200.0),
])
def test_multiple_deposits_parametrized(deposit_amount, expected_balance):
    """Pytest runs this single test 3 times with different parameters!"""
    acc = BankAccount(owner="Test", balance=100.0)
    result = acc.deposit(deposit_amount)
    assert result == expected_balance


# ================================================================================
# PART 4: MOCKING IN PYTEST
# ================================================================================

@pytest.fixture
def mock_gateway():
    """Fixture providing a mocked PaymentGatewayService."""
    gateway = MagicMock(spec=PaymentGatewayService)
    gateway.charge_card.return_value = {"status": "success", "transaction_id": "tx_pytest_123"}
    return gateway


def test_checkout_successful(mock_gateway):
    cart = ShoppingCart(gateway=mock_gateway)
    cart.add_item("Book", 20.0)
    
    assert cart.checkout("4111-2222-3333-4444") is True
    mock_gateway.charge_card.assert_called_once_with("4111-2222-3333-4444", 20.0)


# ================================================================================
# PART 5: ASYNC TESTING WITH @pytest.mark.asyncio
# ================================================================================

@pytest.mark.asyncio
async def test_fetch_user_data_success():
    mock_async_client = AsyncMock()
    mock_async_client.get.return_value = {
        "status": 200,
        "data": {"id": 42, "name": "Charlie", "role": "admin"}
    }

    user_data = await fetch_user_data(42, mock_async_client)
    assert user_data["name"] == "Charlie"
    mock_async_client.get.assert_awaited_once_with("/users/42")
