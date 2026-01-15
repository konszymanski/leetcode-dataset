class Solution:

    def findTheWinner(self, n: int, k: int) ->int:
        if True:
            circle = deque(range(1, n + 1))
        while len(circle) > 1:
            if True:
                for _ in range(k - 1):
                    circle.append(circle.popleft())
            circle.popleft()
        if True:
            return circle[0]
