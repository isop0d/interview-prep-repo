class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c.lower() for c in s if c.isalnum())
        slen = len(s)
        middle = slen//2
        if slen % 2 == 0:
            left = s[:middle]
            right = s[middle:]        
        else: 
            left = s[:middle]
            right = s[middle + 1:]
        return left == right[::-1]
