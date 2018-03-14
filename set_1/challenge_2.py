import unittest, base64
from challenge_1 import convert_to_raw_bytes, convert_to_base64, convert_to_hex

buffer1 = '1c0111001f010100061a024b53535009181c'
buffer2 = '686974207468652062756c6c277320657965'


def are_equal_len(buffer1, buffer2):
	"""Checks if two buffers are equal length."""

	if len(buffer1) != len(buffer2):
		return False
	else:
		return True


def fixed_xor(buffer1, buffer2):
	xor = ''
	output = ''

	for pair in zip(buffer1, buffer2):
		xor = ord(pair[0]) ^ ord(pair[1])
		output += chr(xor)

	return output


def do_fixed_xor(buffer1, buffer2):
	"""Runs the functions to check length, base64 decode, then xor two equal length
	buffers"""
	if not are_equal_len(buffer1, buffer2):
		return("Error. Not equal length buffers!")
	else:
		buffer1_2 = convert_to_raw_bytes(buffer1)
		buffer2_2 = convert_to_raw_bytes(buffer2)

		xor = fixed_xor(buffer1_2, buffer2_2)

		return xor


do_fixed_xor(buffer1, buffer2)


class TestXorFunctions(unittest.TestCase):

	def test_are_equal_len(self):
		self.assertTrue(are_equal_len('1c0111001f010100061a024b53535009181c','686974207468652062756c6c277320657965'), True)

	def test_do_fixed_xor(self):
		self.assertEqual(do_fixed_xor(buffer1,buffer2),b"the kid don't play")

	def test_do_fixed_xor_hex_encode(self):
		self.assertEqual(convert_to_hex(do_fixed_xor(buffer1, buffer2)),
			'746865206b696420646f6e277420706c6179')


if __name__ == '__main__':
    unittest.main()
