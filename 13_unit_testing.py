#!/usr/bin/env python3
"""
================================================================================
LESSON 13: UNIT TESTING IN PYTHON — FROM BASIC TO ADVANCED MOCKING & ASYNC
================================================================================

Software testing ensures that your code works correctly, prevents regressions, 
and gives you confidence when refactoring.

In Python, testing is divided into several patterns and tools:
1. Standard Library `unittest`: Built-in class-based testing framework.
2. `pytest`: Popular third-party framework with clean function-based `assert` syntax.
3. Test Double & Mocking (`unittest.mock`): Replacing real databases/APIs with fake objects.
4. Asynchronous Testing (`unittest.IsolatedAsyncioTestCase` / `AsyncMock`): Testing `async def`.

--------------------------------------------------------------------------------
TYPES OF TESTS COVERED IN THIS LESSON
--------------------------------------------------------------------------------
1. Basic Unit Test: Testing pure functions & return values.
2. Exception / Edge Case Test: Verifying that invalid input raises expected errors.
3. Test Lifecycle Fixtures: Using `setUp` & `tearDown` for clean state.
4. Mocking External API / Dependencies: Replacing HTTP calls with `MagicMock` & `@patch`.
5. Async Unit Test: Testing async coroutines and `AsyncMock`.
6. Parametrized Testing: Testing multiple input/output scenarios cleanly.
"""

import unittest
from unittest.mock import patch, MagicMock, AsyncMock
import asyncio
import time

# ================================================================================
# CODE UNDER TEST (THE APPLICATION LOGIC WE WANT TO TEST)
# ================================================================================

class BankAccount:
    """A simple bank account class to demonstrate unit testing."""
    def __init__(self, owner: str, balance: float = 0.0):
        if balance < 0:
            raise ValueError("Initial balance cannot be negative!")
        self.owner = owner
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount: float) -> float:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive!")
        self.balance += amount
        self.transaction_history.append(f"Deposited ${amount:.2f}")
        return self.balance

    def withdraw(self, amount: float) -> float:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive!")
        if amount > self.balance:
            raise InsufficientFundsError(f"Cannot withdraw ${amount}. Current balance: ${self.balance}")
        self.balance -= amount
        self.transaction_history.append(f"Withdrew ${amount:.2f}")
        return self.balance


class InsufficientFundsError(Exception):
    """Custom exception raised when withdrawal exceeds balance."""
    pass


class PaymentGatewayService:
    """Service that interacts with an external payment API (to demonstrate Mocking)."""
    def charge_card(self, card_number: str, amount: float) -> dict:
        # In real life, this makes an expensive HTTP network call to Stripe/PayPal
        print("🌐 Connecting to Payment Gateway over network...")
        time.sleep(2.0)  # Simulated network latency
        return {"status": "success", "transaction_id": "tx_9999"}


class ShoppingCart:
    """Uses PaymentGatewayService to process orders."""
    def __init__(self, gateway: PaymentGatewayService):
        self.gateway = gateway
        self.items = []

    def add_item(self, name: str, price: float):
        self.items.append((name, price))

    def checkout(self, card_number: str) -> bool:
        total = sum(price for _, price in self.items)
        response = self.gateway.charge_card(card_number, total)
        return response.get("status") == "success"


# Async Code under test
async def fetch_user_data(user_id: int, async_api_client) -> dict:
    """Async coroutine fetching user data from an async API client."""
    response = await async_api_client.get(f"/users/{user_id}")
    if response.get("status") == 200:
        return response.get("data")
    raise ValueError(f"User {user_id} not found!")


# ================================================================================
# PART 1: BASIC UNIT TESTS & EXCEPTION TESTING
# ================================================================================

