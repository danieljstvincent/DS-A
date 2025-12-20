"""
Banking System Implementation
A simplified banking system with 4 levels of functionality.

This solution demonstrates:
- Level 1: Basic account operations (create, deposit, transfer)
- Level 2: Account ranking based on outgoing transactions
- Level 3: Scheduled payments with cashback
- Level 4: Account merging with history retention

Key Design Decisions:
1. Using dictionaries for O(1) lookups and updates
2. Tracking transaction history from Level 1 (needed for Level 4)
3. Using a helper method to handle merged accounts transparently
4. Storing payment details separately to track status
"""

from typing import Optional, List, Dict
from collections import defaultdict


class BankingSystem:
    """
    A simplified banking system that supports:
    - Level 1: Account creation, deposits, and transfers
    - Level 2: Ranking accounts based on outgoing transactions
    - Level 3: Scheduled payments with cashback
    - Level 4: Merging accounts with history retention
    """
    
    def __init__(self):
        """
        Initialize all data structures needed for the banking system.
        
        DESIGN NOTE: We initialize all data structures upfront, even if they're
        only used in later levels. This makes the code cleaner and avoids
        conditional initialization later.
        """
        # Level 1: Basic account management
        # Dictionary provides O(1) lookup and update for account balances
        # Key: account_id (str), Value: balance (int)
        self.accounts: Dict[str, int] = {}  # account_id -> balance
        
        # Level 2: Transaction tracking for ranking
        # defaultdict(int) automatically initializes missing keys to 0
        # This is useful because not all accounts make outgoing transactions
        # Key: account_id (str), Value: total outgoing amount (int)
        self.outgoing_transactions: Dict[str, int] = defaultdict(int)  # account_id -> total outgoing amount
        
        # Level 3: Scheduled payments
        # Store payment details as dictionaries for easy access to all fields
        # Key: payment_id (str), Value: payment details (dict)
        self.scheduled_payments: Dict[str, Dict] = {}  # payment_id -> payment details
        
        # Counter for generating unique payment IDs
        # Incremented each time a payment is scheduled
        # Format: "payment_0", "payment_1", "payment_2", etc.
        self.payment_counter = 0  # For generating unique payment IDs
        
        # Level 4: Transaction history and account merging
        # defaultdict(list) automatically creates empty lists for new accounts
        # Each transaction is stored as a dictionary with relevant fields
        # Key: account_id (str), Value: list of transaction dictionaries
        self.transaction_history: Dict[str, List[Dict]] = defaultdict(list)  # account_id -> list of transactions
        
        # Track merged accounts: maps old account ID to new account ID
        # This allows us to redirect operations on merged accounts
        # Key: old_account_id (str), Value: new_account_id (str)
        self.merged_accounts: Dict[str, str] = {}  # old_account_id -> new_account_id (for merged accounts)
        
        # Track which accounts were merged into each account
        # This is useful for debugging and understanding merge chains
        # Key: account_id (str), Value: list of account IDs merged into it
        self.merged_from: Dict[str, List[str]] = defaultdict(list)  # account_id -> list of accounts merged into it
    
    # ==================== LEVEL 1 ====================
    
    def create_account(self, timestamp: int, account_id: str) -> bool:
        """
        Create a new account with the given identifier.
        
        TIME COMPLEXITY: O(1)
        - Dictionary membership check: O(1)
        - Dictionary insertion: O(1)
        - Total: O(1) constant time
        
        SPACE COMPLEXITY: O(1)
        - Only creates one new dictionary entry
        - No additional data structures needed
        
        IMPLEMENTATION NOTES:
        - We check two conditions before creating an account:
          1. Account doesn't already exist in self.accounts
          2. Account wasn't previously merged (doesn't exist in self.merged_accounts)
        - New accounts start with a balance of 0
        - The timestamp parameter is provided for consistency but not used in Level 1
        
        Args:
            timestamp: Stringified timestamp in milliseconds (not used in Level 1)
            account_id: Unique identifier for the account
            
        Returns:
            True if account was successfully created, False if account already exists
        """
        # Check if account already exists in the active accounts dictionary
        # This prevents duplicate account creation
        if account_id in self.accounts:
            return False
        
        # Check if this account was previously merged into another account
        # Once an account is merged, its ID is "taken" and cannot be reused
        # This maintains data integrity and prevents confusion
        if account_id in self.merged_accounts:
            return False
        
        # Create the account with initial balance of 0
        # All accounts start with zero balance
        self.accounts[account_id] = 0
        return True
    
    def deposit(self, timestamp: int, account_id: str, amount: int) -> Optional[int]:
        """
        Deposit money into the specified account.
        
        TIME COMPLEXITY: O(k) where k is the length of merge chain
        - _get_actual_account_id(): O(k) worst case (if account was merged multiple times)
        - Dictionary lookup: O(1)
        - Dictionary update: O(1)
        - List append: O(1)
        - Total: O(k) where k is typically 1 (no merges) or small (few merges)
        
        SPACE COMPLEXITY: O(1)
        - Only adds one transaction dictionary to the list
        - No additional data structures created
        
        IMPLEMENTATION NOTES:
        - Uses _get_actual_account_id() to handle merged accounts transparently
        - Records transaction history even though it's not required for Level 1
          This makes Level 4 implementation easier (no need to retroactively add history)
        - Returns None if account doesn't exist (error condition)
        - Returns new balance if successful
        
        Args:
            timestamp: Stringified timestamp in milliseconds (used for transaction history)
            account_id: Identifier of the account (may be a merged account)
            amount: Amount to deposit (must be positive)
            
        Returns:
            Balance of the account after deposit, or None if account doesn't exist
        """
        # Handle merged accounts: resolve to the actual account ID
        # If account_id was merged, this will return the account it was merged into
        # If account_id doesn't exist, this returns None
        actual_account_id = self._get_actual_account_id(account_id)
        
        # Validate that the account exists
        # We check both None (from _get_actual_account_id) and not in accounts
        # for extra safety
        if actual_account_id is None or actual_account_id not in self.accounts:
            return None
        
        # Update the account balance
        # Simple addition operation
        self.accounts[actual_account_id] += amount
        
        # Record transaction history (Level 4 requirement, but we do it from Level 1)
        # This ensures we have complete history when we reach Level 4
        # Transaction format includes all relevant information for later queries
        self.transaction_history[actual_account_id].append({
            'timestamp': timestamp,
            'type': 'deposit',  # Transaction type for filtering/querying later
            'from': None,  # Deposits don't have a source account
            'to': actual_account_id,  # Destination account
            'amount': amount  # Amount deposited
        })
        
        # Return the new balance
        return self.accounts[actual_account_id]
    
    def transfer(self, timestamp: int, source_account_id: str, target_account_id: str, amount: int) -> Optional[int]:
        """
        Transfer money from source account to target account.
        
        TIME COMPLEXITY: O(k) where k is the length of merge chain
        - Two _get_actual_account_id() calls: O(k) each
        - Dictionary lookups: O(1) each
        - Dictionary updates: O(1) each
        - List appends: O(1) each
        - Total: O(k) where k is typically 1 (no merges) or small (few merges)
        
        SPACE COMPLEXITY: O(1)
        - Only adds two transaction dictionaries to lists
        - No additional data structures created
        
        IMPLEMENTATION NOTES:
        - Validates both accounts exist before proceeding
        - Prevents transferring to the same account (edge case)
        - Checks for sufficient funds before transferring
        - Updates both accounts' balances atomically
        - Tracks outgoing transactions for Level 2 ranking
        - Records transaction history for both accounts (Level 4)
        
        Args:
            timestamp: Stringified timestamp in milliseconds
            source_account_id: Source account identifier
            target_account_id: Target account identifier
            amount: Amount to transfer
            
        Returns:
            Balance of source account after transfer, or None if transfer failed
        """
        # Handle merged accounts: resolve both account IDs to their actual accounts
        # This ensures transfers work correctly even if accounts were merged
        actual_source = self._get_actual_account_id(source_account_id)
        actual_target = self._get_actual_account_id(target_account_id)
        
        # Validate that source account exists
        # Return None if account doesn't exist (error condition)
        if actual_source is None or actual_source not in self.accounts:
            return None
        
        # Validate that target account exists
        # Both accounts must exist for a transfer to succeed
        if actual_target is None or actual_target not in self.accounts:
            return None
        
        # Edge case: prevent transferring to the same account
        # This would be a no-op but we treat it as an error for clarity
        if actual_source == actual_target:
            return None
        
        # Check if source account has sufficient funds
        # This prevents overdrafts
        if self.accounts[actual_source] < amount:
            return None
        
        # Perform the transfer: atomic operation
        # Deduct from source and add to target
        # These operations happen together to maintain consistency
        self.accounts[actual_source] -= amount
        self.accounts[actual_target] += amount
        
        # Track outgoing transactions for Level 2 ranking
        # We only track outgoing (not incoming) for ranking purposes
        # This accumulates the total amount transferred out by each account
        self.outgoing_transactions[actual_source] += amount
        
        # Record transaction history for source account (Level 4)
        # Type is 'transfer_out' to distinguish from incoming transfers
        self.transaction_history[actual_source].append({
            'timestamp': timestamp,
            'type': 'transfer_out',  # Indicates money leaving this account
            'from': actual_source,
            'to': actual_target,
            'amount': amount
        })
        
        # Record transaction history for target account (Level 4)
        # Type is 'transfer_in' to distinguish from outgoing transfers
        self.transaction_history[actual_target].append({
            'timestamp': timestamp,
            'type': 'transfer_in',  # Indicates money entering this account
            'from': actual_source,
            'to': actual_target,
            'amount': amount
        })
        
        # Return the source account's new balance
        return self.accounts[actual_source]
    
    # ==================== LEVEL 2 ====================
    
    def get_top_accounts(self, n: int) -> List[str]:
        """
        Get the top n accounts ranked by total outgoing transaction amount.
        
        TIME COMPLEXITY: O(m log m) where m is the number of accounts with outgoing transactions
        - List comprehension: O(m) to iterate through outgoing_transactions
        - Sorting: O(m log m) - Python's Timsort algorithm
        - Slicing [:n]: O(n) to get top n elements
        - List comprehension to extract IDs: O(n)
        - Total: O(m log m) where m ≤ total number of accounts
        
        SPACE COMPLEXITY: O(m) for the intermediate list of tuples
        
        IMPLEMENTATION NOTES:
        - Only includes accounts with outgoing transactions > 0
        - Sorts by amount (descending), then by account_id (ascending) for ties
        - Uses tuple sorting: (-amount, account_id) for descending amount, ascending ID
        - Returns only the top n account IDs
        
        SORTING EXPLANATION:
        - key=lambda x: (-x[1], x[0]) means:
          * Sort by -x[1] (negative amount) = descending by amount
          * Then by x[0] (account_id) = ascending alphabetically
        - Python's tuple comparison works element by element
        
        Args:
            n: Number of top accounts to return
            
        Returns:
            List of account IDs sorted by outgoing transaction amount (descending)
            If accounts have the same amount, they should be sorted by account_id (ascending)
        """
        # Filter to only accounts with outgoing transactions
        # List comprehension creates tuples of (account_id, amount)
        # We only include accounts with amount > 0 (have made at least one transfer)
        accounts_with_transactions = [
            (account_id, amount) 
            for account_id, amount in self.outgoing_transactions.items()
            if amount > 0  # Only include accounts that have made outgoing transactions
        ]
        
        # Sort by outgoing amount (descending), then by account_id (ascending)
        # The key function returns a tuple: (-amount, account_id)
        # Negative amount means descending order (largest first)
        # Account ID means ascending order (alphabetically first)
        # Python compares tuples element by element
        sorted_accounts = sorted(
            accounts_with_transactions,
            key=lambda x: (-x[1], x[0])  # (-amount, account_id) for desc amount, asc ID
        )
        
        # Return top n account IDs
        # [:n] slices to get first n elements
        # [account_id for account_id, _ in ...] extracts just the account IDs
        return [account_id for account_id, _ in sorted_accounts[:n]]
    
    # ==================== LEVEL 3 ====================
    
    def schedule_payment(self, timestamp: int, source_account_id: str, target_account_id: str, 
                        amount: int, cashback_percentage: float) -> Optional[str]:
        """
        Schedule a payment with cashback.
        
        TIME COMPLEXITY: O(k) where k is the length of merge chain
        - Two _get_actual_account_id() calls: O(k) each
        - Dictionary lookups: O(1) each
        - Dictionary insertion: O(1)
        - List append: O(1)
        - Total: O(k) where k is typically 1 (no merges) or small (few merges)
        
        IMPLEMENTATION NOTES:
        - Reserves (deducts) the amount immediately when scheduled
        - Calculates cashback amount (rounded down to integer)
        - Generates unique payment ID using counter
        - Stores payment details for later execution
        - Records transaction history for Level 4
        
        PAYMENT FLOW:
        1. Schedule: Amount is deducted from source (reserved)
        2. Execute: Amount goes to target, cashback goes to source
        
        Args:
            timestamp: Current timestamp in milliseconds
            source_account_id: Source account identifier
            target_account_id: Target account identifier
            amount: Amount to transfer
            cashback_percentage: Percentage of cashback (e.g., 0.05 for 5%)
            
        Returns:
            Payment ID if successful, None if account doesn't exist or insufficient funds
        """
        # Handle merged accounts: resolve both account IDs
        actual_source = self._get_actual_account_id(source_account_id)
        actual_target = self._get_actual_account_id(target_account_id)
        
        # Validate source account exists
        if actual_source is None or actual_source not in self.accounts:
            return None
        
        # Validate target account exists
        if actual_target is None or actual_target not in self.accounts:
            return None
        
        # Check if source has sufficient funds
        # The amount must be available immediately (it will be reserved)
        if self.accounts[actual_source] < amount:
            return None
        
        # Generate unique payment ID
        # Format: "payment_0", "payment_1", "payment_2", etc.
        # Counter ensures uniqueness across all payments
        payment_id = f"payment_{self.payment_counter}"
        self.payment_counter += 1  # Increment for next payment
        
        # Calculate cashback amount
        # int() truncates (rounds down) to ensure we return an integer
        # Example: 100 * 0.15 = 15.0 -> 15
        # Example: 100 * 0.153 = 15.3 -> 15 (truncated)
        cashback_amount = int(amount * cashback_percentage)
        
        # Reserve the amount (deduct from source immediately)
        # This ensures the funds are available when the payment is executed
        # The money is "locked" until execution
        self.accounts[actual_source] -= amount
        
        # Store scheduled payment details
        # We store all relevant information for execution later
        self.scheduled_payments[payment_id] = {
            'timestamp': timestamp,  # When payment was scheduled
            'source_account_id': actual_source,  # Use actual ID (handles merges)
            'target_account_id': actual_target,  # Use actual ID (handles merges)
            'amount': amount,  # Amount to transfer
            'cashback_percentage': cashback_percentage,  # Original percentage (for reference)
            'cashback_amount': cashback_amount,  # Calculated cashback (for execution)
            'status': 'scheduled'  # Current status: 'scheduled' or 'executed'
        }
        
        # Record transaction history for Level 4
        # This shows that a payment was scheduled (but not yet executed)
        self.transaction_history[actual_source].append({
            'timestamp': timestamp,
            'type': 'scheduled_payment',  # Indicates this is a scheduled payment
            'from': actual_source,
            'to': actual_target,
            'amount': amount,
            'payment_id': payment_id  # Link to payment details
        })
        
        # Return the payment ID so caller can track/execute it later
        return payment_id
    
    def execute_payment(self, timestamp: int, payment_id: str) -> Optional[bool]:
        """
        Execute a scheduled payment.
        
        TIME COMPLEXITY: O(1)
        - Dictionary lookup: O(1)
        - Dictionary updates: O(1) each
        - List appends: O(1) each
        - Total: O(1) constant time
        
        SPACE COMPLEXITY: O(1)
        - Only adds two transaction dictionaries to lists
        - No additional data structures created
        
        IMPLEMENTATION NOTES:
        - Validates payment exists and is in 'scheduled' status
        - Transfers reserved amount to target account
        - Adds cashback to source account
        - Updates payment status to 'executed'
        - Records transaction history for both accounts
        
        EXECUTION FLOW:
        1. Payment was already scheduled (amount deducted from source)
        2. Now: Add amount to target, add cashback to source
        3. Update status to prevent double execution
        
        Args:
            timestamp: Current timestamp in milliseconds
            payment_id: Payment identifier
            
        Returns:
            True if payment was executed successfully, None if payment doesn't exist or already executed
        """
        # Check if payment exists
        if payment_id not in self.scheduled_payments:
            return None
        
        # Get payment details
        payment = self.scheduled_payments[payment_id]
        
        # Check if payment is still in 'scheduled' status
        # If already executed, return None (prevent double execution)
        if payment['status'] != 'scheduled':
            return None
        
        # Extract payment details for clarity
        source = payment['source_account_id']
        target = payment['target_account_id']
        amount = payment['amount']  # Amount to transfer to target
        cashback = payment['cashback_amount']  # Cashback to add to source
        
        # Transfer the reserved amount to target account
        # The amount was already deducted from source during scheduling
        # Now we add it to the target
        self.accounts[target] += amount
        
        # Add cashback to source account
        # This is a bonus/reward for using the payment system
        # Cashback is calculated as a percentage of the payment amount
        self.accounts[source] += cashback
        
        # Update payment status to 'executed'
        # This prevents the payment from being executed again
        payment['status'] = 'executed'
        payment['executed_timestamp'] = timestamp  # Track when it was executed
        
        # Record transaction history for target account (Level 4)
        # This shows the target received the payment
        self.transaction_history[target].append({
            'timestamp': timestamp,
            'type': 'payment_received',  # Indicates money received from a payment
            'from': source,
            'to': target,
            'amount': amount,
            'payment_id': payment_id  # Link to payment details
        })
        
        # Record transaction history for source account (Level 4)
        # This shows the source received cashback
        self.transaction_history[source].append({
            'timestamp': timestamp,
            'type': 'cashback',  # Indicates cashback reward
            'from': None,  # Cashback doesn't come from another account
            'to': source,  # Cashback goes to source account
            'amount': cashback,
            'payment_id': payment_id  # Link to payment details
        })
        
        # Return True to indicate successful execution
        return True
    
    def get_payment_status(self, payment_id: str) -> Optional[str]:
        """
        Get the status of a scheduled payment.
        
        TIME COMPLEXITY: O(1)
        - Dictionary lookup: O(1)
        - Dictionary access: O(1)
        - Total: O(1) constant time
        
        SPACE COMPLEXITY: O(1)
        - No additional space used
        - Only returns a string value
        
        IMPLEMENTATION NOTES:
        - Simple lookup in scheduled_payments dictionary
        - Returns 'scheduled' or 'executed' status
        - Returns None if payment doesn't exist
        
        Args:
            payment_id: Payment identifier
            
        Returns:
            'scheduled' or 'executed', or None if payment doesn't exist
        """
        # Check if payment exists
        if payment_id not in self.scheduled_payments:
            return None
        
        # Return the current status
        # Status is either 'scheduled' (not yet executed) or 'executed' (completed)
        return self.scheduled_payments[payment_id]['status']
    
    # ==================== LEVEL 4 ====================
    
    def merge_accounts(self, timestamp: int, account_id_1: str, account_id_2: str) -> Optional[str]:
        """
        Merge two accounts, retaining both accounts' balance and transaction histories.
        
        TIME COMPLEXITY: O(t log t + p) where:
        - t = total number of transactions in both accounts
        - p = number of scheduled payments
        - k = length of merge chain (for _get_actual_account_id calls)
        
        Breakdown:
        - Two _get_actual_account_id() calls: O(k) each
        - Dictionary lookups: O(1) each
        - Combining transaction lists: O(t) where t is total transactions
        - Sorting transactions: O(t log t) - Python's Timsort
        - Updating scheduled payments: O(p) to iterate through all payments
        - Dictionary operations: O(1) each
        - Total: O(t log t + p + k) ≈ O(t log t + p) in typical cases
        
        SPACE COMPLEXITY: O(t) for the combined transaction list
        
        IMPLEMENTATION NOTES:
        - Determines which account to keep (alphabetically first)
        - Combines balances (sum of both)
        - Merges transaction histories (combines and sorts by timestamp)
        - Combines outgoing transaction amounts
        - Updates merged_accounts mapping for redirection
        - Updates scheduled payments that reference merged account
        - Removes merged account from active accounts
        
        MERGE STRATEGY:
        - Keep the account with alphabetically first ID
        - All operations on the merged account ID redirect to kept account
        - Transaction histories are combined and sorted chronologically
        
        Args:
            timestamp: Current timestamp in milliseconds
            account_id_1: First account identifier
            account_id_2: Second account identifier
            
        Returns:
            The account ID of the merged account, or None if merge failed
        """
        # Handle merged accounts: resolve both account IDs to their actual accounts
        # This handles cases where one or both accounts were previously merged
        actual_1 = self._get_actual_account_id(account_id_1)
        actual_2 = self._get_actual_account_id(account_id_2)
        
        # Validate that first account exists
        if actual_1 is None or actual_1 not in self.accounts:
            return None
        
        # Validate that second account exists
        if actual_2 is None or actual_2 not in self.accounts:
            return None
        
        # Edge case: prevent merging an account with itself
        # After resolving merged accounts, they might be the same
        if actual_1 == actual_2:
            return None
        
        # Determine which account to keep (alphabetically first)
        # This ensures consistent behavior: always keep the "smaller" account ID
        # Example: merge("bob", "alice") -> keep "alice"
        if actual_1 < actual_2:
            keep_account = actual_1
            merge_account = actual_2
        else:
            keep_account = actual_2
            merge_account = actual_1
        
        # Combine balances
        # Add the merged account's balance to the kept account
        combined_balance = self.accounts[keep_account] + self.accounts[merge_account]
        self.accounts[keep_account] = combined_balance
        
        # Merge transaction histories
        # Combine all transactions from both accounts
        all_transactions = (
            self.transaction_history[keep_account] + 
            self.transaction_history[merge_account]
        )
        
        # Sort by timestamp to maintain chronological order
        # This ensures the merged history is in correct time order
        all_transactions.sort(key=lambda x: x['timestamp'])
        
        # Update transaction history for kept account
        # Now contains all transactions from both accounts
        self.transaction_history[keep_account] = all_transactions
        
        # Update outgoing transactions (combine amounts)
        # If the merged account had outgoing transactions, add them to kept account
        if merge_account in self.outgoing_transactions:
            if keep_account in self.outgoing_transactions:
                # Both accounts had outgoing transactions: add them
                self.outgoing_transactions[keep_account] += self.outgoing_transactions[merge_account]
            else:
                # Only merged account had outgoing: copy to kept account
                self.outgoing_transactions[keep_account] = self.outgoing_transactions[merge_account]
            # Remove merged account from outgoing transactions tracking
            del self.outgoing_transactions[merge_account]
        
        # Record merge in transaction history
        # This creates a record of the merge operation itself
        # The amount is the balance that was merged (for reference)
        self.transaction_history[keep_account].append({
            'timestamp': timestamp,
            'type': 'merge',  # Indicates this is a merge operation
            'from': merge_account,  # Account that was merged
            'to': keep_account,  # Account that was kept
            'amount': self.accounts[merge_account]  # Balance that was merged (before deletion)
        })
        
        # Track merged accounts for redirection
        # This allows _get_actual_account_id() to redirect operations
        # Example: merged_accounts["bob"] = "alice" means "bob" redirects to "alice"
        self.merged_accounts[merge_account] = keep_account
        
        # Track which accounts were merged into the kept account (for debugging)
        # This is useful for understanding merge chains
        if merge_account in self.merged_from:
            # If merge_account itself had accounts merged into it, preserve that history
            self.merged_from[keep_account].extend(self.merged_from[merge_account])
        # Add merge_account to the list of accounts merged into keep_account
        self.merged_from[keep_account].append(merge_account)
        
        # Remove the merged account from active accounts
        # The account no longer exists independently, but operations on its ID will redirect
        del self.accounts[merge_account]
        
        # Update scheduled payments that reference the merged account
        # If any scheduled payments have the merged account as source or target,
        # update them to reference the kept account instead
        for payment_id, payment in self.scheduled_payments.items():
            if payment['source_account_id'] == merge_account:
                payment['source_account_id'] = keep_account
            if payment['target_account_id'] == merge_account:
                payment['target_account_id'] = keep_account
        
        # Return the kept account ID (the merged account)
        return keep_account
    
    def get_account_balance(self, account_id: str) -> Optional[int]:
        """
        Get the current balance of an account.
        
        TIME COMPLEXITY: O(k) where k is the length of merge chain
        - _get_actual_account_id(): O(k) worst case (if account was merged multiple times)
        - Dictionary lookup: O(1)
        - Total: O(k) where k is typically 1 (no merges) or small (few merges)
        
        IMPLEMENTATION NOTES:
        - Uses _get_actual_account_id() to handle merged accounts
        - Returns None if account doesn't exist
        - Returns balance if account exists
        
        Args:
            account_id: Account identifier (may be a merged account)
            
        Returns:
            Account balance or None if account doesn't exist
        """
        # Resolve to actual account ID (handles merged accounts)
        actual_account_id = self._get_actual_account_id(account_id)
        
        # Validate account exists
        if actual_account_id is None or actual_account_id not in self.accounts:
            return None
        
        # Return the balance
        return self.accounts[actual_account_id]
    
    def get_transaction_history(self, account_id: str) -> Optional[List[Dict]]:
        """
        Get the transaction history of an account.
        
        TIME COMPLEXITY: O(k + t) where:
        - k = length of merge chain
        - t = number of transactions in the account
        
        Breakdown:
        - _get_actual_account_id(): O(k) worst case
        - Dictionary lookup: O(1)
        - List copy: O(t) where t is number of transactions
        - Total: O(k + t)
        
        SPACE COMPLEXITY: O(t) for the copied list
        
        IMPLEMENTATION NOTES:
        - Uses _get_actual_account_id() to handle merged accounts
        - Returns a copy to prevent external modification
        - Includes all transactions from merged accounts (already combined during merge)
        
        Args:
            account_id: Account identifier (may be a merged account)
            
        Returns:
            List of transactions or None if account doesn't exist
        """
        # Resolve to actual account ID (handles merged accounts)
        actual_account_id = self._get_actual_account_id(account_id)
        
        # Validate account exists
        if actual_account_id is None or actual_account_id not in self.accounts:
            return None
        
        # Return a copy to prevent external modification
        # If we returned the list directly, caller could modify it
        # .copy() creates a shallow copy (sufficient for this use case)
        return self.transaction_history[actual_account_id].copy()
    
    # ==================== HELPER METHODS ====================
    
    def _get_actual_account_id(self, account_id: str) -> Optional[str]:
        """
        Get the actual account ID, handling merged accounts.
        
        TIME COMPLEXITY: O(k) where k is the length of the merge chain
        - Fast path (account exists directly): O(1) - single dictionary lookup
        - Slow path (following merge chain): O(k) where k is number of merges in chain
        - Worst case: O(k) when account was merged k times
        - Best case: O(1) when account exists directly (no merges)
        - Average case: O(1) in practice (most accounts are not merged)
        
        SPACE COMPLEXITY: O(k) for the visited set (only in worst case)
        
        IMPLEMENTATION NOTES:
        - This is a critical helper method used throughout the codebase
        - Handles the redirection chain when accounts are merged
        - Prevents infinite loops with visited set (circular reference protection)
        - Returns None if account doesn't exist (even after following merge chain)
        
        MERGE CHAIN EXAMPLE:
        - If "bob" was merged into "alice", then "alice" was merged into "charlie"
        - merged_accounts = {"bob": "alice", "alice": "charlie"}
        - _get_actual_account_id("bob") -> follows chain: "bob" -> "alice" -> "charlie"
        - Returns "charlie" (the actual account)
        
        Args:
            account_id: Account identifier (may be a merged account)
            
        Returns:
            Actual account ID or None if account doesn't exist
        """
        # Fast path: if account exists directly, return it immediately
        # This is the common case (most accounts are not merged)
        if account_id in self.accounts:
            return account_id
        
        # Slow path: account might be merged, follow the chain
        # Start with the given account_id
        current = account_id
        visited = set()  # Track visited accounts to prevent infinite loops
        
        # Follow the merge chain until we find an account that exists
        # or until we detect a circular reference
        while current in self.merged_accounts:
            # Safety check: detect circular references
            # This shouldn't happen in normal operation, but protects against bugs
            if current in visited:
                # Circular reference detected (shouldn't happen, but safety check)
                return None
            
            # Mark current as visited
            visited.add(current)
            
            # Move to the next account in the chain
            current = self.merged_accounts[current]
        
        # Check if the final account exists
        # After following the chain, we should have the actual account
        if current in self.accounts:
            return current
        
        # Account doesn't exist (not in accounts and not in merge chain)
        return None
    
    def get_outgoing_transactions(self, account_id: str) -> Optional[int]:
        """
        Get the total outgoing transaction amount for an account.
        
        TIME COMPLEXITY: O(k) where k is the length of merge chain
        - _get_actual_account_id(): O(k) worst case
        - Dictionary get() with default: O(1)
        - Total: O(k) where k is typically 1 (no merges) or small (few merges)
        
        SPACE COMPLEXITY: O(1)
        - Only returns an integer value
        - No additional data structures created
        
        IMPLEMENTATION NOTES:
        - Uses _get_actual_account_id() to handle merged accounts
        - Returns 0 if account exists but has no outgoing transactions
        - Returns None if account doesn't exist
        
        Args:
            account_id: Account identifier (may be a merged account)
            
        Returns:
            Total outgoing transaction amount, or None if account doesn't exist
        """
        # Resolve to actual account ID (handles merged accounts)
        actual_account_id = self._get_actual_account_id(account_id)
        
        # Validate account exists
        if actual_account_id is None:
            return None
        
        # Return outgoing transaction amount (defaults to 0 if not found)
        # .get() with default 0 handles accounts that haven't made any transfers
        return self.outgoing_transactions.get(actual_account_id, 0)
    
    def debug_state(self) -> str:
        """
        Return a string representation of the current system state for debugging.
        
        TIME COMPLEXITY: O(a + p + m) where:
        - a = number of accounts
        - p = number of scheduled payments
        - m = number of merged accounts
        - t = total number of accounts with transaction history
        
        Breakdown:
        - Iterating through accounts: O(a)
        - Iterating through outgoing transactions: O(a) (at most one per account)
        - Iterating through scheduled payments: O(p)
        - Iterating through merged accounts: O(m)
        - Iterating through transaction history: O(t)
        - Sorting operations: O(a log a) for accounts, O(p log p) for payments, etc.
        - Total: O(a log a + p log p + m log m + t) ≈ O(n log n) where n is total items
        
        SPACE COMPLEXITY: O(s) where s is the size of the output string
        
        IMPLEMENTATION NOTES:
        - Useful for debugging and understanding system state
        - Shows all accounts, balances, transactions, payments, and merges
        - Formatted for easy reading
        
        Returns:
            Formatted string showing accounts, balances, transactions, etc.
        """
        lines = []
        lines.append("=" * 60)
        lines.append("BANKING SYSTEM STATE")
        lines.append("=" * 60)
        
        # Display all accounts and their balances
        lines.append(f"\nAccounts ({len(self.accounts)}):")
        for account_id, balance in sorted(self.accounts.items()):
            lines.append(f"  {account_id}: ${balance}")
        
        # Display outgoing transactions (only accounts with transactions > 0)
        lines.append(f"\nOutgoing Transactions ({len(self.outgoing_transactions)}):")
        for account_id, amount in sorted(self.outgoing_transactions.items()):
            if amount > 0:
                lines.append(f"  {account_id}: ${amount}")
        
        # Display scheduled payments and their status
        lines.append(f"\nScheduled Payments ({len(self.scheduled_payments)}):")
        for payment_id, payment in sorted(self.scheduled_payments.items()):
            lines.append(f"  {payment_id}: {payment.get('status', 'unknown')} - ${payment.get('amount', 0)}")
        
        # Display merged accounts (redirect mappings)
        lines.append(f"\nMerged Accounts ({len(self.merged_accounts)}):")
        for old_id, new_id in sorted(self.merged_accounts.items()):
            lines.append(f"  {old_id} -> {new_id}")
        
        # Display transaction history counts
        lines.append(f"\nTransaction History:")
        for account_id, transactions in sorted(self.transaction_history.items()):
            lines.append(f"  {account_id}: {len(transactions)} transactions")
        
        lines.append("=" * 60)
        return "\n".join(lines)
