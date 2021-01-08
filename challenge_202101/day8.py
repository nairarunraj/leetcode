from typing import List

import pytest


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        word1_len = len(word1)
        word2_len = len(word2)
        word_len = max(word1_len, word2_len)
        arr_str1 = ""
        arr_str2 = ""
        for i in range(word_len):
            if len(arr_str1) == len(arr_str2):
                if arr_str1 == arr_str2:
                    arr_str1 = ""
                    arr_str2 = ""
                else:
                    return False

            if i < word1_len:
                arr_str1 = arr_str1 + word1[i]

            if i < word2_len:
                arr_str2 = arr_str2 + word2[i]

        if len(arr_str1) == len(arr_str2) and arr_str1 == arr_str2:
            return True

        return False


@pytest.fixture()
def solution():
    return Solution()


def test_solution1(solution):
    word1 = ["ab", "c"]
    word2 = ["a", "bc"]
    assert solution.arrayStringsAreEqual(word1, word2)


def test_solution2(solution):
    word1 = ["a", "cb"]
    word2 = ["ab", "c"]
    assert not solution.arrayStringsAreEqual(word1, word2)


def test_solution3(solution):
    word1 = ["a", "b", "cb", "aac", "c"]
    word2 = ["ab", "cba", "acc"]
    assert solution.arrayStringsAreEqual(word1, word2)
