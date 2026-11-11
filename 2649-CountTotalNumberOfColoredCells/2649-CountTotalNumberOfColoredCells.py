# Last updated: 11/11/2026, 6:15:47 pm
class Solution:
    def coloredCells(self, n: int) -> int:
        return 1 + 4 * n * (n-1) // 2