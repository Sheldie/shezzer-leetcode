# -*- coding: UTF-8 -*-

__author__ = 'Shezzer'

# 45. 跳跃游戏 II
# hard
# 贪心 数组
from typing import List


class Solution:
    # Solution 1
    # 反向查找
    # 递归地从左到右找到第一个能达到目标位置的格子

    # Solution 2*
    # 正向查找
    # 选择当前格子弹跳范围内弹跳距离最大的格子 / 遍历一遍数组并记录能达到的最远距离
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        maxPos, end, step = 0, 0, 0
        for i in range(n - 1):
            if maxPos >= i:
                maxPos = max(maxPos, i + nums[i])
                if i == end:
                    end = maxPos
                    step += 1
        return step


if __name__ == '__main__':
    ls = [2, 3, 1, 1, 4]
    print(Solution().jump(ls))
