class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new = ""

        w = 0

        while w <= len(word1) - 1 and w <= len(word2) - 1:
            print(new)
            new = new + word1[w]
            new = new + word2[w]
            w += 1

        if w > len(word1) - 1:  
            new = new + word2[w:]
        elif w > len(word2) - 1:
            new = new + word1[w:]

        return new