# Last updated: 8/11/2026, 5:27:05 pm
class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        count = 0
        nums.sort()
        
        mid_idx = len(nums)//2
        mid = nums[mid_idx]
        nums1 = nums[:mid_idx]
        nums2 = nums[mid_idx+1:]
        for num in nums1:
            count += mid - num
        for num in nums2:
            count += num - mid
        
        return count
        