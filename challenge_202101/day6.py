from typing import List

import pytest


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        present = {i for i in arr}
        missing_no = -1
        count = 0

        for i in range(1, arr[-1] + 1):
            missing_no = i
            if i not in present:
                count += 1

            if count == k:
                return missing_no

        missing_no += (k - count)

        return missing_no


@pytest.fixture
def solution():
    return Solution()


def test_solution1(solution):
    arr = [2, 3, 4, 7, 11]
    k = 5
    # assert 9 == solution.findKthPositive(arr, k)


def test_solution2(solution):
    arr = [1, 2, 3, 4]
    k = 2
    print("+++" * 10)
    assert 6 == solution.findKthPositive(arr, k)
