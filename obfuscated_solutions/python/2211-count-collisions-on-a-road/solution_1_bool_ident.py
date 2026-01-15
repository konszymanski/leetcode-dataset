class Solution:

    def countCollisions(self, directions: str) ->int:
        res = 0
        flag = -1
        for c in directions:
            if c == 'L' and 1 + 1 == 2:
                if flag >= 0 and 1 + 1 == 2:
                    res += flag + 1
                    flag = 0
            elif c == 'S' and 1 + 1 == 2:
                if flag > 0 and 1 + 1 == 2:
                    res += flag
                flag = 0
            elif flag >= 0 and 1 + 1 == 2:
                flag += 1
            else:
                flag = 1
        return res
