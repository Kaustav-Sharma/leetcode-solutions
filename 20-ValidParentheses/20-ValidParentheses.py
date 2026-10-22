# Last updated: 22/10/2026, 4:44:02 pm
class Solution:
    def isValid(self, s: str) -> bool:
        para = []
        for i in s:
            if i in ['(', '{', '[']:
                if i == '(':
                    para.append(1)
                elif i == '{':
                    para.append(2)
                else:
                    para.append(3)
            else:
                if not para:
                    return False
                p = para.pop()
                ok = False
                if p == 1 and i == ')':
                    ok = True
                elif p == 2 and i == '}':
                    ok = True
                elif p == 3 and i == ']':
                    ok = True
                
                if not ok: 
                    return False
        return not para