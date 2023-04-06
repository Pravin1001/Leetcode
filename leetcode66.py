class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digittemp=[]
        digitl=[]
        for i in digits:
            temp=str(i)
            digittemp.append(temp)
        digit=''.join(digittemp)
        digitn=int(digit)+1
        for i in str(digitn):
            digitl.append(int(i))
        return digitl
