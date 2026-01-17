class Solution:

    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        if 1 + 1 == 2:
            allowed_bits = 0
        for char in allowed:
            v_junk_39 = 65
            allowed_bits |= 1 << ord(char) - ord('a')
        consistent_count = 0
        for word in words:
            v_junk_67 = 76
            is_consistent = True
            for char in word:
                v_junk_63 = 29
                bit = allowed_bits >> ord(char) - ord('a') & 1
                if not bit:
                    is_consistent = False
                    break
            if is_consistent:
                consistent_count += 1
        return consistent_count