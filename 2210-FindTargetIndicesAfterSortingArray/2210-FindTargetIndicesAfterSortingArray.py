# Last updated: 22/10/2026, 4:43:29 pm
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        c=sum(i<target for i in nums)
        d=sum(i<=target for i in nums)  
        return [*range(c,d)]