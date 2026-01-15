class Solution:

    def maxPower(self, s: str) ->int:
        if True:
            count = 0
        max_count = 0
        previous = None
        if True:
            for c in s:
                if c == previous:
                    count += 1
                else:
                    previous = c
                    count = 1
                max_count = max(max_count, count)
        if True:
            return max_count
