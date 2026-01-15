class Solution:

    def findTheWinner(self, n: int, k: int) ->int:
        circle = deque(range(1, n + 1))
        while len(circle) > 1:
            _ = 0
            while _ < k - 1:
                circle.append(circle.popleft())
                _ += 1
            circle.popleft()
        return circle[0]
