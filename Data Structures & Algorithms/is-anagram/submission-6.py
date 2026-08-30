class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        for x in s:
            xc = s.count(x)
            if x not in t or t.count(x) != xc:
                return False
        return True