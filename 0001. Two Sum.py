# -*- coding: UTF-8 -*-

__author__ = 'Shezzer'

from typing import List


# 1. 两数之和
# 数组 哈希表

class Solution:
    # Solution 1
    # BF
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    # Solution 2
    # 哈希表
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()
        for idx, num in enumerate(nums):
            hashmap[num] = idx
        for i, num in enumerate(nums):
            j = hashmap.get(target - num)
            if j and i != j:
                return [i, j]


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    print(Solution().twoSum2(nums, target))
