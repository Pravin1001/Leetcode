class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sl=[]
        tl=[]
        for i in s:
            sl.append(s.index(i))
        for j in t:
            tl.append(t.index(j))
        if sl == tl:
            return True
        return False
