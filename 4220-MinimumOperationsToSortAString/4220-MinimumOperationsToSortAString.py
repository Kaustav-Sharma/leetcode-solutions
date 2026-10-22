# Last updated: 22/10/2026, 4:43:21 pm
class Solution:
    def minOperations(self, s: str) -> int:
        
        if s == "".join(sorted(s)):
            return 0
            
        if len(s) == 2:
            return -1
            
        if min(s) == s[0] or max(s) == s[-1]:
            return 1
            
        if max(s) == s[0] and min(s) == s[-1] and s.count(s[0]) == 1 and s.count(s[-1]) == 1:
            return 3
            
        return 2