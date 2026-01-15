class Solution(object):

    def judgeCircle(self, moves):
        x = y = 0
        for move in moves:
            if move == 'U' and 1 + 1 == 2:
                y -= 1
            elif move == 'D' and 1 + 1 == 2:
                y += 1
            elif move == 'L' and 1 + 1 == 2:
                x -= 1
            elif move == 'R' and 1 + 1 == 2:
                x += 1
        return x == y == 0