class TestBankAccount(unittest.TestCase):
    
    # --- Lifecycle Fixtures ---
    def setUp(self):
        """Runs BEFORE every test method to provide fresh state."""
        self.account = BankAccount(owner="Alice", balance=100.0)

    def tearDown(self):
        """Runs AFTER every test method for cleanup (e.g. closing files or DB)."""
        pass

    # --- 1. Testing Normal Behavior ---
    def test_initial_balance(self):
        self.assertEqual(self.account.balance, 100.0)
        self.assertEqual(self.account.owner, "Alice")

    def test_deposit_valid_amount(self):
        new_balance = self.account.deposit(50.0)
        self.assertEqual(new_balance, 150.0)
        self.assertEqual(self.account.balance, 150.0)
        self.assertIn("Deposited $50.00", self.account.transaction_history)

    def test_withdraw_valid_amount(self):
        new_balance = self.account.withdraw(40.0)
        self.assertEqual(new_balance, 60.0)
        self.assertIn("Withdrew $40.00", self.account.transaction_history)

    # --- 2. Testing Exceptions & Edge Cases ---
    def test_deposit_negative_amount_raises_error(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-10.0)

    def test_withdraw_insufficient_funds_raises_custom_exception(self):
        with self.assertRaises(InsufficientFundsError):
            self.account.withdraw(500.0)

    # --- 3. Parametrized Test (SubTest) ---
    def test_multiple_deposits_parametrized(self):
        """Test multiple deposit amounts using subTest context manager."""
        test_cases = [
            (10.0, 110.0),
            (25.5, 125.5),
            (100.0, 200.0),
        ]
        for deposit_amount, expected_balance in test_cases:
            with self.subTest(deposit=deposit_amount, expected=expected_balance):
                acc = BankAccount(owner="Test", balance=100.0)
                result = acc.deposit(deposit_amount)
                self.assertEqual(result, expected_balance)


# ================================================================================
# PART 2: MOCKING EXTERNAL DEPENDENCIES (unittest.mock)
# ================================================================================

class TestShoppingCartWithMocking(unittest.TestCase):
    
    # --- 4. Using MagicMock directly ---
    def test_checkout_successful(self):
        # Create a fake PaymentGatewayService object
        mock_gateway = MagicMock(spec=PaymentGatewayService)
        # Configure return value of charge_card without hitting real network!
        mock_gateway.charge_card.return_value = {"status": "success", "transaction_id": "tx_mock_123"}

        cart = ShoppingCart(gateway=mock_gateway)
        cart.add_item("Book", 20.0)
        cart.add_item("Pen", 5.0)

        result = cart.checkout("4111-2222-3333-4444")

        # Verify assertions
        self.assertTrue(result)
        # Verify the mock function was actually called with expected arguments!
        mock_gateway.charge_card.assert_called_once_with("4111-2222-3333-4444", 25.0)

    # --- 5. Mocking Side Effects (Exceptions / Failures) ---
    def test_checkout_gateway_failure(self):
        mock_gateway = MagicMock(spec=PaymentGatewayService)
        # Simulate network error or failed payment
        mock_gateway.charge_card.return_value = {"status": "declined", "error": "Insufficient funds"}

        cart = ShoppingCart(gateway=mock_gateway)
        cart.add_item("Laptop", 1200.0)

        result = cart.checkout("4111-2222-3333-4444")
        self.assertFalse(result)

    # --- 6. Using @patch Decorator ---
    @patch.object(PaymentGatewayService, 'charge_card')
    def test_checkout_with_patch_decorator(self, mock_charge_card):
        # mock_charge_card is automatically injected by @patch
        mock_charge_card.return_value = {"status": "success", "transaction_id": "tx_patch_777"}

        real_gateway = PaymentGatewayService()
        cart = ShoppingCart(gateway=real_gateway)
        cart.add_item("Keyboard", 50.0)

        self.assertTrue(cart.checkout("1234"))
        mock_charge_card.assert_called_once_with("1234", 50.0)


# ================================================================================
# PART 3: ASYNCHRONOUS UNIT TESTING (unittest.IsolatedAsyncioTestCase)
# ================================================================================

class TestAsyncCode(unittest.IsolatedAsyncioTestCase):
    
    # --- 7. Testing Coroutines & AsyncMock ---
    async def test_fetch_user_data_success(self):
        # Create an AsyncMock for the async API client
        mock_async_client = AsyncMock()
        mock_async_client.get.return_value = {
            "status": 200,
            "data": {"id": 42, "name": "Charlie", "role": "admin"}
        }

        # Await the async function under test
        user_data = await fetch_user_data(42, mock_async_client)

        self.assertEqual(user_data["name"], "Charlie")
        mock_async_client.get.assert_awaited_once_with("/users/42")

    async def test_fetch_user_data_not_found_raises_error(self):
        mock_async_client = AsyncMock()
        mock_async_client.get.return_value = {"status": 404}

        with self.assertRaises(ValueError):
            await fetch_user_data(999, mock_async_client)


# ================================================================================
# DRIVER TO RUN ALL TESTS
# ================================================================================

if __name__ == "__main__":
    print("==================================================")
    print("RUNNING PYTHON UNIT TEST SUITE")
    print("==================================================")
    unittest.main(verbosity=2)
