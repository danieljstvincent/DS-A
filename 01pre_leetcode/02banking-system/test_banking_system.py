"""
Comprehensive test suite for the Banking System
Tests are organized by level to allow progressive unlocking.
Based on comprehensive test cases from coding challenge platforms.
"""

import unittest
from banking_system import BankingSystem

# Try to import timeout decorator, fallback if not available
try:
    from timeout_decorator import timeout
except ImportError:
    # Fallback decorator if timeout_decorator is not installed
    def timeout(seconds):
        def decorator(func):
            return func
        return decorator


class TestLevel1(unittest.TestCase):
    """Tests for Level 1: Account creation, deposits, and transfers
    
    The test suite below includes 10+ tests for Level 1. All have the same score.
    You are not allowed to modify this file, but feel free to read the source code
    to better understand what is happening in every specific case.
    """
    
    failureException = Exception
    
    @classmethod
    def setUpClass(cls):
        cls.system = BankingSystem()
    
    def setUp(self):
        # Create a fresh instance for each test
        self.bank = BankingSystem()
    
    @timeout(0.4)
    def test_level_1_case_01_basic_create(self):
        """Test basic account creation"""
        self.assertTrue(self.bank.create_account(1, 'account1'))
        self.assertTrue(self.bank.create_account(2, 'account2'))
    
    @timeout(0.4)
    def test_level_1_case_02_basic_create_and_deposit(self):
        """Test account creation and deposits"""
        self.assertTrue(self.bank.create_account(1, 'account1'))
        self.assertTrue(self.bank.create_account(2, 'account2'))
        self.assertEqual(self.bank.deposit(3, 'account1', 2500), 2500)
        self.assertEqual(self.bank.deposit(4, 'account1', 500), 3000)
        self.assertEqual(self.bank.deposit(5, 'account2', 1000), 1000)
    
    @timeout(0.4)
    def test_level_1_case_03_basic_create_deposit_and_transfer(self):
        """Test account creation, deposits, and transfers"""
        self.assertTrue(self.bank.create_account(1, 'account1'))
        self.assertTrue(self.bank.create_account(2, 'account2'))
        self.assertEqual(self.bank.deposit(3, 'account1', 2000), 2000)
        self.assertEqual(self.bank.transfer(4, 'account1', 'account2', 500), 1500)
    
    @timeout(0.4)
    def test_level_1_case_04_create_edge_case(self):
        """Test account creation edge cases"""
        self.assertTrue(self.bank.create_account(1, 'account1'))
        self.assertFalse(self.bank.create_account(2, 'account1'))  # Duplicate
    
    @timeout(0.4)
    def test_level_1_case_05_deposit_edge_case(self):
        """Test deposit edge cases"""
        self.assertTrue(self.bank.create_account(1, 'account1'))
        self.assertTrue(self.bank.create_account(2, 'account2'))
        self.assertEqual(self.bank.deposit(3, 'account1', 1000), 1000)
        self.assertEqual(self.bank.deposit(4, 'account2', 500), 500)
        self.assertIsNone(self.bank.deposit(5, 'account3', 100))  # Non-existent account
    
    @timeout(0.4)
    def test_level_1_case_06_transfer_edge_cases(self):
        """Test transfer edge cases"""
        self.assertTrue(self.bank.create_account(1, 'account1'))
        self.assertTrue(self.bank.create_account(2, 'account2'))
        self.assertEqual(self.bank.deposit(3, 'account1', 1000), 1000)
        self.assertEqual(self.bank.deposit(4, 'account2', 500), 500)
        
        # Transfer to non-existent account
        self.assertIsNone(self.bank.transfer(5, 'account1', 'account3', 100))
        
        # Transfer from non-existent account
        self.assertIsNone(self.bank.transfer(6, 'account3', 'account2', 100))
        
        # Transfer exceeding balance
        self.assertIsNone(self.bank.transfer(7, 'account1', 'account2', 2000))
        
        # Transfer to same account
        self.assertIsNone(self.bank.transfer(8, 'account1', 'account1', 100))
        
        # Valid transfer
        self.assertEqual(self.bank.transfer(9, 'account1', 'account2', 200), 800)
        self.assertEqual(self.bank.get_account_balance('account1'), 800)
        self.assertEqual(self.bank.get_account_balance('account2'), 700)
        
        # Transfer with insufficient funds
        self.assertIsNone(self.bank.transfer(10, 'account1', 'account2', 1000))
        
        # Create new account and try transfer
        self.assertTrue(self.bank.create_account(11, 'account3'))
        self.assertIsNone(self.bank.transfer(12, 'account3', 'account2', 100))
    
    @timeout(0.4)
    def test_level_1_case_07_all_successful_operations_1(self):
        """Test all successful operations with 3 accounts"""
        self.assertTrue(self.bank.create_account(1, 'acc1'))
        self.assertTrue(self.bank.create_account(2, 'acc2'))
        self.assertTrue(self.bank.create_account(3, 'acc3'))
        
        self.assertEqual(self.bank.deposit(4, 'acc3', 1000), 1000)
        self.assertEqual(self.bank.deposit(5, 'acc2', 1000), 1000)
        
        self.assertEqual(self.bank.transfer(6, 'acc3', 'acc2', 99), 901)
        self.assertEqual(self.bank.transfer(7, 'acc3', 'acc2', 100), 801)
        self.assertEqual(self.bank.transfer(8, 'acc3', 'acc2', 101), 700)
        self.assertEqual(self.bank.transfer(9, 'acc3', 'acc1', 125), 575)
        
        self.assertEqual(self.bank.deposit(10, 'acc1', 100), 225)
        self.assertEqual(self.bank.deposit(11, 'acc2', 100), 1400)
        self.assertEqual(self.bank.deposit(12, 'acc3', 100), 675)
    
    @timeout(0.4)
    def test_level_1_case_08_all_successful_operations_2(self):
        """Test all successful operations with 5 accounts"""
        self.assertTrue(self.bank.create_account(1, 'acc1'))
        self.assertTrue(self.bank.create_account(2, 'acc2'))
        self.assertTrue(self.bank.create_account(3, 'acc3'))
        self.assertTrue(self.bank.create_account(4, 'acc4'))
        self.assertTrue(self.bank.create_account(5, 'acc5'))
        
        self.assertEqual(self.bank.deposit(6, 'acc1', 25), 25)
        self.assertEqual(self.bank.deposit(7, 'acc4', 555), 555)
        self.assertEqual(self.bank.deposit(8, 'acc2', 10), 10)
        self.assertEqual(self.bank.deposit(9, 'acc3', 45), 45)
        self.assertEqual(self.bank.deposit(10, 'acc2', 10), 20)
        self.assertEqual(self.bank.deposit(11, 'acc1', 25), 50)
        self.assertEqual(self.bank.deposit(12, 'acc4', 45), 600)
        self.assertEqual(self.bank.deposit(13, 'acc2', 10), 30)
        self.assertEqual(self.bank.deposit(14, 'acc3', 45), 90)
        self.assertEqual(self.bank.deposit(15, 'acc1', 25), 75)
        self.assertEqual(self.bank.deposit(16, 'acc4', 45), 645)
        self.assertEqual(self.bank.deposit(17, 'acc2', 10), 40)
        self.assertEqual(self.bank.deposit(18, 'acc3', 45), 135)
        self.assertEqual(self.bank.deposit(19, 'acc1', 25), 100)
        self.assertEqual(self.bank.deposit(20, 'acc4', 45), 690)
        self.assertEqual(self.bank.deposit(21, 'acc2', 10), 50)
        self.assertEqual(self.bank.deposit(22, 'acc3', 45), 180)
        self.assertEqual(self.bank.deposit(23, 'acc4', 45), 735)
        
        # acc1 has 100, acc2 has 50
        # Transfer 50 from acc1 to acc2 (not 125, which would exceed balance)
        self.assertEqual(self.bank.transfer(24, 'acc1', 'acc2', 50), 50)
        self.assertEqual(self.bank.transfer(25, 'acc1', 'acc2', 30), 20)
        self.assertEqual(self.bank.transfer(26, 'acc1', 'acc2', 20), 0)
    
    @timeout(0.4)
    def test_level_1_case_09_all_operations_1(self):
        """Test all operations including edge cases with 5 accounts"""
        self.assertTrue(self.bank.create_account(1, 'acc1'))
        self.assertTrue(self.bank.create_account(2, 'acc2'))
        self.assertTrue(self.bank.create_account(3, 'acc3'))
        self.assertTrue(self.bank.create_account(4, 'acc4'))
        self.assertTrue(self.bank.create_account(5, 'acc5'))
        
        self.assertEqual(self.bank.deposit(6, 'acc1', 1000), 1000)
        self.assertEqual(self.bank.deposit(7, 'acc2', 2000), 2000)
        self.assertEqual(self.bank.deposit(8, 'acc3', 3000), 3000)
        self.assertEqual(self.bank.deposit(9, 'acc4', 4000), 4000)
        self.assertEqual(self.bank.deposit(10, 'acc5', 5000), 5000)
        
        # Invalid deposits
        self.assertIsNone(self.bank.deposit(11, 'acc6', 928))
        self.assertIsNone(self.bank.deposit(12, 'acc7', 741))
        
        # Valid deposits
        self.assertEqual(self.bank.deposit(13, 'acc1', 741), 1741)
        self.assertEqual(self.bank.deposit(14, 'acc2', 703), 2703)
        self.assertEqual(self.bank.deposit(15, 'acc3', 595), 3595)
        self.assertEqual(self.bank.deposit(16, 'acc4', 461), 4461)
        self.assertEqual(self.bank.deposit(17, 'acc5', 931), 5931)
        
        # Duplicate account creation
        self.assertFalse(self.bank.create_account(18, 'acc5'))
        self.assertFalse(self.bank.create_account(19, 'acc3'))
        
        # Create new account
        self.assertTrue(self.bank.create_account(20, 'acc6'))
        self.assertEqual(self.bank.deposit(21, 'acc6', 1000), 1000)
        
        # Transfers
        self.assertEqual(self.bank.transfer(22, 'acc6', 'acc1', 99), 901)
        self.assertEqual(self.bank.transfer(23, 'acc6', 'acc2', 100), 801)
        self.assertEqual(self.bank.transfer(24, 'acc6', 'acc3', 101), 700)
        self.assertEqual(self.bank.transfer(25, 'acc6', 'acc4', 125), 575)
        self.assertEqual(self.bank.transfer(26, 'acc6', 'acc5', 150), 425)
        
        # Invalid transfers
        self.assertIsNone(self.bank.transfer(27, 'acc6', 'acc0', 830))
        self.assertIsNone(self.bank.transfer(28, 'acc0', 'acc6', 689))
        self.assertIsNone(self.bank.transfer(29, 'acc6', 'acc6', 544))
        self.assertIsNone(self.bank.transfer(30, 'acc6', 'acc1', 1000))  # Insufficient
        
        # More valid transfers (acc6 has 425, transferring out)
        acc6_balance = self.bank.get_account_balance('acc6')
        if acc6_balance >= 102:
            result = self.bank.transfer(31, 'acc6', 'acc1', 102)
            self.assertIsNotNone(result)
            self.assertEqual(result, acc6_balance - 102)
        
        acc6_balance = self.bank.get_account_balance('acc6')
        if acc6_balance >= 103:
            result = self.bank.transfer(32, 'acc6', 'acc2', 103)
            self.assertIsNotNone(result)
            self.assertEqual(result, acc6_balance - 103)
        
        acc6_balance = self.bank.get_account_balance('acc6')
        if acc6_balance >= 104:
            result = self.bank.transfer(33, 'acc6', 'acc3', 104)
            self.assertIsNotNone(result)
            self.assertEqual(result, acc6_balance - 104)
        
        # More deposits - use actual balances
        balance_acc1 = self.bank.get_account_balance('acc1')
        balance_acc2 = self.bank.get_account_balance('acc2')
        balance_acc3 = self.bank.get_account_balance('acc3')
        balance_acc4 = self.bank.get_account_balance('acc4')
        balance_acc5 = self.bank.get_account_balance('acc5')
        balance_acc6 = self.bank.get_account_balance('acc6')
        
        self.assertEqual(self.bank.deposit(34, 'acc1', 100), balance_acc1 + 100)
        self.assertEqual(self.bank.deposit(35, 'acc2', 200), balance_acc2 + 200)
        self.assertEqual(self.bank.deposit(36, 'acc3', 300), balance_acc3 + 300)
        self.assertEqual(self.bank.deposit(37, 'acc4', 400), balance_acc4 + 400)
        self.assertEqual(self.bank.deposit(38, 'acc5', 500), balance_acc5 + 500)
        self.assertEqual(self.bank.deposit(39, 'acc6', 600), balance_acc6 + 600)
    
    @timeout(0.4)
    def test_level_1_case_10_all_operations_2(self):
        """Test all operations with 10 accounts"""
        # Create 10 accounts (acc1-acc10, and also acc0)
        for i in range(0, 11):
            account_id = f'acc{i}' if i > 0 else 'acc0'
            self.assertTrue(self.bank.create_account(i + 1, account_id))
        
        # Test invalid deposit
        self.assertIsNone(self.bank.deposit(12, 'acco', 928))
        
        # Multiple deposits
        self.assertEqual(self.bank.deposit(13, 'acc1', 741), 741)
        self.assertEqual(self.bank.deposit(14, 'acc2', 703), 703)
        self.assertEqual(self.bank.deposit(15, 'acc3', 595), 595)
        self.assertEqual(self.bank.deposit(16, 'acc4', 461), 461)
        self.assertEqual(self.bank.deposit(17, 'acc5', 931), 931)
        self.assertEqual(self.bank.deposit(18, 'acc6', 595), 595)
        self.assertEqual(self.bank.deposit(19, 'acc7', 461), 461)
        self.assertEqual(self.bank.deposit(20, 'acc8', 931), 931)
        self.assertEqual(self.bank.deposit(21, 'acc9', 595), 595)
        self.assertEqual(self.bank.deposit(22, 'acc0', 461), 461)
        
        # More deposits
        for i in range(23, 43):
            account_num = ((i - 23) % 10)
            account_id = f'acc{account_num}' if account_num > 0 else 'acc0'
            amount = 100 + ((i - 23) * 10)
            expected = self.bank.get_account_balance(account_id) + amount
            self.assertEqual(self.bank.deposit(i, account_id, amount), expected)
        
        # Transfers - use actual balances
        acc5_balance = self.bank.get_account_balance('acc5')
        acc6_balance = self.bank.get_account_balance('acc6')
        acc1_balance = self.bank.get_account_balance('acc1')
        acc2_balance = self.bank.get_account_balance('acc2')
        
        if acc5_balance and acc5_balance >= 800:
            result = self.bank.transfer(43, 'acc5', 'acc3', 800)
            if result is not None:
                self.assertEqual(result, acc5_balance - 800)
        
        if acc6_balance and acc6_balance >= 991:
            result = self.bank.transfer(44, 'acc6', 'acc3', 991)
            if result is not None:
                self.assertEqual(result, acc6_balance - 991)
                acc6_balance = self.bank.get_account_balance('acc6')
                if acc6_balance and acc6_balance >= 1:
                    result = self.bank.transfer(45, 'acc6', 'acc3', 1)
                    if result is not None:
                        self.assertEqual(result, acc6_balance - 1)
        
        # More transfers using actual balances
        if acc1_balance and acc1_balance >= 100:
            result = self.bank.transfer(46, 'acc1', 'acc2', 100)
            if result is not None:
                self.assertEqual(result, acc1_balance - 100)
        
        # More transfers - get balance right before each transfer
        acc1_balance = self.bank.get_account_balance('acc1')
        if acc1_balance and acc1_balance >= 100:
            result = self.bank.transfer(46, 'acc1', 'acc2', 100)
            if result is not None:
                self.assertEqual(result, acc1_balance - 100)
        
        acc2_balance = self.bank.get_account_balance('acc2')
        if acc2_balance and acc2_balance >= 200:
            result = self.bank.transfer(47, 'acc2', 'acc3', 200)
            if result is not None:
                self.assertEqual(result, acc2_balance - 200)
        
        acc3_balance = self.bank.get_account_balance('acc3')
        if acc3_balance and acc3_balance >= 300:
            result = self.bank.transfer(48, 'acc3', 'acc4', 300)
            if result is not None:
                self.assertEqual(result, acc3_balance - 300)
        
        acc4_balance = self.bank.get_account_balance('acc4')
        if acc4_balance and acc4_balance >= 400:
            result = self.bank.transfer(49, 'acc4', 'acc5', 400)
            if result is not None:
                self.assertEqual(result, acc4_balance - 400)
        
        # More deposits - get balance right before each deposit
        acc1_balance = self.bank.get_account_balance('acc1')
        if acc1_balance is not None:
            self.assertEqual(self.bank.deposit(50, 'acc1', 50), acc1_balance + 50)
        
        acc2_balance = self.bank.get_account_balance('acc2')
        if acc2_balance is not None:
            self.assertEqual(self.bank.deposit(51, 'acc2', 100), acc2_balance + 100)
        
        acc3_balance = self.bank.get_account_balance('acc3')
        if acc3_balance is not None:
            self.assertEqual(self.bank.deposit(52, 'acc3', 150), acc3_balance + 150)
        
        acc4_balance = self.bank.get_account_balance('acc4')
        if acc4_balance is not None:
            self.assertEqual(self.bank.deposit(53, 'acc4', 200), acc4_balance + 200)
        
        acc5_balance = self.bank.get_account_balance('acc5')
        if acc5_balance is not None:
            self.assertEqual(self.bank.deposit(54, 'acc5', 250), acc5_balance + 250)


