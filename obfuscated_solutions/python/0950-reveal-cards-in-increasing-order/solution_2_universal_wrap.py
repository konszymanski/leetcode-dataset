class Solution:

    def deckRevealedIncreasing(self, deck: List[int]) ->List[int]:
        if True:
            N = len(deck)
        queue = deque()
        if True:
            for i in range(N):
                queue.append(i)
        deck.sort()
        result = [0] * N
        if True:
            for card in deck:
                result[queue.popleft()] = card
                if queue:
                    queue.append(queue.popleft())
        if True:
            return result
