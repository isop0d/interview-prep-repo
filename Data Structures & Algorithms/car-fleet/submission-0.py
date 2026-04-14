'''
    output = 0

    zip funciton to combine the two arrays for sorting.
'''

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        pairs = [[p, s] for p, s in zip(position, speed)]

        stack = []

        for p, s in sorted(pairs)[::-1]:
            time = (target - p) / s  

            if not stack:
                stack.append(time)
            
            elif time <= stack[-1]:
                continue

            else: stack.append(time)
        
        return len(stack)