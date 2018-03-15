import unittest
from challenge_3 import xor_decrypt, count_score
from challenge_1 import convert_to_raw_bytes

file = open("4.txt").read().split()


def search_file(file):

	for line in file:

		for key in range(0,256):
			decrypted_line = xor_decrypt(convert_to_raw_bytes(line), key) # decrypt line
			score = count_score(decrypted_line) # checking likelihood of decrypted line
			if score > 80:
				print("Ciphertext :", line, "\n", decrypted_line, "\nLikelihood: ", int
					(score), "%\nKey:", key, "\n")
			key += 1


search_file(file)


class TestingSearch(unittest.TestCase):

	def test_search(self):
		self.assertEqual(xor_decrypt
			(convert_to_raw_bytes
				('7b5a4215415d544115415d5015455447414c155c46155f4058455c5b523f'), 53),
				"Now that the party is jumping\n")


if __name__ == '__main__':
    unittest.main()
