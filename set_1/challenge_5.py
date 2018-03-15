import unittest
from itertools import cycle
from challenge_1 import convert_to_hex

stanza = b"Burning 'em, if you ain't quick and nimble\n\
I go crazy when I hear a cymbal"

key = b"ICE"


def ice_encrypt(plaintext, key):
	ciphertext = b''

	for plaintext_byte, key_byte in zip(plaintext, cycle(key)):
		xored_byte = plaintext_byte ^ key_byte
		ciphertext += xored_byte.to_bytes(1, 'little')
	return convert_to_hex(ciphertext)

print(ice_encrypt(stanza,key))


class TestingEncryption(unittest.TestCase):

	def test_ice_encrypt(self):
		self.assertEqual(ice_encrypt(stanza, key), b"0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272\
a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f")


if __name__ == '__main__':
	unittest.main()