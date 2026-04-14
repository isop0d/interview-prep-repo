class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        numMap = {}

        for i,n in enumerate(nums):

            numMap[n] = i

        for i,n in enumerate(nums):

            numNeeded = target - n

            if numNeeded in numMap and numMap[numNeeded] != i:

                return [i, numMap[numNeeded]] 
        
        return []

            
