import unittest
import base64
import binascii

string = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'


def convert_to_raw_bytes(string_input):
	"""Hex decodes a string."""
	return binascii.unhexlify(string_input)


def convert_to_hex(string_input):
	"""Hex encodes a string"""
	return binascii.hexlify(string_input)


def convert_to_base64(bytes_input):
	"""Base64 encodes some bytes."""
	return base64.b64encode(bytes_input)


class TestStringConversions(unittest.TestCase):

	def test_hex_decode(self):
		self.assertEqual
		(convert_to_raw_bytes(string), b"I'm killing your brain like a poisonous mushroom")

	def test_base64_encode(self):
		self.assertEqual
		(convert_to_base64(string),
			b"SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t")


if __name__ == '__main__':
    unittest.main()
