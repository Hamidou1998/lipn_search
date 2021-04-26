import sys
sys.path.append('../src')
from hamming import hamming
import unittest

class TestHamming(unittest.TestCase):
	def test_hamming(self):
			result=hamming("mais","mats")
			self.assertEqual(result,1)

