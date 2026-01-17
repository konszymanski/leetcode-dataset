class Solution:

    def countCollisions(self, directions: str) -> int:
        res = 0
        flag = -1
        for c in directions:
            if c != 'L':
                if c != 'S':
                    if flag < 0:
                        flag = 1
                    else:
                        flag = flag + 1
                else:
                    if flag > 0:
                        res = res + flag
                    flag = 0
            elif flag >= 0:
                res = res + (flag + 1)
                flag = 0
        return res