class Solution:
    def climbStairs(self, n: int) -> int:
        map = defaultdict(int)

        def climb(curr):
            if curr in map:
                return map[curr]
            elif curr == n:
                return 1
            elif curr > n:
                return 0
            else:
                choiceA = climb(curr + 1)
                choiceB = climb(curr + 2)
                map[curr] = (choiceA + choiceB)
                return map[curr]
        return climb(0)

