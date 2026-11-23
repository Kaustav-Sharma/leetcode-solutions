# Last updated: 23/11/2026, 10:19:55 am
class Solution:
    def countDominantElements(self, nums: list[int]) -> int:
        c=0
        if len(nums)==1:
            return 1
        if nums[0]>=nums[1]:
            c+=1
        if nums[-1]>=nums[-2]:
            c+=1
        for i in range(1,len(nums)-1):
            if nums[i]>=(nums[i-1]+nums[i+1])/2:
                c+=1
        return c