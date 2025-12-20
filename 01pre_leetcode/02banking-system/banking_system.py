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
        # Level 1: Basic account management
        # Store account balances: account_id -> balance
        self.accounts: Dict[str, int] = {}
        
        # Level 2: Transaction tracking for ranking
        # Track total outgoing transaction amounts: account_id -> total_outgoing_amount
        self.outgoing_transactions: Dict[str, int] = defaultdict(int)
        
        # Level 3: Scheduled payments
        # Store scheduled payment details: payment_id -> payment_info
        self.scheduled_payments: Dict[str, Dict] = {}
        # Counter for generating unique payment IDs
        self.payment_counter = 0
        
        # Level 4: Transaction history and account merging
        # Store transaction history: account_id -> list of transactions
        self.transaction_history: Dict[str, List[Dict]] = defaultdict(list)
        # Track merged accounts: old_account_id -> new_account_id
        self.merged_accounts: Dict[str, str] = {}
    
    # ==================== LEVEL 1 ====================
    
    def create_account(self, timestamp: int, account_id: str) -> bool:
        """
        Create a new account with the given identifier.
        
        Args:
            timestamp: Timestamp in milliseconds (not used in Level 1, but needed for Level 4)
            account_id: Unique identifier for the account
            
        Returns:
            True if account was successfully created, False if account already exists
            
        Note:
            - Initially, accounts have a balance of 0
            - Check if account already exists (including merged accounts)
        """
        pass
    
    def deposit(self, timestamp: int, account_id: str, amount: int) -> Optional[int]:
        """
        Deposit money into the specified account.
        
        Args:
            timestamp: Timestamp in milliseconds (needed for transaction history in Level 4)
            account_id: Identifier of the account
            amount: Amount to deposit (must be positive)
            
        Returns:
            Balance of the account after deposit, or None if account doesn't exist
            
        Note:
            - Handle merged accounts using _get_actual_account_id() helper
            - Record transaction history for Level 4
        """
        pass
    
    def transfer(self, timestamp: int, source_account_id: str, target_account_id: str, amount: int) -> Optional[int]:
        """
        Transfer money from source account to target account.
        
        Args:
            timestamp: Timestamp in milliseconds (needed for transaction history in Level 4)
            source_account_id: Source account identifier
            target_account_id: Target account identifier
            amount: Amount to transfer (must be positive)
            
        Returns:
            Balance of source account after transfer, or None if transfer failed
            
        Returns None if:
            - source_account_id or target_account_id doesn't exist
            - source_account_id and target_account_id are the same
            - source_account_id has insufficient funds
            
        Note:
            - Handle merged accounts using _get_actual_account_id() helper
            - Track outgoing transactions for Level 2 ranking
            - Record transaction history for Level 4
        """
        pass
    
    # ==================== LEVEL 2 ====================
    
    def get_top_accounts(self, n: int) -> List[str]:
        """
        Get the top n accounts ranked by total outgoing transaction amount.
        
        Args:
            n: Number of top accounts to return
            
        Returns:
            List of account IDs sorted by:
            1. Outgoing transaction amount (descending)
            2. Account ID (ascending, alphabetically) for ties
            
        Note:
            - Only accounts that have made at least one outgoing transaction should be included
            - Use self.outgoing_transactions to get the amounts
        """
        pass
    
    # ==================== LEVEL 3 ====================
    
    def schedule_payment(self, timestamp: int, source_account_id: str, target_account_id: str, 
                        amount: int, cashback_percentage: float) -> Optional[str]:
        """
        Schedule a payment with cashback.
        
        Args:
            timestamp: Timestamp in milliseconds
            source_account_id: Source account identifier
            target_account_id: Target account identifier
            amount: Amount to transfer
            cashback_percentage: Percentage of cashback (e.g., 0.05 for 5%, 0.10 for 10%)
            
        Returns:
            Payment ID (string) if successful, None if account doesn't exist or insufficient funds
            
        Note:
            - The amount should be reserved (deducted) from source account immediately
            - Generate unique payment ID: "payment_0", "payment_1", etc.
            - Calculate cashback amount: int(amount * cashback_percentage)
            - Store payment details in self.scheduled_payments
            - Record transaction history for Level 4
        """
        pass
    
    def execute_payment(self, timestamp: int, payment_id: str) -> Optional[bool]:
        """
        Execute a scheduled payment.
        
        Args:
            timestamp: Timestamp in milliseconds
            payment_id: Payment identifier
            
        Returns:
            True if payment was executed successfully, None if payment doesn't exist or already executed
            
        Note:
            - When executed:
              * Transfer the reserved amount to target account
              * Add cashback to source account
            - Update payment status to 'executed'
            - Record transaction history for Level 4
        """
        pass
    
    def get_payment_status(self, payment_id: str) -> Optional[str]:
        """
        Get the status of a scheduled payment.
        
        Args:
            payment_id: Payment identifier
            
        Returns:
            'scheduled' if payment has been scheduled but not executed
            'executed' if payment has been executed
            None if payment_id doesn't exist
        """
        pass
    
    # ==================== LEVEL 4 ====================
    
    def merge_accounts(self, timestamp: int, account_id_1: str, account_id_2: str) -> Optional[str]:
        """
        Merge two accounts, retaining both accounts' balance and transaction histories.
        
        Args:
            timestamp: Timestamp in milliseconds
            account_id_1: First account identifier
            account_id_2: Second account identifier
            
        Returns:
            The account ID of the merged account (alphabetically first), or None if merge failed
            
        Returns None if:
            - account_id_1 or account_id_2 doesn't exist
            - account_id_1 and account_id_2 are the same
            
        Note:
            - The merged account should:
              * Have combined balance (sum of both accounts)
              * Retain complete transaction history from both accounts
              * Use the account_id that comes first alphabetically
            - After merging, operations using the merged account's original ID should redirect
            - Update self.merged_accounts to track the merge
            - Update scheduled payments that reference the merged account
            - Combine outgoing transaction amounts
        """
        pass
    
    def get_account_balance(self, account_id: str) -> Optional[int]:
        """
        Get the current balance of an account.
        
        Args:
            account_id: Account identifier (may be a merged account)
            
        Returns:
            Account balance, or None if account doesn't exist
            
        Note:
            - Should handle merged accounts (redirect to actual account)
        """
        pass
    
    def get_transaction_history(self, account_id: str) -> Optional[List[Dict]]:
        """
        Get the complete transaction history of an account.
        
        Args:
            account_id: Account identifier (may be a merged account)
            
        Returns:
            List of transaction dictionaries, or None if account doesn't exist
            
        Note:
            - Should include all transactions from the account
            - Should include transactions from accounts that were merged into it
            - Each transaction should be a dictionary with relevant information
            - Return a copy to prevent external modification
        """
        pass
    
    # ==================== HELPER METHODS ====================
    
    def _get_actual_account_id(self, account_id: str) -> Optional[str]:
        """
        Get the actual account ID, handling merged accounts.
        
        This helper method resolves merged account IDs to their actual account.
        If an account was merged into another, it returns the account it was merged into.
        
        Args:
            account_id: Account identifier (may be a merged account)
            
        Returns:
            Actual account ID, or None if account doesn't exist
            
        Note:
            - If account exists directly, return it
            - If account was merged, follow the chain to find the actual account
            - Handle potential circular references (safety check)
        """
        pass
    
    def get_outgoing_transactions(self, account_id: str) -> Optional[int]:
        """
        Get the total outgoing transaction amount for an account.
        
        Args:
            account_id: Account identifier (may be a merged account)
            
        Returns:
            Total outgoing transaction amount, or None if account doesn't exist
        """
        actual_account_id = self._get_actual_account_id(account_id)
        if actual_account_id is None:
            return None
        return self.outgoing_transactions.get(actual_account_id, 0)
    
    def debug_state(self) -> str:
        """
        Return a string representation of the current system state for debugging.
        
        Returns:
            Formatted string showing accounts, balances, transactions, etc.
        """
        lines = []
        lines.append("=" * 60)
        lines.append("BANKING SYSTEM STATE")
        lines.append("=" * 60)
        lines.append(f"\nAccounts ({len(self.accounts)}):")
        for account_id, balance in sorted(self.accounts.items()):
            lines.append(f"  {account_id}: ${balance}")
        
        lines.append(f"\nOutgoing Transactions ({len(self.outgoing_transactions)}):")
        for account_id, amount in sorted(self.outgoing_transactions.items()):
            if amount > 0:
                lines.append(f"  {account_id}: ${amount}")
        
        lines.append(f"\nScheduled Payments ({len(self.scheduled_payments)}):")
        for payment_id, payment in sorted(self.scheduled_payments.items()):
            lines.append(f"  {payment_id}: {payment.get('status', 'unknown')} - ${payment.get('amount', 0)}")
        
        lines.append(f"\nMerged Accounts ({len(self.merged_accounts)}):")
        for old_id, new_id in sorted(self.merged_accounts.items()):
            lines.append(f"  {old_id} -> {new_id}")
        
        lines.append(f"\nTransaction History:")
        for account_id, transactions in sorted(self.transaction_history.items()):
            lines.append(f"  {account_id}: {len(transactions)} transactions")
        
        lines.append("=" * 60)
        return "\n".join(lines)
