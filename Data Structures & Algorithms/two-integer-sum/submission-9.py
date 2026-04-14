class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            num_needed = target - nums[i]
        
            if num_needed in hashmap:
                return [hashmap[num_needed], i]
        
            hashmap[nums[i]] = i

        return []