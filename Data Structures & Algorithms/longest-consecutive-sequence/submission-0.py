class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums: 
            return 0
        
        longestStreak = 0

        numset = set(nums)

        for num in nums:
            streak = 1
            currentNum = num

            while (currentNum + 1) in nums:
                streak += 1
                currentNum += 1

            longestStreak = max(longestStreak, streak)


        return longestStreak
