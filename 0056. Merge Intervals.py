# -*- coding: UTF-8 -*-

__author__ = 'Shezzer'

from typing import List


# 56. 合并区间
# 排序 数组

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(interval[1], merged[-1][1])
        return merged


if __name__ == '__main__':
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(Solution().merge(intervals))

    intervals = [[1, 4], [4, 5]]
    print(Solution().merge(intervals))
