import unittest
from primes1 import is_prime

class PrimesTestCase(unittest.TestCase):
    """Tests for `primes.py`."""

    def test_is_five_prime(self):
        """Is five successfully determined to be prime?"""
        self.assertTrue(is_prime(5))

    def test_is_four_not_prime(self):
      """Is four determined to be not prime?"""
      self.assertFalse(is_prime(4), msg="Four is not prime!")

    def test_is_zero_not_prime(self):
      """Is zero determined to be not prime?"""
      self.assertFalse(is_prime(0), msg="Zero is not prime!")

    def test_negative_number(self):
      """Is a negative number determined to be not prime?"""
      self.assertFalse(is_prime(-5), msg="-5 is not prime!")

    def test_one_is_not_prime(self):
      """Is 1 determined to be not prime?"""
      self.assertFalse(is_prime(1), msg="1 is not prime!")

    def test_non_integers_are_not_prime(self):
      """Is any data type other than an integer determined to be not prime?"""
      self.assertFalse(is_prime('1'), msg="'1' is not an integer!")

if __name__ == '__main__':
    unittest.main()
