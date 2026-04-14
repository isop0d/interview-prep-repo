class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_Water  = 0

        while left < right:
            if heights[left] < heights[right] or heights[left] == heights[right]:
                curr_Water = heights[left] * (right - left)
            elif heights[left] > heights[right]:
                curr_Water = heights[right] * (right - left)

            if curr_Water > max_Water:
                max_Water = curr_Water

            if heights[left] > heights[right]:
                right -= 1

            elif heights[left] < heights[right]:
                left += 1
            
            else:
                left += 1

        return max_Water
