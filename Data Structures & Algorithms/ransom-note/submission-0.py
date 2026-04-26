class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazineTable = defaultdict(int)

        for char in magazine:
            magazineTable[char] += 1

        for char in ransomNote:
            if char not in magazineTable:
                return False
            elif char in magazineTable:
                if magazineTable[char] <= 0:
                    return False
                magazineTable[char] -= 1 

        return True
