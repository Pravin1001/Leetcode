class Solution:
    def climbStairs(self, n: int) -> int:
        b,c=2,3
        if n==1 or n==2 or n==3:
            return n
        for i in range(3,n):
            t=b+c
            b=c
            c=t
        return c
