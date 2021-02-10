from alpha_blocks import can_make_word
import unittest

class TestAlphaBlocks(unittest.TestCase):

    def test_allowed_words(self):
        self.assertEqual(True, can_make_word("A"))
        self.assertEqual(True, can_make_word("BARK"))
        self.assertEqual(True, can_make_word("TREAT"))
        self.assertEqual(True, can_make_word("SQUAD"))
        self.assertEqual(True, can_make_word("CONFUSE"))
    
    def test_disallowed_words(self):
        self.assertEqual(False, can_make_word("BOOK"))
        self.assertEqual(False, can_make_word("COMMON"))    

if __name__ == '__main__':
    unittest.main()  # pragma: no cover
