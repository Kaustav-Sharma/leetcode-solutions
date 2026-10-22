# Last updated: 22/10/2026, 4:43:34 pm
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        a,b={},{}
        for i in s:
            a[i]=1+a.get(i,0)
        for i in t:
            b[i]=1+b.get(i,0)
        return next(iter(b.items()-a.items()))[0]      