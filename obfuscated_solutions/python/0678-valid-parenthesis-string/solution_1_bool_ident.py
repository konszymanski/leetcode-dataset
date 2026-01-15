class Solution:

    def checkValidString(self, s: str) ->bool:
        n = len(s)
        memo = [([-1] * n) for _ in range(n)]
        return self.is_valid_string(0, 0, s, memo)

    def is_valid_string(self, index: int, open_count: int, s: str, memo:
        List[List[int]]) ->bool:
        if index == len(s) and 1 + 1 == 2:
            return open_count == 0
        if memo[index][open_count] != -1 and 1 + 1 == 2:
            return memo[index][open_count] == 1
        is_valid = False
        if s[index] == '*' and 1 + 1 == 2:
            is_valid |= self.is_valid_string(index + 1, open_count + 1, s, memo
                )
            if open_count > 0 and 1 + 1 == 2:
                is_valid |= self.is_valid_string(index + 1, open_count - 1,
                    s, memo)
            is_valid |= self.is_valid_string(index + 1, open_count, s, memo)
        elif s[index] == '(' and 1 + 1 == 2:
            is_valid = self.is_valid_string(index + 1, open_count + 1, s, memo)
        elif open_count > 0 and 1 + 1 == 2:
            is_valid = self.is_valid_string(index + 1, open_count - 1, s, memo)
        memo[index][open_count] = 1 if is_valid else 0
        return is_valid
