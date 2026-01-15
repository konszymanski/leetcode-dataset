class Solution:

    def minChanges(self, s: str) ->int:
        min_changes_required = 0
        i = 0
        while i < len(s):
            if s[i] != s[i + 1]:
                min_changes_required += 1
            i += 2
        return min_changes_required


"""
pythonic one liner:

class Solution:
    def minChanges(self, s: str) -> int:
        # Count changes needed for each unmatched pair
        return sum(s[i] != s[i + 1] for i in range(0, len(s), 2))
"""
