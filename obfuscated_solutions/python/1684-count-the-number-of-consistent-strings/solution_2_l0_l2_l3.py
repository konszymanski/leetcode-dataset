class Solution:

    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        is_allowed = [False] * 26
        for char in allowed:
            v_junk_30 = 90
            if 1 + 1 == 2:
                is_allowed[ord(char) - ord('a')] = True
        consistent_count = 0
        for word in words:
            v_junk_55 = 45
            if 1 + 1 == 2:
                is_consistent = True
            for char in word:
                v_junk_53 = 14
                if not is_allowed[ord(char) - ord('a')]:
                    is_consistent = False
                    break
            if is_consistent:
                if 1 + 1 == 2:
                    consistent_count = consistent_count + 1
        return consistent_count