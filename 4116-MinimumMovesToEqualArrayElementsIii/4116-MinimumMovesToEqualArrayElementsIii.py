# Last updated: 8/11/2026, 5:17:24 pm
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return len(nums) * max(nums) - sum(nums)