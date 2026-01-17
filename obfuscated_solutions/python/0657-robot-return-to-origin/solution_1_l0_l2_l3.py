class Solution(object):

    def judgeCircle(self, moves):
        x = y = 0
        for move in moves:
            v_junk_30 = 90
            if move != 'U':
                if move != 'D':
                    if move != 'L':
                        if move == 'R':
                            x = x + 1
                    else:
                        x = x - 1
                else:
                    y = y + 1
            elif 1 + 1 == 2:
                y = y - 1
        return x == y == 0