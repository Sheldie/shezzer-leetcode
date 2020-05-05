# -*- coding: UTF-8 -*-

__author__ = 'Shezzer'


# 424. 替换后的最长重复字符
# medium
# 双指针 滑动窗口

class Solution:
    # Solution*
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        res = 0
        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            max_letter = max(count, key=count.get)
            while right - left + 1 - count[max_letter] > k:
                count[s[left]] -= 1
                left += 1
                max_letter = max(count, key=count.get)
            res = max(res, right - left + 1)
        return res


if __name__ == '__main__':
    print(Solution().characterReplacement('AABABBA', 1))
