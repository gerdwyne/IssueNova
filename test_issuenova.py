# test_issuenova.py
"""
Tests for IssueNova module.
"""

import unittest
from issuenova import IssueNova

class TestIssueNova(unittest.TestCase):
    """Test cases for IssueNova class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = IssueNova()
        self.assertIsInstance(instance, IssueNova)
        
    def test_run_method(self):
        """Test the run method."""
        instance = IssueNova()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
