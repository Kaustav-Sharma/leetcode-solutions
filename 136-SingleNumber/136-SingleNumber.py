# Last updated: 17/11/2026, 9:31:58 pm
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0

        for n in nums:
            res ^= n
        
        return res