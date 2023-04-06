class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        l=[]
        r=0
        for i in mat:
            l.append([sum(i),r])
            r+=1
        l.sort()
        end=[]
        for i in range(k):
            end.append(l[i][1])
        return end
