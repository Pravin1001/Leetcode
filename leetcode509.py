class Solution:
    def fib(self, n: int) -> int:
        if n!=0:
            l=[0]*(n+1)
            l[1]=1
            s=l[0]+l[1]
            for i in range(2,n+1):
                l[i]=l[i-1]+l[i-2]
                s=s+l[i]
            return l[n-1]+l[n-2]
        return 0           
