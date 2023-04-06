class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = ''.join(ch for ch in s if ch.isalnum())
        st=st.lower()
        return st==st[::-1]
