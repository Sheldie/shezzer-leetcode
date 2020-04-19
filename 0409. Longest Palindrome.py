# -*- coding: UTF-8 -*-

__author__ = 'Shezzer'

from collections import Counter


# 409. 最长回文串
# 哈希表

class Solution:
    def longestPalindrome(self, s: str) -> int:
        ans = 0
        count = Counter(s)
        for v in count.values():
            ans += v // 2 * 2
            if ans % 2 == 0 and v % 2 == 1:
                ans += 1
        return ans


if __name__ == '__main__':
    s = "abccccdd"
    print(Solution().longestPalindrome(s))
