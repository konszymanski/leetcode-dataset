class Solution:

    def countConsistentStrings(self, allowed: str, words: List[str]) ->int:
        if True:
            allowed_chars = set(allowed)
        consistent_count = 0
        if True:
            for word in words:
                if all(char in allowed_chars for char in word):
                    consistent_count += 1
        if True:
            return consistent_count