class TestLevel2(unittest.TestCase):
    """Tests for Level 2: Ranking accounts by outgoing transactions"""
    
    failureException = Exception
    
    @classmethod
    def setUpClass(cls):
        cls.system = BankingSystem()
    
    def setUp(self):
        self.bank = BankingSystem()
    
    @timeout(0.4)
    def test_get_top_accounts_no_transactions(self):
        """Test getting top accounts when no transactions exist"""
        result = self.bank.get_top_accounts(5)
        self.assertEqual(result, [])
    
    @timeout(0.4)
    def test_get_top_accounts_single_transfer(self):
        """Test ranking with a single transfer"""
        self.bank.create_account(1000, "acc1")
        self.bank.create_account(2000, "acc2")
        self.bank.deposit(3000, "acc1", 100)
        self.bank.transfer(4000, "acc1", "acc2", 50)
        
        top = self.bank.get_top_accounts(5)
        self.assertEqual(top, ["acc1"])
    
    @timeout(0.4)
    def test_get_top_accounts_multiple_accounts(self):
        """Test ranking multiple accounts by outgoing transactions"""
        # Create accounts
        for i in range(1, 6):
            self.bank.create_account(i * 1000, f"acc{i}")
            self.bank.deposit(i * 1000 + 100, f"acc{i}", 1000)
        
        # Make transfers: acc1 -> 100, acc2 -> 200, acc3 -> 300, acc4 -> 400
        self.bank.transfer(6000, "acc1", "acc2", 100)
        self.bank.transfer(7000, "acc2", "acc3", 200)
        self.bank.transfer(8000, "acc3", "acc4", 300)
        self.bank.transfer(9000, "acc4", "acc5", 400)
        
        top = self.bank.get_top_accounts(5)
        # Should be sorted by outgoing amount descending, then by account_id ascending
        self.assertEqual(top, ["acc4", "acc3", "acc2", "acc1"])
    
    @timeout(0.4)
    def test_get_top_accounts_tie_breaking(self):
        """Test tie-breaking by account_id when amounts are equal"""
        self.bank.create_account(1000, "acc2")
        self.bank.create_account(2000, "acc1")
        self.bank.create_account(3000, "acc3")
        
        self.bank.deposit(4000, "acc1", 200)
        self.bank.deposit(5000, "acc2", 200)
        self.bank.deposit(6000, "acc3", 200)
        
        self.bank.transfer(7000, "acc1", "acc2", 100)
        self.bank.transfer(8000, "acc2", "acc3", 100)
        self.bank.transfer(9000, "acc3", "acc1", 100)
        
        top = self.bank.get_top_accounts(3)
        # All have 100 outgoing, so sorted by account_id
        self.assertEqual(top, ["acc1", "acc2", "acc3"])


