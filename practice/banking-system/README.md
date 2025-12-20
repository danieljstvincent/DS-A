# Banking System - 4-Level Implementation

A simplified banking system implementation for practicing Python and interview preparation. The system is divided into 4 progressive levels, where each level unlocks after the previous one is completed.

## 📚 Solution Location

**The complete solution is available in:** `banking_system_solution.py`

**The template file for you to implement is:** `banking_system.py`

Try implementing it yourself first, then refer to the solution if you get stuck!

## Overview

This banking system supports:
- **Level 1:** Account creation, deposits, and transfers
- **Level 2:** Ranking accounts based on outgoing transactions
- **Level 3:** Scheduled payments with cashback
- **Level 4:** Merging accounts with balance and transaction history retention

## Project Structure

```
Banking_System/
├── banking_system.py          # Template for you to implement (with method stubs)
├── banking_system_solution.py # Complete solution (for reference)
├── test_banking_system.py     # Comprehensive test suite
├── run_single_test.sh         # Script to run individual tests
├── demo.py                    # Demo script showing all features
├── sandbox_tests.py           # Custom test playground
└── README.md                  # Complete documentation (this file)
```

## Getting Started

1. **Start with the template**: Open `banking_system.py` - it includes method stubs with helpful docstrings
2. **Understand data structures**: Review the `__init__` method to see what data structures are initialized
3. **Test your implementation**: Run `python3 test_banking_system.py 1` to test Level 1
4. **Debug when needed**: Use `bank.debug_state()` to inspect the system state
5. **Check the solution**: If you get stuck, refer to `banking_system_solution.py` for the complete implementation
6. **Progressive unlocking**: Each level unlocks after passing all tests for the previous level

## Method Reference

### Level 1: Basic Operations

#### `create_account(timestamp: int, account_id: str) -> bool`
Creates a new account with the given identifier.
- Returns `True` if account was created successfully
- Returns `False` if account already exists

#### `deposit(timestamp: int, account_id: str, amount: int) -> int | None`
Deposits money into the specified account.
- Returns the balance after deposit if successful
- Returns `None` if account doesn't exist

#### `transfer(timestamp: int, source_account_id: str, target_account_id: str, amount: int) -> int | None`
Transfers money from source to target account.
- Returns the source account balance if successful
- Returns `None` if:
  - Either account doesn't exist
  - Source and target are the same
  - Source has insufficient funds

### Level 2: Account Ranking

#### `get_top_accounts(n: int) -> List[str]`
Returns the top `n` accounts ranked by total outgoing transaction amount.
- Accounts are sorted by outgoing amount (descending)
- Ties are broken by account ID (ascending)

### Level 3: Scheduled Payments with Cashback

#### `schedule_payment(timestamp: int, source_account_id: str, target_account_id: str, amount: int, cashback_percentage: float) -> str | None`
Schedules a payment with cashback.
- Reserves the amount from source account immediately
- Returns payment ID if successful
- Returns `None` if account doesn't exist or has insufficient funds

#### `execute_payment(timestamp: int, payment_id: str) -> bool | None`
Executes a scheduled payment.
- Transfers amount to target account
- Adds cashback to source account
- Returns `True` if successful
- Returns `None` if payment doesn't exist or already executed

#### `get_payment_status(payment_id: str) -> str | None`
Gets the status of a scheduled payment.
- Returns `'scheduled'` or `'executed'`
- Returns `None` if payment doesn't exist

### Level 4: Account Merging

#### `merge_accounts(timestamp: int, account_id_1: str, account_id_2: str) -> str | None`
Merges two accounts, retaining both accounts' balance and transaction histories.
- Returns the account ID of the merged account (alphabetically first)
- Returns `None` if either account doesn't exist or accounts are the same
- Merged account can still be accessed through its original ID

#### `get_account_balance(account_id: str) -> int | None`
Gets the current balance of an account (handles merged accounts).

#### `get_transaction_history(account_id: str) -> List[Dict] | None`
Gets the complete transaction history of an account.

### Helper Methods

#### `_get_actual_account_id(account_id: str) -> Optional[str]`
Resolves merged accounts to actual account ID. Use this helper in all methods that access account data.

