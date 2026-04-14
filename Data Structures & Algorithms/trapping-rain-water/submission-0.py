class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        prefix = height[l]
        suffix = height[r]
        water_total = 0

        while l < r:
            if prefix < suffix:
                l += 1
                if height[l] < prefix:
                    water_total += prefix - height[l]
                else:
                    prefix = height[l]
            else:
                r -= 1
                if height[r] < suffix:
                    water_total += suffix - height[r]
                else:
                    suffix = height[r]

        return water_total