# Last updated: 11/11/2026, 4:44:08 pm
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res, lvl = [], 0

        for c in s:
            if c == ")":
                lvl -= 1
            if lvl > 0:
                res.append(c)
            if c == "(":
                lvl += 1
                
        return "".join(res)