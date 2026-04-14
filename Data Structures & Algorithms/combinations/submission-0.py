class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(path, start):
            #base case:
            if len(path) == k:
                res.append(path[:])
                return 
            #choices
            for i in range(start, n + 1):
                path.append(i)
                backtrack(path, i + 1)

                path.pop()
        backtrack([], 1)
        return res