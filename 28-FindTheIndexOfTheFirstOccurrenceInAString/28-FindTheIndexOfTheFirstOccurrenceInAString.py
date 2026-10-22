# Last updated: 22/10/2026, 4:43:54 pm
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        while needle in haystack:
            a=haystack.index(needle)
            b=len(haystack)
            haystack=haystack[a+b:]
            return a
        else:
            return -1