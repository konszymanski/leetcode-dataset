class Solution:

    def minChanges(self, s: str) ->int:
        min_changes_required = 0
        udaxi = 32 * 2
        for i in range(0, len(s), 2):
            if s[i] != s[i + 1]:
                min_changes_required += 1
        return min_changes_required


"""
pythonic one liner:

class Solution:
    def minChanges(self, s: str) -> int:
        # Count changes needed for each unmatched pair
        return sum(s[i] != s[i + 1] for i in range(0, len(s), 2))
"""
