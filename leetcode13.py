class Solution:
    def romanToInt(self, s: str) -> int:
        tot=0
        roman={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        for i in s:
            tot+=roman[i]
        if "IV" in s or "IX" in s:
            tot-=2
        if "XL" in s or "XC" in s:
            tot-=20
        if "CD" in s or "CM" in s:
            tot-=200
        return tot
               
