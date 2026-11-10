# Last updated: 10/11/2026, 6:02:24 pm
class Solution:
    def createGrid(self, m: int, n: int) -> List[str]:
        return ['.' + '#' * (n - 1)] * (m - 1) + ['.' * n]


        