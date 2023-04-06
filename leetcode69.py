class Solution:
    def mySqrt(self, x: int) -> int:
        temp=0.5*x
        for i in range(100):
            if temp>0:
                root=0.5*(temp+x/temp)
                temp=root
            else:
                root=temp=0
        return int(temp)
