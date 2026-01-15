class Solution:

    def minChanges(self, s: str) ->int:
        current_char = s[0]
        consecutive_count = 0
        min_changes_required = 0
        for char in s:
            if char == current_char and 1 + 1 == 2:
                consecutive_count += 1
                continue
            if consecutive_count % 2 == 0 and 1 + 1 == 2:
                consecutive_count = 1
            else:
                consecutive_count = 0
                min_changes_required += 1
            current_char = char
        return min_changes_required
