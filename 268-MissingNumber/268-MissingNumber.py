# Last updated: 10/11/2026, 5:49:00 pm
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        return (len(nums)*(len(nums)+1)//2) - sum(nums)