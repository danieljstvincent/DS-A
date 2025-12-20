"""
Demo script showing how to use the Banking System
This demonstrates all 4 levels of functionality.
"""

from banking_system import BankingSystem


def print_separator(level: int):
    """Print a visual separator for each level"""
    print("\n" + "=" * 60)
    print(f"LEVEL {level}")
    print("=" * 60 + "\n")


def main():
    bank = BankingSystem()
    
    # ==================== LEVEL 1 ====================
    print_separator(1)
    print("Creating accounts and making transactions...")
    
    # Create accounts
    print("\n1. Creating accounts:")
    bank.create_account(1000, "alice")
    bank.create_account(2000, "bob")
    bank.create_account(3000, "charlie")
    print("   ✓ Created accounts: alice, bob, charlie")
    
    # Make deposits
    print("\n2. Making deposits:")
    bank.deposit(4000, "alice", 1000)
    bank.deposit(5000, "bob", 500)
    bank.deposit(6000, "charlie", 300)
    print(f"   ✓ Alice balance: ${bank.get_account_balance('alice')}")
    print(f"   ✓ Bob balance: ${bank.get_account_balance('bob')}")
    print(f"   ✓ Charlie balance: ${bank.get_account_balance('charlie')}")
    
    # Make transfers
    print("\n3. Making transfers:")
    bank.transfer(7000, "alice", "bob", 200)
    bank.transfer(8000, "bob", "charlie", 100)
    print(f"   ✓ Transferred $200 from alice to bob")
    print(f"   ✓ Transferred $100 from bob to charlie")
    print(f"   ✓ Alice balance: ${bank.get_account_balance('alice')}")
    print(f"   ✓ Bob balance: ${bank.get_account_balance('bob')}")
    print(f"   ✓ Charlie balance: ${bank.get_account_balance('charlie')}")
    
    # ==================== LEVEL 2 ====================
    print_separator(2)
    print("Ranking accounts by outgoing transactions...")
    
    top_accounts = bank.get_top_accounts(5)
    print(f"\nTop accounts by outgoing transactions:")
    for i, account_id in enumerate(top_accounts, 1):
        outgoing = bank.get_outgoing_transactions(account_id)
        if outgoing is not None:
            print(f"   {i}. {account_id}: ${outgoing} in outgoing transactions")
    
    # ==================== LEVEL 3 ====================
    print_separator(3)
    print("Scheduling payments with cashback...")
    
    # Schedule a payment
    print("\n1. Scheduling payment:")
    payment_id = bank.schedule_payment(9000, "alice", "bob", 300, 0.10)
    print(f"   ✓ Scheduled payment: {payment_id}")
    print(f"   ✓ Payment status: {bank.get_payment_status(payment_id)}")
    print(f"   ✓ Alice balance (after reservation): ${bank.get_account_balance('alice')}")
    
    # Execute the payment
    print("\n2. Executing payment:")
    bank.execute_payment(10000, payment_id)
    print(f"   ✓ Payment executed: {payment_id}")
    print(f"   ✓ Payment status: {bank.get_payment_status(payment_id)}")
    print(f"   ✓ Alice balance (with cashback): ${bank.get_account_balance('alice')}")
    print(f"   ✓ Bob balance (after receiving): ${bank.get_account_balance('bob')}")
    
    # ==================== LEVEL 4 ====================
    print_separator(4)
    print("Merging accounts...")
    
    print("\n1. Before merge:")
    print(f"   ✓ Alice balance: ${bank.get_account_balance('alice')}")
    print(f"   ✓ Bob balance: ${bank.get_account_balance('bob')}")
    print(f"   ✓ Alice transactions: {len(bank.get_transaction_history('alice'))}")
    print(f"   ✓ Bob transactions: {len(bank.get_transaction_history('bob'))}")
    
    # Merge accounts
    print("\n2. Merging alice and bob:")
    merged_id = bank.merge_accounts(11000, "alice", "bob")
    print(f"   ✓ Merged into: {merged_id}")
    print(f"   ✓ Merged account balance: ${bank.get_account_balance(merged_id)}")
    print(f"   ✓ Total transactions: {len(bank.get_transaction_history(merged_id))}")
    
    # Access through merged account ID
    print("\n3. Accessing through merged account ID:")
    print(f"   ✓ Accessing 'bob' redirects to merged account: ${bank.get_account_balance('bob')}")
    
    print("\n" + "=" * 60)
    print("Demo completed successfully!")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()

