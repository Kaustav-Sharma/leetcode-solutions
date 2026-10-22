# Last updated: 22/10/2026, 4:43:27 pm
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        a=0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i<j and nums[i]==nums[j] and i*j % k == 0:
                    a=a+1
        return a