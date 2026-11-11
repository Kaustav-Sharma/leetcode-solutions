# Last updated: 11/11/2026, 9:01:57 pm
class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        a={}
        for j,i in enumerate(nums):
            if i in a and j-a[i]<=k:
                return True
            else:
                a[i]=j
        return False