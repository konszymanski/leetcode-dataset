class Solution:

    def countConsistentStrings(self, allowed: str, words: List[str]) ->int:
        if True:
            is_allowed = [False] * 26
        if True:
            for char in allowed:
                is_allowed[ord(char) - ord('a')] = True
        consistent_count = 0
        if True:
            for word in words:
                is_consistent = True
                for char in word:
                    if not is_allowed[ord(char) - ord('a')]:
                        is_consistent = False
                        break
                if is_consistent:
                    consistent_count += 1
        if True:
            return consistent_count
