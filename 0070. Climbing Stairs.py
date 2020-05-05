# -*- coding: UTF-8 -*-

__author__ = 'Shezzer'


# 70. 爬楼梯
# easy
# 动态规划

class Solution:
    # Solution
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        dp = [0 for _ in range(n)]
        dp[0] = 1
        dp[1] = 2
        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n - 1]


if __name__ == '__main__':
    print(Solution().climbStairs(0))
