import unittest
from solution import *


class AnagramSolutionTest(unittest.TestCase):
    def test_two_strings_are_not_anagram_case_1(self):
        result = anagram_example_result("Tom Marvolo Riddle", "I Am Lord Voldemort")
        self.assertEquals(result,
                          "remove 7 characters from 'Tom Marvolo Riddle' and 8 characters from 'I Am Lord Voldemort'")

    def test_two_strings_are_anagram(self):
        result = anagram_example_result("tom marvolo riddle", "i am lordvoldemort")
        self.assertEquals(result, "they are anagrams")


if __name__ == '__main__':
    unittest.main()