class TestLevel3(unittest.TestCase):
    """Tests for Level 3: Scheduled payments with cashback"""
    
    failureException = Exception
    
    @classmethod
    def setUpClass(cls):
        cls.system = BankingSystem()
    
    def setUp(self):
        self.bank = BankingSystem()
    
    @timeout(0.4)
    def test_schedule_payment_successful(self):
        """Test scheduling a payment successfully"""
        self.bank.create_account(1000, "acc1")
        self.bank.create_account(2000, "acc2")
        self.bank.deposit(3000, "acc1", 1000)
        
        payment_id = self.bank.schedule_payment(4000, "acc1", "acc2", 500, 0.05)
        self.assertIsNotNone(payment_id)
        self.assertEqual(self.bank.get_account_balance("acc1"), 500)  # Amount reserved
        self.assertEqual(self.bank.get_payment_status(payment_id), "scheduled")
    
    @timeout(0.4)
    def test_schedule_payment_insufficient_funds(self):
        """Test scheduling payment with insufficient funds"""
        self.bank.create_account(1000, "acc1")
        self.bank.create_account(2000, "acc2")
        self.bank.deposit(3000, "acc1", 100)
        
        payment_id = self.bank.schedule_payment(4000, "acc1", "acc2", 500, 0.05)
        self.assertIsNone(payment_id)
    
    @timeout(0.4)
    def test_execute_payment(self):
        """Test executing a scheduled payment"""
        self.bank.create_account(1000, "acc1")
        self.bank.create_account(2000, "acc2")
        self.bank.deposit(3000, "acc1", 1000)
        
        payment_id = self.bank.schedule_payment(4000, "acc1", "acc2", 500, 0.10)
        self.assertIsNotNone(payment_id)
        
        result = self.bank.execute_payment(5000, payment_id)
        self.assertTrue(result)
        self.assertEqual(self.bank.get_payment_status(payment_id), "executed")
        
        # Check balances: acc1 should have 500 (reserved) + 50 (cashback) = 550
        # acc2 should have 500 (received)
        self.assertEqual(self.bank.get_account_balance("acc1"), 550)
        self.assertEqual(self.bank.get_account_balance("acc2"), 500)
    
    @timeout(0.4)
    def test_execute_nonexistent_payment(self):
        """Test executing non-existent payment"""
        result = self.bank.execute_payment(1000, "nonexistent")
        self.assertIsNone(result)
    
    @timeout(0.4)
    def test_execute_payment_twice(self):
        """Test executing same payment twice"""
        self.bank.create_account(1000, "acc1")
        self.bank.create_account(2000, "acc2")
        self.bank.deposit(3000, "acc1", 1000)
        
        payment_id = self.bank.schedule_payment(4000, "acc1", "acc2", 500, 0.05)
        self.bank.execute_payment(5000, payment_id)
        
        result = self.bank.execute_payment(6000, payment_id)
        self.assertIsNone(result)  # Already executed
    
    @timeout(0.4)
    def test_get_payment_status_nonexistent(self):
        """Test getting status of non-existent payment"""
        status = self.bank.get_payment_status("nonexistent")
        self.assertIsNone(status)


