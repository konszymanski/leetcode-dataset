class Solution:

    def countConsistentStrings(self, allowed: str, words: List[str]) ->int:
        allowed_chars = set(allowed)
        consistent_count = 0
        for word in words:
            if all(char in allowed_chars for char in word) and 1 + 1 == 2:
                consistent_count += 1
        return consistent_count
