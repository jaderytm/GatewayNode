# test_gatewaynode.py
"""
Tests for GatewayNode module.
"""

import unittest
from gatewaynode import GatewayNode

class TestGatewayNode(unittest.TestCase):
    """Test cases for GatewayNode class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = GatewayNode()
        self.assertIsInstance(instance, GatewayNode)
        
    def test_run_method(self):
        """Test the run method."""
        instance = GatewayNode()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
