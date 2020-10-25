import unittest
from solution import *


class AnagramSolutionTest(unittest.TestCase):

    def test_two_strings_are_anagram(self):
        result = anagram_example_result("tom marvolo riddle", "i am lordvoldemort")
        self.assertEquals(result, "they are anagrams")


if __name__ == '__main__':
    unittest.main()
