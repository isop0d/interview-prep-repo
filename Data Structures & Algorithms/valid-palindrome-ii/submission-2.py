class Solution:

    def validPalindrome(self, s:str) -> bool: 
        l, r = 0, len(s) - 1

        def check_char(left: int, right: int) -> bool:
            while left <= right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        while l <= r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return (check_char(l + 1, r) or check_char(l, r - 1))
        
        return True
