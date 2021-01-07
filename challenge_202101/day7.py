import pytest


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        last_occurrence = {}
        max_length = 0
        min_idx = 0
        for idx, ch in enumerate(s, 1):
            if ch in last_occurrence and last_occurrence[ch] > min_idx:
                min_idx = last_occurrence[ch]

            max_length = max(max_length, idx - min_idx)
            last_occurrence[ch] = idx

        return max_length


@pytest.fixture()
def solution():
    return Solution()


def test_solution1(solution):
    s = "abcabcbb"
    assert 3 == solution.lengthOfLongestSubstring(s)


def test_solution2(solution):
    s = "bbbbb"
    assert 1 == solution.lengthOfLongestSubstring(s)


def test_solution3(solution):
    s = "pwwkew"
    assert 3 == solution.lengthOfLongestSubstring(s)


def test_solution4(solution):
    s = "a"
    assert 1 == solution.lengthOfLongestSubstring(s)


def test_solution5(solution):
    s = ""
    assert 0 == solution.lengthOfLongestSubstring(s)


def test_solution6(solution):
    s = "au"
    assert 2 == solution.lengthOfLongestSubstring(s)


def test_solution7(solution):
    s = "aab"
    assert 2 == solution.lengthOfLongestSubstring(s)


def test_solution8(solution):
    s = "abba"
    assert 2 == solution.lengthOfLongestSubstring(s)


def test_solution9(solution):
    s = "tmmzuxt"
    assert 5 == solution.lengthOfLongestSubstring(s)


def test_solution10(solution):
    s = "abbcssderergffffsdfwerasvcxbbcsa"
    assert 11 == solution.lengthOfLongestSubstring(s)
