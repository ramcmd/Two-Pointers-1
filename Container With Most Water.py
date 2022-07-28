#TC: O(n)
#SC: O(1)

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        low = 0
        high = len(height) - 1
        max_ = 0
        while low < high:
            
            max_ = max(max_, min(height[low], height[high]) * (high - low))
            
            if height[low] < height[high]:
                low += 1
            else:
                high -= 1
                
        return max_
                