from typing import List

import pytest


class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        idx = 0
        arr_len = len(arr)
        while idx < arr_len:
            val = arr[idx]
            found_piece = []
            for piece_arr in pieces:
                if val == piece_arr[0]:
                    found_piece = piece_arr
                    break

            if len(found_piece) == 0:
                return False

            for piece_val in found_piece:
                if val != piece_val:
                    return False

                idx += 1
                if idx == arr_len: return True

                val = arr[idx]

        return True


@pytest.fixture()
def solution():
    return Solution()


def test_solution1(solution):
    arr = [49, 18, 16]
    pieces = [[16, 18, 49]]
    assert not solution.canFormArray(arr, pieces)


def test_solution2(solution):
    arr = [1, 2, 3]
    pieces = [[2], [1, 3]]

    assert not solution.canFormArray(arr, pieces)


def test_solution3(solution):
    arr = [15, 88]
    pieces = [[88], [15]]
    assert solution.canFormArray(arr, pieces)


def test_solution4(solution):
    arr = [85]
    pieces = [[85]]
    assert solution.canFormArray(arr, pieces)


def test_solution5(solution):
    arr = [91, 4, 64, 78]
    pieces = [[78], [4, 64], [91]]
    assert solution.canFormArray(arr, pieces)


def test_solution6(solution):
    arr = [1, 3, 5, 7]
    pieces = [[2, 4, 6, 8]]
    assert not solution.canFormArray(arr, pieces)
