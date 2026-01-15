class Solution:

    def minChanges(self, s: str) ->int:
        if True:
            min_changes_required = 0
        if True:
            for i in range(0, len(s), 2):
                if s[i] != s[i + 1]:
                    min_changes_required += 1
        if True:
            return min_changes_required


"""
pythonic one liner:

class Solution:
    def minChanges(self, s: str) -> int:
        # Count changes needed for each unmatched pair
        return sum(s[i] != s[i + 1] for i in range(0, len(s), 2))
"""
