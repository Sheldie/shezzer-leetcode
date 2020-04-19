# -*- coding: UTF-8 -*-

__author__ = 'Shezzer'

import bisect
from typing import List


# 1385. 两个数组间的距离值
# 数组


class Solution:
    # Solution 1
    # BF
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        sum = 0
        for a in arr1:
            flag = True
            for b in arr2:
                if abs(a - b) <= d:
                    flag = False
                    break
            if flag:
                sum += 1
        return sum

    # 假设arr1中元素个数为n，arr2中元素个数为m。
    # 时间复杂度：从代码可以看出这里的渐进时间复杂度是O(n×m)。
    # 空间复杂度：这里没有使用任何的辅助空间，故渐进空间复杂度为O(1)。

    # Solution 2*
    # 二分查找
    # 实际上我们只要找到大于等于x的第一个y和小于x的第一个y，看看它们满不满足这个性质就可以了。
    def findTheDistanceValue2(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        cnt = 0
        for x in arr1:
            p = bisect.bisect_left(arr2, x)
            if p == len(arr2) or abs(x - arr2[p]) > d:
                if p == 0 or abs(x - arr2[p - 1]) > d:
                    cnt += 1
        return cnt


if __name__ == '__main__':
    arr1 = [4, 5, 8]
    arr2 = [10, 9, 1, 8]
    d = 2
    print(Solution().findTheDistanceValue(arr1, arr2, d))

    arr1 = [1, 4, 2, 3]
    arr2 = [-4, -3, 6, 10, 20, 30]
    d = 3
    print(Solution().findTheDistanceValue(arr1, arr2, d))

    arr1 = [2, 1, 100, 3]
    arr2 = [-5, -2, 10, -3, 7]
    d = 6
    print(Solution().findTheDistanceValue(arr1, arr2, d))

    arr1 = [4, 5, 8]
    arr2 = [10, 9, 1, 8]
    d = 2
    print(Solution().findTheDistanceValue2(arr1, arr2, d))

    arr1 = [1, 4, 2, 3]
    arr2 = [-4, -3, 6, 10, 20, 30]
    d = 3
    print(Solution().findTheDistanceValue2(arr1, arr2, d))

    arr1 = [2, 1, 100, 3]
    arr2 = [-5, -2, 10, -3, 7]
    d = 6
    print(Solution().findTheDistanceValue2(arr1, arr2, d))
