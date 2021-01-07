import copy

import pytest


class Solution:
    def countArrangement(self, n: int) -> int:
        # The number at the ith position is divisible by i.
        # i is divisible by the number at the ith position.

        # 1 -> [1..n],[1]
        # 2 -> [2,4,6,...n],[1,2]
        # 3 -> [3,6,9,...],[1,3]
        # 4 -> [4,8,12,...],[1,2,4]

        arr_range = list(range(1, n + 1))

        factors_dict = {}
        multiples_dict = {}

        def get_factors(idx, arr):
            if idx in factors_dict:
                return factors_dict[idx]

            factors = set()
            for i in arr:
                if idx % i == 0:
                    factors.add(i)

            factors_dict[idx] = factors

            return factors

        def get_multiples(idx, arr):
            if idx in multiples_dict:
                return multiples_dict[idx]

            multiples = set()
            for i in arr:
                if i % idx == 0:
                    multiples.add(i)

            multiples_dict[idx] = multiples

            return multiples

        def count_arrangements(arr_len, valid_entries_at_current_idx, idx, perm):
            if idx == arr_len + 1:
                return 1

            count = 0
            for poss in valid_entries_at_current_idx[idx]:
                if poss in perm:
                    continue

                current_perm = copy.copy(perm)
                current_perm.add(poss)
                count += count_arrangements(arr_len, valid_entries_at_current_idx, idx + 1, current_perm)

            return count

        def get_distinct_arrangements(arr_len, arr):
            valid_entries_at_current_idx = {}
            for idx in arr:
                factors = get_factors(idx, arr)
                multiples = get_multiples(idx, arr)

                valid_entries_at_current_idx[idx] = set(factors.union(multiples))

            return count_arrangements(arr_len, valid_entries_at_current_idx, 1, set())

        return get_distinct_arrangements(n, arr_range)


@pytest.fixture
def solution():
    return Solution()


def test_solution1(solution):
    n = 1
    assert 1 == solution.countArrangement(n)


def test_solution2(solution):
    n = 2
    assert 2 == solution.countArrangement(n)


def test_solution3(solution):
    n = 3
    assert 3 == solution.countArrangement(n)


def test_solution4(solution):
    n = 4
    assert 8 == solution.countArrangement(n)


def test_solution12(solution):
    n = 12
    assert 4010 == solution.countArrangement(n)


def test_solution15(solution):
    n = 15
    assert 24679 == solution.countArrangement(n)
