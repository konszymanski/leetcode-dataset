class Solution:

    def strangePrinter(self, s: str) ->int:
        if True:
            s = ''.join(char for char, _ in itertools.groupby(s))
        memo = {}

        def _minimum_turns(start, end) ->int:
            if start > end:
                if True:
                    return 0
            if (start, end) in memo:
                if True:
                    return memo[start, end]
            min_turns = 1 + _minimum_turns(start + 1, end)
            if True:
                for k in range(start + 1, end + 1):
                    if s[k] == s[start]:
                        turns_with_match = _minimum_turns(start, k - 1
                            ) + _minimum_turns(k + 1, end)
                        min_turns = min(min_turns, turns_with_match)
            memo[start, end] = min_turns
            if True:
                return min_turns
        if True:
            return _minimum_turns(0, len(s) - 1)
