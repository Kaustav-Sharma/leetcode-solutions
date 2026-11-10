# Last updated: 10/11/2026, 6:00:43 pm
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        n=len(nums)
        i=0
        maxi=float('-inf')
        total=0                                              
        while i<n:                                         
            total=total+nums[i]                      
            maxi=max(maxi,total)
            if total<0:
                total=0
            i+=1
        return maxi