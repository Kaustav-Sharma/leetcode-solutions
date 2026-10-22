# Last updated: 22/10/2026, 4:43:35 pm
class Solution:
    def firstUniqChar(self, s: str) -> int:
        a = {}

        for c in s:
            a[c] = 1 + a.get(c, 0)
        
        for i, c in enumerate(s):
            if a[c] == 1:
                return i
        
        return -1