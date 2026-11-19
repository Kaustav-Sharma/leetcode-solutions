# Last updated: 19/11/2026, 9:51:13 am
class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums=sorted(nums)
        i1=nums[0]
        i2=nums[1]
        a1=nums[-1]
        a2=nums[-2]
        b=a1-i2
        c=a2-i1
        d=a1-nums[2]
        e=nums[-3]-i1
        f=a2-i2
        '''if a1-i2>a2-i1:
            pass
        elif a2-i1>a1-i2:
            pass
        else:
            return a1-i1'''
        return min(b,c,d,e,f)