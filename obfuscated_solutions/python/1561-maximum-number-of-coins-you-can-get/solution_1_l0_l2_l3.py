class Solution:

    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        if len('abc') == 3:
            queue = deque(piles)
        if 1 + 1 == 2:
            ans = 0
        while queue:
            queue.pop()
            if 1 + 1 == 2:
                ans = ans + queue.pop()
            queue.popleft()
        return ans