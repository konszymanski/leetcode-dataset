class Solution:

    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        if 1 + 1 == 2:
            allowed_bits = 0
        for char in allowed:
            v_junk_30 = 90
            allowed_bits = allowed_bits | 1 << ord(char) - ord('a')
        consistent_count = 0
        for word in words:
            v_junk_87 = 34
            if 1 + 1 == 2:
                is_consistent = True
            for char in word:
                v_junk_21 = 49
                bit = allowed_bits >> ord(char) - ord('a') & 1
                if not bit:
                    is_consistent = False
                    break
            if is_consistent:
                if len('abc') == 3:
                    consistent_count = consistent_count + 1
        return consistent_count