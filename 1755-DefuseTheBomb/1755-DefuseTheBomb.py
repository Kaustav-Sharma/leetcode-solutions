# Last updated: 11/11/2026, 4:44:05 pm
class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]:
        new = [0] * len(code)
        if k < 0:
            for i in range(len(code)):
                for j in range(0,k,-1):
                    new[i] += code[(i-1+j)%len(code)]
            return new
        else:
            for i in range(len(code)):
                for j in range(k):
                    new[i] += code[(i+1+j)%len(code)]
            return new