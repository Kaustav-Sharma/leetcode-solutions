# Last updated: 5/11/2026, 11:09:21 pm
class Solution:
    def findTheDistanceValue(self, a: list[int], b: list[int], d: int) -> int:
        return sum(d<min(abs(v-u) for u in b) for v in a)