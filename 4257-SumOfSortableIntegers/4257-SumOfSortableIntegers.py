# Last updated: 22/10/2026, 4:43:24 pm
from math import sqrt

class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        d=[]
        for l in range(1,int(sqrt(len(nums)))+1):
            if len(nums)%l==0:
                d.append(l)
                if len(nums)//l !=l:
                    d.append(len(nums)//l)

        tar=sorted(nums)
        
        if nums == tar:
            return sum(d)

        s=0

        def t(o,p,i):
            while p<=len(nums):
                chunk = nums[o:p]
                target = tar[o:p]
                
                # Fast fail: If min or max don't match, it's impossible to be a valid cyclic shift
                if min(chunk) != target[0] or max(chunk) != target[-1]:
                    return False

                e = chunk * 2
                r = False
                
                # Cache these to avoid looking them up repeatedly
                first_val = target[0]
                last_val = target[-1]
                
                for k in range(i):
                    # Only do the expensive slice if BOTH the start and end of the window match
                    if e[k] == first_val and e[k+i-1] == last_val:
                        if e[k:k+i] == target:
                            r = True
                            break
                            
                if not r:
                    return False
                o=p
                p+=i
            return True
        
        for i in d:
            j=0
            if t(j,i,i):
                s+=i
        
        return s