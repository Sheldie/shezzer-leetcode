# -*- coding: UTF-8 -*-

__author__ = 'Shezzer'


# 1387. 将整数按权重排序
# medium
# 排序 图

# 对数字按特殊规则进行排序
# 字典排序

class Solution:
    # Solution 1
    def cal(self, x):
        cnt = 0
        while x != 1:
            if x % 2 == 0:
                x = x / 2
            else:
                x = 3 * x + 1
            cnt += 1
        return cnt

    def getKth(self, lo: int, hi: int, k: int) -> int:
        res = dict()
        for i in range(lo, hi + 1):
            res[i] = Solution().cal(i)
        ls = sorted(res.items(), key=lambda kv: (kv[1], kv[0]))
        return ls[k - 1][0]

    # Solution 2*
    # 递归
    def getKth2(self, lo: int, hi: int, k: int) -> int:
        ls = list(range(lo, hi + 1))

        def power(x):
            cnt = 0
            while x != 1:
                if x % 2 == 0:
                    x = x / 2
                else:
                    x = 3 * x + 1
                cnt += 1
            return cnt

        ls.sort(key=lambda i: power(i))
        return ls[k - 1]

    # 记区间长度为n，等于hi - lo + 1。
    # 时间复杂度：这里的区间一定是[1, 1000]的子集，在[1, 1000]中权重最大数的权重为178，即这个递归函数要执行178次，
    # 所以排序的每次比较的时间代价为O(178)，故渐进时间复杂度为O(178×nlogn)。
    # 空间复杂度：我们使用了长度为n的数组辅助进行排序，同时再使用递归计算权重时最多会使用178层的栈空间
    # 故渐进空间复杂度为O(n + 178)。

    # Solution 3*
    # 记忆化
    # 在[1, 1000]中所有x求f(x)的值的过程中，只可能出现2228种x，于是效率就会大大提高。
    def getKth3(self, lo: int, hi: int, k: int) -> int:
        f = {1: 0}

        def getF(x):
            if x in f:
                return f[x]
            f[x] = (getF(x * 3 + 1) if x % 2 == 1 else getF(x // 2)) + 1
            return f[x]

        v = list(range(lo, hi + 1))
        v.sort(key=lambda x: (getF(x), x))
        return v[k - 1]

    # 时间复杂度：平均情况下比较的次数为nlogn，把2228次平摊到每一次的时间代价为O(2228/nlogn)
    # 故总时间代价为O(2228/nlogn×nlogn)= O(2228)。


if __name__ == '__main__':
    lo = 10
    hi = 20
    k = 5
    print(Solution().getKth3(lo, hi, k))

    lo = 7
    hi = 11
    k = 4
    print(Solution().getKth3(lo, hi, k))

    lo = 1
    hi = 1000
    k = 777
    print(Solution().getKth3(lo, hi, k))
