"""
Sandbox Tests - Playground for Custom Testing

This is a playground for you to modify, add, or delete custom tests.
The results of these tests are always at the beginning of the report.
These results do not affect the final score (unless the project fails to build).
"""

import inspect
import os
import sys

# Add parent directory to path for imports
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

try:
    from timeout_decorator import timeout
except ImportError:
    # Fallback decorator if timeout_decorator is not installed
    def timeout(seconds):
        def decorator(func):
            return func
        return decorator

import unittest
from banking_system import BankingSystem


class SandboxTests(unittest.TestCase):
    """Playground for custom tests - modify as needed"""
    
    failureException = Exception
    
    @classmethod
    def setUpClass(cls):
        """Set up test class with a banking system instance"""
        cls.system = BankingSystem()
    
    @timeout(0.4)
    def test_sample(self):
        """Sample test for quick debugging"""
        self.assertTrue(self.system.create_account(1, 'account1'))
        self.assertTrue(self.system.create_account(2, 'account2'))
        self.assertEqual(self.system.deposit(3, 'account1', 2000), 2000)
        self.assertEqual(self.system.deposit(4, 'account2', 1000), 1000)
        self.assertEqual(self.system.transfer(5, 'account1', 'account2', 500), 1500)
    
    # Add your custom tests below
    # Example:
    # @timeout(0.4)
    # def test_my_custom_test(self):
    #     """Your custom test description"""
    #     self.assertTrue(self.system.create_account(1, 'test_account'))
    #     # Add more assertions here


if __name__ == "__main__":
    unittest.main(verbosity=2)

