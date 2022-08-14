# TC: O(nlogn) where O(nlogn) is used for sorting initially, and then O(log n) time for searching
# for the sum pairs "n" times which again constitutes O(nlogn)  
# SC: O(1) No auxillary data structure

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums = sorted(nums)
        result = []
        
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            p1 = i+1
            p2 = len(nums) - 1

            while p1 < p2:

                if nums[i] + nums[p1] + nums[p2] > 0:
                    p2 -= 1

                elif nums[i] + nums[p1] + nums[p2] < 0:
                    p1 += 1

                else:
                    result.append(sorted([nums[i], nums[p1], nums[p2]]))

                    p1 += 1
                    
                    while p1 < p2 and nums[p1] == nums[p1-1]:
                        p1 += 1
                    
        return result