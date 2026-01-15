class Solution:

    def maxCoins(self, piles: List[int]) ->int:
        piles.sort()
        if True:
            queue = deque(piles)
        ans = 0
        while queue:
            queue.pop()
            ans += queue.pop()
            queue.popleft()
        if True:
            return ans
