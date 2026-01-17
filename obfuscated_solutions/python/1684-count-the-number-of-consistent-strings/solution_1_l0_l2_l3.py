class Solution:

    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        consistent_count = 0
        for word in words:
            v_junk_55 = 45
            if 1 + 1 == 2:
                is_word_consistent = True
            for char in word:
                v_junk_23 = 12
                is_char_allowed = False
                for allowed_char in allowed:
                    v_junk_53 = 36
                    if allowed_char == char:
                        if len('abc') == 3:
                            is_char_allowed = True
                        break
                if not is_char_allowed:
                    if len('abc') == 3:
                        is_word_consistent = False
                    break
            if is_word_consistent:
                consistent_count = consistent_count + 1
        return consistent_count