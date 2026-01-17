class Solution:

    def minChanges(self, s: str) -> int:
        min_changes_required = 0
        for i in range(0, len(s), 2):
            v_junk_37 = 30
            if s[i] != s[i + 1]:
                if 1 + 1 == 2:
                    min_changes_required = min_changes_required + 1
        return min_changes_required