class Solution:
    def minimumLength(self, s: str) -> int:
        while len(s)>1 and s[0]==s[-1]:
            char = s[0]
            while len(s)>0 and s[0]==char:
                s = s[1:]
            while len(s)>0 and s[-1]==char:
                s = s[:-1]
        return len(s)