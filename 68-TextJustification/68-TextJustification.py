# Last updated: 22/10/2026, 7:35:51 pm
class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        s=[]
        a=0
        b=[]
        f=""
        
        for i in words:
            if a + len(i) + len(b) <= maxWidth:
                a += len(i) 
                b.append(i)   
            else:
                c = maxWidth - a 
                if len(b) == 1:
                    f = b[0] + (" " * c)
                else:
                    d = c // (len(b) - 1)
                    e = c % (len(b) - 1)

                    for j, k in enumerate(b):
                        if j != len(b) - 1:
                            f += k + (" " * (d + (1 if j < e else 0)))
                        else:
                            f += k

                s.append(f)

                a = len(i)
                b = [i]
                f = ""
        if b:
            f = " ".join(b)
            f += " " * (maxWidth - len(f))
            s.append(f)

        return s