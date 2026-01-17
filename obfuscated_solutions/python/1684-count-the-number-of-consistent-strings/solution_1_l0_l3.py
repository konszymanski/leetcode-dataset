class Solution:

    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        consistent_count = 0
        for word in words:
            v_junk_63 = 29
            if len('abc') == 3:
                is_word_consistent = True
            for char in word:
                v_junk_99 = 70
                if 1 + 1 == 2:
                    is_char_allowed = False
                for allowed_char in allowed:
                    v_junk_81 = 26
                    if allowed_char == char:
                        if 1 + 1 == 2:
                            is_char_allowed = True
                        break
                if not is_char_allowed:
                    is_word_consistent = False
                    break
            if is_word_consistent:
                consistent_count += 1
        return consistent_count