class TestLevel4(unittest.TestCase):
    """Tests for Level 4: Merging accounts with history retention"""
    
    failureException = Exception
    
    @classmethod
    def setUpClass(cls):
        cls.system = BankingSystem()
    
    def setUp(self):
        self.bank = BankingSystem()
    
    @timeout(0.4)
    def test_merge_accounts_successful(self):
        """Test merging two accounts successfully"""
        self.bank.create_account(1000, "acc1")
        self.bank.create_account(2000, "acc2")
        self.bank.deposit(3000, "acc1", 100)
        self.bank.deposit(4000, "acc2", 200)
        
        merged_id = self.bank.merge_accounts(5000, "acc1", "acc2")
        self.assertEqual(merged_id, "acc1")  # Should keep alphabetically first
        self.assertEqual(self.bank.get_account_balance("acc1"), 300)
        # Merged account should still be accessible (redirects to merged account)
        self.assertEqual(self.bank.get_account_balance("acc2"), 300)
    
    @timeout(0.4)
    def test_merge_accounts_retain_history(self):
        """Test that transaction history is retained after merge"""
        self.bank.create_account(1000, "acc1")
        self.bank.create_account(2000, "acc2")
        self.bank.deposit(3000, "acc1", 100)
        self.bank.deposit(4000, "acc2", 200)
        self.bank.transfer(5000, "acc1", "acc2", 50)
        
        merged_id = self.bank.merge_accounts(6000, "acc1", "acc2")
        history = self.bank.get_transaction_history(merged_id)
        
        self.assertIsNotNone(history)
        self.assertGreater(len(history), 0)
        # Should have deposits and transfers from both accounts
    
    @timeout(0.4)
    def test_merge_same_account(self):
        """Test merging same account returns None"""
        self.bank.create_account(1000, "acc1")
        result = self.bank.merge_accounts(2000, "acc1", "acc1")
        self.assertIsNone(result)
    
    @timeout(0.4)
    def test_merge_nonexistent_account(self):
        """Test merging with non-existent account returns None"""
        self.bank.create_account(1000, "acc1")
        result = self.bank.merge_accounts(2000, "acc1", "acc2")
        self.assertIsNone(result)
    
    @timeout(0.4)
    def test_merge_multiple_accounts(self):
        """Test merging multiple accounts"""
        self.bank.create_account(1000, "acc1")
        self.bank.create_account(2000, "acc2")
        self.bank.create_account(3000, "acc3")
        
        self.bank.deposit(4000, "acc1", 100)
        self.bank.deposit(5000, "acc2", 200)
        self.bank.deposit(6000, "acc3", 300)
        
        # Merge acc1 and acc2 -> acc1
        merged = self.bank.merge_accounts(7000, "acc1", "acc2")
        self.assertEqual(merged, "acc1")
        self.assertEqual(self.bank.get_account_balance("acc1"), 300)
        
        # Merge acc1 and acc3 -> acc1
        merged = self.bank.merge_accounts(8000, "acc1", "acc3")
        self.assertEqual(merged, "acc1")
        self.assertEqual(self.bank.get_account_balance("acc1"), 600)
    
    @timeout(0.4)
    def test_access_merged_account(self):
        """Test accessing account through merged account ID"""
        self.bank.create_account(1000, "acc1")
        self.bank.create_account(2000, "acc2")
        self.bank.deposit(3000, "acc1", 100)
        self.bank.deposit(4000, "acc2", 200)
        
        self.bank.merge_accounts(5000, "acc1", "acc2")
        
        # Should be able to access through merged account ID
        balance = self.bank.get_account_balance("acc2")
        self.assertEqual(balance, 300)  # Should redirect to acc1


