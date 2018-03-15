import unittest
from challenge_1 import convert_to_raw_bytes, convert_to_hex

hex_string = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
ciphertext = convert_to_raw_bytes(hex_string)


def xor_decrypt(ciphertext, key):
	"""Decrypts a ciphertext using a given key"""

	decrypted_char = ''
	decrypted_str = ''

	for char in ciphertext:
		decrypted_char = chr(char ^ key)
		decrypted_str += decrypted_char

	return decrypted_str


def count_score(decrypted_str):
	"""Calculates likelihood of a char being the key by counting
	instances of English letters and other common symbols from
	the decrypted text. """

	english_chars = 'ABCDEFGHIJKLMNOPQRSTUVWVYZ abcdefghijklmnopqrstuvwxyz?.,'

	score = float(0.0)
	points = float(0.0)

	for i in range(len(decrypted_str)):
		if decrypted_str[i] in english_chars:
			points += 1
		score = points / len(decrypted_str)
		score = score * 100

	return score


def test_possible_keys(ciphertext):
	""" Tests all possible keys and returns keys with highest 
	likelihood of bring the encryption key."""

	top_keys = []

	for num in range(0, 255, 1):
		decrypted_str = xor_decrypt(ciphertext, num)
		score = count_score(decrypted_str)
		if score > 80:
			top_keys.append(chr(num))

	return top_keys


test_possible_keys(ciphertext)


class TestSingleByteXor(unittest.TestCase):

	def test_xor_decrypt(self):
		self.assertEqual(xor_decrypt(ciphertext, ord('X')), "Cooking MC's like a pound\
			of bacon")

	def test_xor_decrypt(self):
		self.assertIsNot(xor_decrypt(ciphertext, ord('T')), "Cooking MC's like a\
			pound of bacon")


if __name__ == '__main__':
    unittest.main()
