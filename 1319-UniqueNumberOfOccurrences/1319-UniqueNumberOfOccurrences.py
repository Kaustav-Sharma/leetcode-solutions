# Last updated: 11/11/2026, 6:38:09 pm
class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        a={}
        for i in arr:
            a[i]=1+a.get(i,0)
        if len(set(a.values()))==len(a):
            return True
        else:
            return False