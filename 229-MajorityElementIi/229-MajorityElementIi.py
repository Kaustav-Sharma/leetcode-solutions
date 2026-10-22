# Last updated: 22/10/2026, 4:43:39 pm
class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        a={}
        b=[]
        for i in nums:
            if i in a:
                a[i]+=1
            else:
                a[i]=1
        for i in a:
            if len(nums)/3<a[i]:
                b.append(i)
        return b