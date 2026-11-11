# Last updated: 11/11/2026, 8:56:27 pm
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        a={}
        for i in nums:
            a[i]=1+a.get(i,0)
        for i in a.values():
            if i>1:
                return True
        return False