#### `get_outgoing_transactions(account_id: str) -> Optional[int]`
Returns total outgoing transaction amount for an account.

#### `debug_state() -> str`
Returns formatted string of system state for debugging.

## Implementation Guide

### Data Structures

Before implementing, understand these data structures (already initialized in `__init__`):

- **`self.accounts`**: `Dict[str, int]` - account_id → balance
- **`self.outgoing_transactions`**: `Dict[str, int]` - account_id → total outgoing amount
- **`self.scheduled_payments`**: `Dict[str, Dict]` - payment_id → payment details
- **`self.payment_counter`**: `int` - counter for generating unique payment IDs
- **`self.transaction_history`**: `Dict[str, List[Dict]]` - account_id → list of transactions
- **`self.merged_accounts`**: `Dict[str, str]` - old_account_id → new_account_id
- **`self.merged_from`**: `Dict[str, List[str]]` - account_id → list of accounts merged into it (for debugging)

### Level 1: Basic Operations

**Implementation Order:**
1. `_get_actual_account_id()` (simple version for Level 1)
2. `create_account()`
3. `deposit()`
4. `transfer()`

#### `_get_actual_account_id()` (Simple Version for Level 1)

```python
def _get_actual_account_id(self, account_id: str) -> Optional[str]:
    if account_id in self.accounts:
        return account_id
    return None
```

#### `create_account()`

**Logic:**
1. Check if account already exists in `self.accounts`
2. Check if account was merged (exists in `self.merged_accounts`)
3. If neither, create account with balance 0
4. Return True if created, False if already exists

**Example:**
```python
def create_account(self, timestamp: int, account_id: str) -> bool:
    if account_id in self.accounts:
        return False
    if account_id in self.merged_accounts:
        return False
    self.accounts[account_id] = 0
    return True
```

#### `deposit()`

**Logic:**
1. Get actual account ID using `_get_actual_account_id()`
2. Check if account exists
3. Add amount to balance
4. Record transaction history (needed for Level 4)
5. Return new balance, or None if account doesn't exist

**Transaction History Format:**
```python
{
    'timestamp': timestamp,
    'type': 'deposit',
    'from': None,
    'to': actual_account_id,
    'amount': amount
}
```

#### `transfer()`

**Logic:**
1. Get actual account IDs for both source and target
2. Check if both accounts exist
3. Check if source and target are different
4. Check if source has sufficient funds
5. If all checks pass:
   - Deduct amount from source
   - Add amount to target
   - Track outgoing transaction (for Level 2)
   - Record transaction history for both accounts
6. Return source balance, or None if any check fails

**Transaction History:**
- Source: `'type': 'transfer_out'`
- Target: `'type': 'transfer_in'`

### Level 2: Account Ranking

#### `get_top_accounts()`

**Logic:**
1. Get all accounts with outgoing transactions (amount > 0)
2. Sort by:
   - Outgoing amount (descending)
   - Account ID (ascending) for ties
3. Return top n account IDs

**Example:**
```python
def get_top_accounts(self, n: int) -> List[str]:
    accounts_with_transactions = [
        (account_id, amount) 
        for account_id, amount in self.outgoing_transactions.items()
        if amount > 0
    ]
    
    sorted_accounts = sorted(
        accounts_with_transactions,
        key=lambda x: (-x[1], x[0])  # desc amount, asc ID
    )
    
    return [account_id for account_id, _ in sorted_accounts[:n]]
```

### Level 3: Scheduled Payments

#### `schedule_payment()`

**Logic:**
1. Get actual account IDs
2. Check if both accounts exist
3. Check if source has sufficient funds
4. Generate payment ID: `f"payment_{self.payment_counter}"`
5. Calculate cashback: `int(amount * cashback_percentage)`
6. Reserve amount (deduct from source immediately)
7. Store payment details in `self.scheduled_payments`
8. Record transaction history
9. Increment payment counter
10. Return payment ID, or None if checks fail

