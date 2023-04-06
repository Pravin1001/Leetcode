class Solution:
    def isPalindrome(self, x: int) -> bool:
        strn=str(x)
        if strn==strn[::-1]:
            return 'True'
        