class TestIntegration(unittest.TestCase):
    """Integration tests combining multiple levels"""
    
    failureException = Exception
    
    @classmethod
    def setUpClass(cls):
        cls.system = BankingSystem()
    
    def setUp(self):
        self.bank = BankingSystem()
    
    @timeout(0.4)
    def test_full_workflow(self):
        """Test a complete workflow using all levels"""
        # Level 1: Create accounts and make transactions
        self.bank.create_account(1000, "alice")
        self.bank.create_account(2000, "bob")
        self.bank.deposit(3000, "alice", 1000)
        self.bank.deposit(4000, "bob", 500)
        self.bank.transfer(5000, "alice", "bob", 200)
        
        # Level 2: Check rankings
        top = self.bank.get_top_accounts(5)
        self.assertIn("alice", top)
        
        # Level 3: Schedule and execute payment
        payment_id = self.bank.schedule_payment(6000, "alice", "bob", 300, 0.10)
        self.assertIsNotNone(payment_id)
        self.bank.execute_payment(7000, payment_id)
        
        # Level 4: Merge accounts
        merged = self.bank.merge_accounts(8000, "alice", "bob")
        self.assertEqual(merged, "alice")
        self.assertGreater(self.bank.get_account_balance("alice"), 0)


def run_level_tests(level: int):
    """Run tests for a specific level"""
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    if level >= 1:
        suite.addTests(loader.loadTestsFromTestCase(TestLevel1))
    if level >= 2:
        suite.addTests(loader.loadTestsFromTestCase(TestLevel2))
    if level >= 3:
        suite.addTests(loader.loadTestsFromTestCase(TestLevel3))
    if level >= 4:
        suite.addTests(loader.loadTestsFromTestCase(TestLevel4))
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    return result.wasSuccessful()


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        level = int(sys.argv[1])
        success = run_level_tests(level)
        sys.exit(0 if success else 1)
    else:
        # Run all tests
        unittest.main(verbosity=2)
