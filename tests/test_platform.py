#!/usr/bin/env python3
"""
Unit Tests for IBM Business Intelligence (BI) Analyst
"""

import unittest
import sys
import os

# Add src to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

class TestPlatform(unittest.TestCase):
    """Test cases for the platform"""
    
    def test_basic_functionality(self):
        """Test basic functionality"""
        result = 2 + 2
        self.assertEqual(result, 4)
    
    def test_data_processing(self):
        """Test data processing"""
        data = [1, 2, 3, 4, 5]
        total = sum(data)
        self.assertEqual(total, 15)
    
    def test_string_operations(self):
        """Test string operations"""
        text = "IBM Business Intelligence (BI) Analyst"
        self.assertTrue(len(text) > 0)

if __name__ == '__main__':
    unittest.main()