**Payment Details Structure:**
```python
{
    'timestamp': timestamp,
    'source_account_id': actual_source,
    'target_account_id': actual_target,
    'amount': amount,
    'cashback_percentage': cashback_percentage,
    'cashback_amount': cashback_amount,
    'status': 'scheduled'
}
```

#### `execute_payment()`

**Logic:**
1. Check if payment exists
2. Check if payment status is 'scheduled'
3. If both checks pass:
   - Transfer amount to target account
   - Add cashback to source account
   - Update payment status to 'executed'
   - Record transaction history for both accounts
4. Return True if successful, None if checks fail

#### `get_payment_status()`

**Logic:**
1. Check if payment exists
2. Return payment status ('scheduled' or 'executed')
3. Return None if payment doesn't exist

### Level 4: Account Merging

#### Update `_get_actual_account_id()` (Handle Merge Chains)

**Logic:**
1. If account exists directly, return it
2. If account was merged, follow the chain to find the actual account
3. Handle circular references (safety check)
4. Return actual account ID, or None if not found

**Example:**
```python
def _get_actual_account_id(self, account_id: str) -> Optional[str]:
    if account_id in self.accounts:
        return account_id
    
    current = account_id
    visited = set()
    
    while current in self.merged_accounts:
        if current in visited:
            return None  # Circular reference
        visited.add(current)
        current = self.merged_accounts[current]
    
    if current in self.accounts:
        return current
    
    return None
```

#### `merge_accounts()`

**Logic:**
1. Get actual account IDs
2. Check if both accounts exist
3. Check if accounts are different
4. Determine which account to keep (alphabetically first)
5. Combine balances
6. Merge transaction histories (combine and sort by timestamp)
7. Combine outgoing transaction amounts
8. Record merge in transaction history
9. Update `self.merged_accounts`
10. Update scheduled payments that reference merged account
11. Remove merged account from `self.accounts`
12. Return kept account ID

#### `get_account_balance()` and `get_transaction_history()`

Both methods should:
1. Get actual account ID (handles merged accounts)
2. Return the requested data if account exists
3. Return None if account doesn't exist

## Common Patterns

### Pattern 1: Checking Account Existence

Always use `_get_actual_account_id()` to check if an account exists:

```python
actual_id = self._get_actual_account_id(account_id)
if actual_id is None or actual_id not in self.accounts:
    return None
```

### Pattern 2: Recording Transaction History

Always record transactions in this format:
```python
self.transaction_history[account_id].append({
    'timestamp': timestamp,
    'type': 'transaction_type',
    'from': source_account_id,  # or None
    'to': target_account_id,     # or None
    'amount': amount,
    # ... other relevant fields
})
```

### Pattern 3: Handling Merged Accounts

When accessing account data, always resolve to the actual account:
```python
actual_id = self._get_actual_account_id(account_id)
# Then use actual_id instead of account_id
```

### Pattern 4: Returning None for Errors

When an operation fails, return `None`. Common failure cases:
- Account doesn't exist
- Insufficient funds
- Invalid parameters (same account, etc.)
- Payment already executed

## Transaction History Formats

### Deposit
```python
{
    'timestamp': int,
    'type': 'deposit',
    'from': None,
    'to': account_id,
    'amount': int
}
```

### Transfer
```python
{
    'timestamp': int,
    'type': 'transfer_out' or 'transfer_in',
    'from': source_account_id,
    'to': target_account_id,
    'amount': int
}
```

### Scheduled Payment
```python
{
    'timestamp': int,
    'type': 'scheduled_payment',
    'from': source_account_id,
    'to': target_account_id,
    'amount': int,
    'payment_id': str
}
```

### Payment Execution
```python
{
    'timestamp': int,
    'type': 'payment_received' or 'cashback',
    'from': source_account_id or None,
    'to': target_account_id or source_account_id,
    'amount': int,
    'payment_id': str
}
```

### Merge
```python
{
    'timestamp': int,
    'type': 'merge',
    'from': merged_account_id,
    'to': kept_account_id,
    'amount': int
}
```

## Usage

### Running All Tests

```bash
python3 test_banking_system.py
```

### Running Tests for a Specific Level

