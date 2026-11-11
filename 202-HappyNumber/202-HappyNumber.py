# Last updated: 11/11/2026, 8:53:19 pm
class Solution:
    def isHappy(self, n: int) -> bool:
        a=set()
        def k(n):
            o=0
            while n:
                o+=(n%10)**2
                n//=10
            return o

        while n not in a:
            a.add(n)
            n=k(n)
            if n==1:
                return True
        return False