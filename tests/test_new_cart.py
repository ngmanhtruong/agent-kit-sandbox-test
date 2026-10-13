import unittest
from shop.cart import new_cart


class TestNewCart(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(new_cart(), {})
