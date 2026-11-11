# Last updated: 11/11/2026, 9:17:36 pm
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=list(s)
        while s[-1]==" ":
            s.pop()
        for j,i in enumerate(s[::-1]):
            if i==" ":
                return j
        return len(s)