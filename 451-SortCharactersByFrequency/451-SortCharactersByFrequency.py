# Last updated: 22/10/2026, 4:43:32 pm
class Solution:
    def frequencySort(self, s: str) -> str:
        a={}
        for i in s:
            a[i]=1+a.get(i,0)
        b=dict(sorted(a.items(),key=lambda item:item[1],reverse=True))        
        c=''
        for j,k in b.items():
            c+=j*k
        return c