# Last updated: 11/11/2026, 6:33:59 pm
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def find_first():
            first = -1
            l, h = 0, len(nums) - 1
            while l <= h:
                m = (l + h) // 2
                if nums[m] == target:
                    first = m
                    h = m - 1  
                elif nums[m] > target:
                    h = m - 1
                else:
                    l = m + 1 
            return first

        def find_last():
            last = -1
            l, h = 0, len(nums) - 1
            while l <= h:
                m = (l + h) // 2
                if nums[m] == target:
                    last = m
                    l = m + 1  
                elif nums[m] > target:
                    h = m - 1
                else:
                    l = m + 1  
            return last
            
        return [find_first(), find_last()]