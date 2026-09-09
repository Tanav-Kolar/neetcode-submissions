class Solution:
    def trap(self, height: List[int]) -> int:
        l , r = 0 , len(height) - 1
        left_max, right_max = height[l], height[r]
        #initialise empty variable to store the amount of water
        water_trapped = 0

        while l < r:
            if left_max < right_max: 
                water_trapped += left_max - height[l]
                l += 1
                left_max = max(left_max,height[l])
            else:
                water_trapped += right_max - height[r]
                r -= 1
                right_max = max(right_max,height[r])
        
        return water_trapped
