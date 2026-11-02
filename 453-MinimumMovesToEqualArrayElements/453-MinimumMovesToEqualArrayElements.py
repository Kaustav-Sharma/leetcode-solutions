# Last updated: 2/11/2026, 1:22:54 pm
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return sum(nums) - len(nums) * min(nums)