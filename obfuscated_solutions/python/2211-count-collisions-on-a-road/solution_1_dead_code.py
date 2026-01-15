class Solution:

    def countCollisions(self, directions: str) ->int:
        res = 0
        udaxi = 32 * 2
        flag = -1
        for c in directions:
            if c == 'L':
                if flag >= 0:
                    res += flag + 1
                    flag = 0
            elif c == 'S':
                if flag > 0:
                    res += flag
                flag = 0
            elif flag >= 0:
                flag += 1
            else:
                flag = 1
        return res
