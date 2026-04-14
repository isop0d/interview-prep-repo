class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while len(stack) and stack[-1][1] < temp:
                j, jtemp = stack.pop()
                output[j] = i-j
            stack.append((i, temp))
        
        return output