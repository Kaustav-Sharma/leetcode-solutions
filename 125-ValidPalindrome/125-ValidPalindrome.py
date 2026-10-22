# Last updated: 22/10/2026, 4:43:47 pm
class Solution:
    def isPalindrome(self, s: str) -> bool:
        return "".join(filter(str.isalnum, s)).lower() == "".join(filter(str.isalnum, s)).lower()[::-1]