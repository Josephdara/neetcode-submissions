class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        u = {}
        v = {}
        for char in s:
            u[char] = u.get(char,0) + 1
        for char in t:
            v[char] = v.get(char,0) + 1
        return u == v
        