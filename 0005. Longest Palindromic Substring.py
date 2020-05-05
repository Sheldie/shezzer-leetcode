# -*- coding: UTF-8 -*-

__author__ = 'Shezzer'


# 5. 最长回文子串
# medium
# 字符串 动态规划
# https://leetcode-cn.com/problems/longest-palindromic-substring/solution/zhong-xin-kuo-san-dong-tai-gui-hua-by-liweiwei1419/

class Solution:
    # Solution 1
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        if size < 2:
            return s

        dp = [[False for _ in range(size)] for _ in range(size)]

        for i in range(size):
            dp[i][i] = True

        max_len = 1
        start = 0
        for j in range(1, size):
            for i in range(0, j):
                if s[i] == s[j]:
                    # j - 1 - (i + 1) + 1 < 2
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = False

                if dp[i][j]:
                    cur_len = j - i + 1
                    if cur_len > max_len:
                        max_len = cur_len
                        start = i
        return s[start: start + max_len]

    # 时间复杂度：O(N^2)。
    # 空间复杂度：O(N^2)，二维dp问题，一个状态得用二维有序数对表示，因此空间复杂度是O(N^2)。

    # Solution 2*
    # 中心扩散
    def longestPalindrome2(self, s: str) -> str:
        def __center_spread(s, size, left, right):
            """
            left = right 的时候，此时回文中心是一个字符，回文串的长度是奇数
            right = left + 1 的时候，此时回文中心是一个空隙，回文串的长度是偶数
            """
            i = left
            j = right

            while i >= 0 and j < size and s[i] == s[j]:
                i -= 1
                j += 1
            return s[i + 1:j], j - i - 1

        size = len(s)
        if size < 2:
            return s

        # 至少是 1
        max_len = 1
        res = s[0]

        for i in range(size):
            palindrome_odd, odd_len = __center_spread(s, size, i, i)
            palindrome_even, even_len = __center_spread(s, size, i, i + 1)

            # 当前找到的最长回文子串
            cur_max_sub = palindrome_odd if odd_len >= even_len else palindrome_even
            if len(cur_max_sub) > max_len:
                max_len = len(cur_max_sub)
                res = cur_max_sub

        return res

    # 时间复杂度：枚举“中心位置”时间复杂度为 O(N)，从“中心位置”扩散得到“回文子串”的时间复杂度为 O(N)，因此时间复杂度可以降到 O(N^2)。
    # 空间复杂度：O(1)，只使用到常数个临时变量，与字符串长度无关。

    # Solution 3*
    # Manacher 算法
    def longestPalindrome3(self, s: str) -> str:
        # 特判
        size = len(s)
        if size < 2:
            return s

        # 得到预处理字符串
        t = "#"
        for i in range(size):
            t += s[i]
            t += "#"
        # 新字符串的长度
        t_len = 2 * size + 1

        # 数组 p 记录了扫描过的回文子串的信息
        p = [0 for _ in range(t_len)]

        # 双指针，它们是一一对应的，须同时更新
        max_right = 0
        center = 0

        # 当前遍历的中心最大扩散步数，其值等于原始字符串的最长回文子串的长度
        max_len = 1
        # 原始字符串的最长回文子串的起始位置，与 max_len 必须同时更新
        start = 1

        for i in range(t_len):
            if i < max_right:
                mirror = 2 * center - i
                # 这一行代码是 Manacher 算法的关键所在，要结合图形来理解
                p[i] = min(max_right - i, p[mirror])

            # 下一次尝试扩散的左右起点，能扩散的步数直接加到 p[i] 中
            left = i - (1 + p[i])
            right = i + (1 + p[i])

            # left >= 0 and right < t_len 保证不越界
            # t[left] == t[right] 表示可以扩散 1 次
            while left >= 0 and right < t_len and t[left] == t[right]:
                p[i] += 1
                left -= 1
                right += 1

            # 根据 max_right 的定义，它是遍历过的 i 的 i + p[i] 的最大者
            # 如果 max_right 的值越大，进入上面 i < max_right 的判断的可能性就越大，这样就可以重复利用之前判断过的回文信息了
            if i + p[i] > max_right:
                # max_right 和 center 需要同时更新
                max_right = i + p[i]
                center = i

            if p[i] > max_len:
                # 记录最长回文子串的长度和相应它在原始字符串中的起点
                max_len = p[i]
                start = (i - max_len) // 2
        return s[start: start + max_len]

    # 时间复杂度：O(N)，由于Manacher算法只有在遇到还未匹配的位置时才进行匹配，已经匹配过的位置不再匹配。
    # 因此对于字符串S的每一个位置，都只进行一次匹配，算法的复杂度为O(N)。
    # 空间复杂度：O(N)。


if __name__ == '__main__':
    s = "dddddddd"
    print(Solution().longestPalindrome3(s))
