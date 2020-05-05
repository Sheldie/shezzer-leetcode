# -*- coding: UTF-8 -*-

__author__ = 'Shezzer'

from typing import List


# 53. 最大子序和
# easy
# 数组 分治算法 动态规划

class Solution:
    # Solution
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0 for _ in range(len(nums))]  # 以i为结尾的最大和
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            temp = nums[i] + dp[i - 1]
            dp[i] = temp if temp > nums[i] else nums[i]
        return max(dp)


if __name__ == '__main__':
    ls = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(Solution().maxSubArray(ls))
