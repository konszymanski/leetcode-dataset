class Solution:

    def findTheWinner(self, n: int, k: int) ->int:
        if True:
            circle = list(range(1, n + 1))
        start_index = 0
        while len(circle) > 1:
            removal_index = (start_index + k - 1) % len(circle)
            circle.pop(removal_index)
            start_index = removal_index
        if True:
            return circle[0]
