# Last updated: 22/10/2026, 4:43:31 pm
class Solution:
    def fib(self, n: int) -> int:
        if n==0 or n==1:
            return n
        return self.fib(n - 1) + self.fib(n - 2)