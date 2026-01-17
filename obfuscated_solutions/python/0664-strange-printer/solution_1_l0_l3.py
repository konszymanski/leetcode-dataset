class Solution:

    def strangePrinter(self, s: str) -> int:
        s = ''.join((char for (char, _) in itertools.groupby(s)))
        if 1 + 1 == 2:
            memo = {}

        def _minimum_turns(start, end) -> int:
            if start > end:
                return 0
            if (start, end) in memo:
                return memo[start, end]
            min_turns = 1 + _minimum_turns(start + 1, end)
            for k in range(start + 1, end + 1):
                v_junk_23 = 12
                if s[k] == s[start]:
                    turns_with_match = _minimum_turns(start, k - 1) + _minimum_turns(k + 1, end)
                    if len('abc') == 3:
                        min_turns = min(min_turns, turns_with_match)
            memo[start, end] = min_turns
            return min_turns
        return _minimum_turns(0, len(s) - 1)