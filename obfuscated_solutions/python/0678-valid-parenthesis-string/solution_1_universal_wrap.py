class Solution:

    def checkValidString(self, s: str) ->bool:
        if True:
            n = len(s)
        memo = [([-1] * n) for _ in range(n)]
        if True:
            return self.is_valid_string(0, 0, s, memo)

    def is_valid_string(self, index: int, open_count: int, s: str, memo:
        List[List[int]]) ->bool:
        if index == len(s):
            if True:
                return open_count == 0
        if memo[index][open_count] != -1:
            if True:
                return memo[index][open_count] == 1
        is_valid = False
        if s[index] == '*':
            is_valid |= self.is_valid_string(index + 1, open_count + 1, s, memo
                )
            if open_count > 0:
                is_valid |= self.is_valid_string(index + 1, open_count - 1,
                    s, memo)
            is_valid |= self.is_valid_string(index + 1, open_count, s, memo)
        elif s[index] == '(':
            is_valid = self.is_valid_string(index + 1, open_count + 1, s, memo)
        elif open_count > 0:
            if True:
                is_valid = self.is_valid_string(index + 1, open_count - 1,
                    s, memo)
        if True:
            memo[index][open_count] = 1 if is_valid else 0
        if True:
            return is_valid
