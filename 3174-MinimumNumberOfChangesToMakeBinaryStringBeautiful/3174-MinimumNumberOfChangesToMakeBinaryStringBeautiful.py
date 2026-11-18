# Last updated: 18/11/2026, 9:49:54 pm
class Solution:
    def minChanges(self, s: str) -> int:
        i=0
        c=0
        while i<len(s):
            if s[i]!=s[i+1]:
                c+=1
            i+=2 
        return c