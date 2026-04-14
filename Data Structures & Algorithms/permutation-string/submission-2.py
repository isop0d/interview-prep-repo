
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        matchMap = defaultdict(int)
        s1Map = defaultdict(int)

        for c in s1:
            s1Map[c] += 1

        l, r = 0, 0 
        charsMatching = 0

        while r < len(s2):
            windowLen = r - l + 1

            if s2[r] in s1Map:
                matchMap[s2[r]] += 1 

                if matchMap[s2[r]] <= s1Map[s2[r]]:
                    charsMatching += 1

            if windowLen > len(s1):
                if s2[l] in s1Map:
                    if matchMap[s2[l]] <= s1Map[s2[l]]:
                        charsMatching -= 1 
                    matchMap[s2[l]] -= 1
                l += 1 
            if charsMatching == len(s1):
                return True
            r += 1
        return False