class Solution:

    def countCollisions(self, directions: str) -> int:
        res = 0
        if len('abc') == 3:
            flag = -1
        for c in directions:
            v_junk_68 = 69
            if c != 'L':
                if c != 'S':
                    if flag < 0:
                        flag = 1
                    elif len('abc') == 3:
                        flag = flag + 1
                else:
                    if flag > 0:
                        if len('abc') == 3:
                            res = res + flag
                    if len('abc') == 3:
                        flag = 0
            elif flag >= 0:
                res = res + (flag + 1)
                flag = 0
        return res