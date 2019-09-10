#!/usr/bin/env python3

# Problem Description - https://leetcode.com/problems/two-sum/

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_hash = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement not in nums_hash:
                nums_hash[num] = i
            else:
                return [nums_hash[complement], i]

if __name__ == "__main__":
    two_sum = Solution()
    print(two_sum.twoSum([3,2,4], 6))
