# Last updated: 10/11/2026, 5:47:48 pm
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n=len(nums)
        return (n*(n+1)//2) - sum(nums)