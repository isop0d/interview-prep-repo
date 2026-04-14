class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashMap = {}
        longestStr = 0
        l, r = 0, 0

        while r < len(s):
            if s[r] in hashMap and hashMap[s[r]] >= l:
                l = hashMap[s[r]] + 1

            hashMap[s[r]] = r
            currStr = r - l + 1
            longestStr = max(currStr, longestStr)

            r += 1

        return longestStr
