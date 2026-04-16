class Solution:
    def tribonacci(self, n: int) -> int:
        seen = defaultdict(int)
        def find_nth_tribonacci(n: int) -> int:
            if n == 0:
                return 0
            elif n == 1 or n == 2:
                return 1
            if n in seen:
                return seen[n]

            else:
                seen[n] = (find_nth_tribonacci(n - 1) + find_nth_tribonacci(n - 2) + find_nth_tribonacci(n - 3) )
                return seen[n]
        return find_nth_tribonacci(n)
    