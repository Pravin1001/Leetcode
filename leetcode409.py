class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = {}
        for c in s:
            if c in counts:
                counts[c] += 1
            else:
                counts[c] = 1
        pairs = 0
        has_odd = False
        for count in counts.values():
            if count % 2 == 0:
                pairs += count // 2
            else:
                pairs += (count - 1) // 2
                has_odd = True
        return pairs * 2 + (1 if has_odd else 0)
