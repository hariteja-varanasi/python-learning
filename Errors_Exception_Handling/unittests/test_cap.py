import unittest2 as unittest
import cap
from typing_extensions import MutableMapping

class TestCap(unittest.TestCase):

    def test_one_word(self):
        text="python"
        result=cap.cap_text(text)
        self.assertEqual(result,"Python")

    def test_multiple_words(self):
        text="monty python"
        result=cap.cap_text(text)
        print(f"result is {result}")
        self.assertEqual(result, "Monty Python")

if __name__=="main":
    unittest.main()
