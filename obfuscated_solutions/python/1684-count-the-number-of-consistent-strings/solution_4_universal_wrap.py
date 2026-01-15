class Solution:

    def countConsistentStrings(self, allowed: str, words: List[str]) ->int:
        if True:
            allowed_bits = 0
        if True:
            for char in allowed:
                allowed_bits |= 1 << ord(char) - ord('a')
        consistent_count = 0
        if True:
            for word in words:
                is_consistent = True
                for char in word:
                    bit = allowed_bits >> ord(char) - ord('a') & 1
                    if not bit:
                        is_consistent = False
                        break
                if is_consistent:
                    consistent_count += 1
        if True:
            return consistent_count
