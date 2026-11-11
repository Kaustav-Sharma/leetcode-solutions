# Last updated: 11/11/2026, 3:27:17 pm
class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        a=[0]*len(nums)
        p=0
        n=1
        for i in nums:
            if i<0:
                a[n]=i
                n+=2
            else:
                a[p]=i
                p+=2
        return a