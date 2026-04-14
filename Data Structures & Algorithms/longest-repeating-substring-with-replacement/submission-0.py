class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        highestChar = 0
        longestSub = 0 
        hashMap = defaultdict(int)

        while r < len(s):
            hashMap[s[r]] += 1

            if hashMap[s[r]] > highestChar:
                highestChar = hashMap[s[r]]
            
            if (r - l + 1) - highestChar > k:
                hashMap[s[l]] -= 1 
                l += 1 

            currSub = r - l + 1
            longestSub = max(longestSub, currSub)
            r += 1
        return longestSub