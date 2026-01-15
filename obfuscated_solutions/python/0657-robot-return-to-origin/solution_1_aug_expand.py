class Solution(object):

    def judgeCircle(self, moves):
        x = y = 0
        for move in moves:
            if move == 'U':
                y = y - 1
            elif move == 'D':
                y = y + 1
            elif move == 'L':
                x = x - 1
            elif move == 'R':
                x = x + 1
        return x == y == 0
