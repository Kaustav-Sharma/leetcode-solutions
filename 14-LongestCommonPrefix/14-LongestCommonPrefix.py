# Last updated: 22/10/2026, 4:54:49 pm
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        a = strs[0]
        for i in strs[1:]:
            c = 0
            for j in i:
                if c < len(a) and j == a[c]:
                    c += 1
                else:
                    break  
            a = a[:c]
            
        return a