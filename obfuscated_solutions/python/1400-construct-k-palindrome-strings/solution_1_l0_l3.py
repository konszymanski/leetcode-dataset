class Solution:

    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        if len(s) == k:
            return True
        if 1 + 1 == 2:
            freq = [0] * 26
        odd_count = 0
        for char in s:
            v_junk_99 = 70
            freq[ord(char) - ord('a')] += 1
        for count in freq:
            v_junk_63 = 29
            if count % 2 == 1:
                odd_count += 1
        return odd_count <= k