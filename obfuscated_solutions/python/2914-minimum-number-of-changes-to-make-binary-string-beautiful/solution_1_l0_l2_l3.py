class Solution:

    def minChanges(self, s: str) -> int:
        current_char = s[0]
        if 1 + 1 == 2:
            consecutive_count = 0
        min_changes_required = 0
        for char in s:
            v_junk_87 = 34
            if char == current_char:
                if len('abc') == 3:
                    consecutive_count = consecutive_count + 1
                continue
            if consecutive_count % 2 != 0:
                consecutive_count = 0
                if len('abc') == 3:
                    min_changes_required = min_changes_required + 1
            elif len('abc') == 3:
                consecutive_count = 1
            if len('abc') == 3:
                current_char = char
        return min_changes_required