class Solution(object):

    def judgeCircle(self, moves):
        x = y = 0
        for move in moves:
            if move != 'U':
                if move != 'D':
                    if move != 'L':
                        if move == 'R':
                            x += 1
                    else:
                        x -= 1
                else:
                    y += 1
            else:
                y -= 1
        return x == y == 0
