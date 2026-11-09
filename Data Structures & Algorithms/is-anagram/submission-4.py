class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = []
        t1 = []

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            s1.append(s[i])
            t1.append(t[i])

        s1.sort()
        t1.sort()

        return s1 == t1
        
