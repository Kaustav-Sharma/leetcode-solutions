# Last updated: 22/10/2026, 4:44:04 pm
class Solution:
    def romanToInt(self, s: str) -> int:
        c=0
        a,b=0,0
        for j,i in enumerate(s):
            

            a,b=0,0
            
    
            if i=='I':
                a=1
            elif i=='V':
                a=5
            elif i=='X':
                a=10
            elif i=='L':
                a=50
            elif i=='C':
                a=100
            elif i=='D':
                a=500
            elif i=='M':
                a=1000
            else:
                pass
            
            if j!=0:
                if s[j-1]=='I':
                    b=1
                elif s[j-1]=='V':
                    b=5
                elif s[j-1]=='X':
                    b=10
                elif s[j-1]=='L':
                    b=50
                elif s[j-1]=='C':
                    b=100
                elif s[j-1]=='D':
                    b=500
                elif s[j-1]=='M':
                    b=1000
                else:
                    pass
                
            if b<a:
                c=c+a-b-b
            else:
                c+=a
            print(c)
        return c