# Last updated: 22/10/2026, 4:43:26 pm
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        a=[]
        for i, value in enumerate(words):
            if x in value:
                a.append(i)
        return(a)