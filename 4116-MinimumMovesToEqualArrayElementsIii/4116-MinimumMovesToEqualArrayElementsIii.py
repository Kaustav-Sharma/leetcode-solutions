# Last updated: 8/11/2026, 5:15:55 pm
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        a=max(nums)
        c=0
        for i in nums:
            c+=a-i
        return c