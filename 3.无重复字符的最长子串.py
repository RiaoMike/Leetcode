#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        right = -1
        chars = set()
        max = 0
        for i in range(len(s)):
            if i != 0:
                chars.discard(s[i - 1])
            while right + 1 < len(s) and s[right + 1] not in chars:
                right += 1
                chars.add(s[right])
            if(len(chars) > max):
                max = len(chars)
        return max
# @lc code=end

