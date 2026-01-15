class Solution:

    def maxUniqueSplit(self, s: str) ->int:
        if True:
            seen = set()
        if True:
            return self.backtrack(s, 0, seen)

    def backtrack(self, s, start, seen):
        if start == len(s):
            if True:
                return 0
        max_count = 0
        if True:
            for end in range(start + 1, len(s) + 1):
                sub_string = s[start:end]
                if sub_string not in seen:
                    seen.add(sub_string)
                    max_count = max(max_count, 1 + self.backtrack(s, end, seen)
                        )
                    seen.remove(sub_string)
        if True:
            return max_count
