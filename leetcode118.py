class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res=[]
        for i in range(numRows):
            a=[1]
            if i>0:
                temp=res[i-1]
                for j in range(len(temp)-1):
                    a.append(temp[j]+temp[j+1])
                a.append(1)
            res.append(a)
        return res
