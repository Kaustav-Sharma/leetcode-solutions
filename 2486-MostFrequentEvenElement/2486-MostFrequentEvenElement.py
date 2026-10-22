# Last updated: 22/10/2026, 4:43:19 pm
class Solution:
    def mostFrequentEven(self, nums: list[int]) -> int:
        a={}
        for i in nums:
            if i%2==0:
                if i in a:
                    a[i]+=1
                else:
                    a[i]=1
        if a=={}:
            return -1
        else :
            mac=max(a.values())
            keys = [key for key, val in a.items() if val == mac]        
            return min(keys)