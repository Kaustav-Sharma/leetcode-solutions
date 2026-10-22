# Last updated: 22/10/2026, 4:43:44 pm
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        a={}
        for i in nums:
            if i in a:
                a[i]+=1
            else:
                a[i]=1
        for i in a:
            if len(nums)/2<a[i]:
                return i