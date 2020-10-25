import unittest
from solution import *


class AnagramSolutionTest(unittest.TestCase):
    def test_two_strings_are_not_anagram_case_1(self):
        result = anagram_example_result("Tom Marvolo Riddle", "I Am Lord Voldemort")
        self.assertEquals(result,
                          "remove 7 characters from 'Tom Marvolo Riddle' and 8 characters from 'I Am Lord Voldemort'")

    def test_two_strings_are_not_anagram_case_1(self):
        result = anagram_example_result("tom marvolo riddle", "i am lord voldemort")
        self.assertEquals(result,
                          "remove 0 characters from 'tom marvolo riddle' and 1 characters from 'i am lord voldemort'")

    def test_two_strings_are_not_anagram_case_1(self):
        result = anagram_example_result("tom riddle", "voldemort")
        self.assertEquals(result,
                          "remove 3 characters from 'tom riddle' and 2 characters from 'voldemort'")

    def test_two_strings_are_anagram(self):
        result = anagram_example_result("tom marvolo riddle", "i am lordvoldemort")
        self.assertEquals(result, "they are anagrams")


if __name__ == '__main__':
    unittest.main()