```bash
python3 test_banking_system.py 1  # Level 1 only
python3 test_banking_system.py 2  # Levels 1 and 2
python3 test_banking_system.py 3  # Levels 1, 2, and 3
python3 test_banking_system.py 4  # All levels
```

### Running a Single Test Case

```bash
bash run_single_test.sh TestLevel1.test_level_1_case_01_basic_create
```

### Running Demo

```bash
python3 demo.py
```

### Running Sandbox Tests

```bash
python3 sandbox_tests.py
```

### Example Usage

```python
from banking_system import BankingSystem

# Create banking system
bank = BankingSystem()

# Level 1: Create accounts and make transactions
bank.create_account(1000, "alice")
bank.create_account(2000, "bob")
bank.deposit(3000, "alice", 1000)
bank.transfer(4000, "alice", "bob", 200)

# Level 2: Get top accounts
top_accounts = bank.get_top_accounts(5)
print(f"Top accounts: {top_accounts}")

# Level 3: Schedule and execute payment
payment_id = bank.schedule_payment(5000, "alice", "bob", 300, 0.10)
bank.execute_payment(6000, payment_id)

# Level 4: Merge accounts
merged_id = bank.merge_accounts(7000, "alice", "bob")
print(f"Merged account: {merged_id}")

# Debug state
print(bank.debug_state())
```

## Testing

The test suite includes:
- **TestLevel1:** 10 test cases for account creation, deposits, and transfers
- **TestLevel2:** 4 test cases for account ranking
- **TestLevel3:** 6 test cases for scheduled payments and cashback
- **TestLevel4:** 6 test cases for account merging
- **TestIntegration:** End-to-end workflow tests

### Test Features

- All tests use `@timeout(0.4)` decorators (0.4 second timeout)
- Tests are designed to match coding challenge platform patterns
- Comprehensive edge case coverage
- Sandbox tests allow for custom testing

## Common Pitfalls

1. **Forgetting to handle merged accounts**: Always use `_get_actual_account_id()` before accessing account data
2. **Not recording transaction history**: Even in Level 1, start recording transaction history (needed for Level 4)
3. **Not tracking outgoing transactions**: Track outgoing transactions in `transfer()` for Level 2 ranking
4. **Incorrect sorting in `get_top_accounts()`**: Remember: descending by amount, ascending by ID for ties
5. **Not updating scheduled payments after merge**: When merging accounts, update any scheduled payments that reference the merged account
6. **Returning balance instead of None**: When an operation fails, return `None`, not the balance

## Notes

- All timestamps are integers representing milliseconds
- Timestamps are guaranteed to be unique and strictly increasing
- The implementation handles merged accounts transparently
- Transaction histories are preserved through merges
- Cashback is calculated as a percentage of the payment amount (rounded down to integer)

## Helpful Features

- **Method Stubs**: The template includes all method signatures with type hints and docstrings
- **Data Structure Initialization**: All data structures are initialized in `__init__` with helpful comments
- **Debug Helper**: Use `bank.debug_state()` to inspect the current system state

## Solution Overview

The solution in `banking_system_solution.py` implements:

### Key Design Decisions

1. **Data Structures**:
   - `accounts`: Dict mapping account_id to balance
   - `outgoing_transactions`: Dict tracking total outgoing amounts
   - `scheduled_payments`: Dict storing payment details
   - `transaction_history`: Dict mapping account_id to list of transactions
   - `merged_accounts`: Dict mapping old account_id to new account_id
   - `merged_from`: Dict mapping account_id to list of accounts merged into it (for debugging)

2. **Merged Account Handling**:
   - Uses `_get_actual_account_id()` helper to resolve merged accounts
   - Follows chain of merges to find the actual account
   - All operations transparently handle merged accounts

3. **Transaction History**:
   - Records all operations (deposits, transfers, payments, merges)
   - Maintains chronological order
   - Preserves history through merges

## Requirements

- Python 3.7+
- No external dependencies (uses only standard library)

## Learning Objectives

This project helps practice:
- Object-oriented programming in Python
- Data structures (dictionaries, lists)
- Algorithm implementation (sorting, searching)
- Test-driven development
- Code organization and modularity
- Handling edge cases and error conditions
