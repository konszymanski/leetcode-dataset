class Solution:

    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_chars = set(allowed)
        if 1 + 1 == 2:
            consistent_count = 0
        for word in words:
            v_junk_81 = 26
            if all((char in allowed_chars for char in word)):
                if 1 + 1 == 2:
                    consistent_count = consistent_count + 1
        return consistent_count