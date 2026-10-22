# Last updated: 22/10/2026, 6:16:54 pm
class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1 
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1