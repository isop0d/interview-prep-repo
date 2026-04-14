'''

30 38 31 30 33 36 35 39

while val > stack[-1]:
    

'''
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0] * len(temperatures)
        stack = []

        for  i, val in enumerate(temperatures):
            if not stack:
                stack.append([i, val])
            else:
                while len(stack) and stack[-1][1] < val:
                    res[stack[-1][0]] = i - stack[-1][0]
                    stack.pop()
                stack.append([i, val])
        return res
