import sys
import os
sys.path.insert(0, os.path.abspath(".."))
import unittest
from trie import Trie

class TestMediumSet(unittest.TestCase):
    trie = Trie()
    with open("25000_words.txt") as f_hdl:
        words = [entry.replace("\n", "") for entry in f_hdl.readlines()]
    trie.add_words(words)

    def test_prefix(self):
        expected_result = {'matches': ['zygote'], 'next_chars': ['o']}
        self.assertEqual(self.trie.from_prefix("zyg"), expected_result)

    def test_wrong_prefix(self):
        expected_result = {'matches': [], 'next_chars': []}
        self.assertEqual(self.trie.from_prefix("zzzz"), expected_result)

    def test_nonstr_prefix(self):
        self.assertRaises(TypeError, self.trie.from_prefix, ["zyg", "z"])

    def test_none_prefix(self):
        self.assertRaises(ValueError, self.trie.from_prefix, None)

    def test_word_exists(self):
        self.assertTrue(self.trie.word_exists("ZYGOTE"))

    def test_word_exists_force_case(self):
        self.assertFalse(self.trie.word_exists("ZYGOTE", ignore_case=False))

    def test_nonstr_word_exists(self):
        self.assertRaises(TypeError, self.trie.word_exists, ["zyg", "z"])

    def test_none_word_exists(self):
        self.assertRaises(ValueError, self.trie.word_exists, None)

if __name__ == '__name__':
    unittest.main()
