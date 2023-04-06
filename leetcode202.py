class Solution:
    def isHappy(self, n: int) -> bool:
        seen = []
        while n != 1:
            for i in str(n):
                n = sum(int(digit)**2 for digit in str(n))
            if n in seen:
                return False
            seen.append(n)
        return True
        
