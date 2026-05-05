class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        max = nums[0]
        maxi = 0
        nums_list = defaultdict(int)
        for num in nums:
            nums_list[num] += 1
            if nums_list[num] > maxi:
                maxi = nums_list[num]
                max = num
        return max