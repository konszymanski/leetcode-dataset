class Solution:

    def deckRevealedIncreasing(self, deck: List[int]) ->List[int]:
        N = len(deck)
        queue = deque()
        i = 0
        while i < N:
            queue.append(i)
            i += 1
        deck.sort()
        result = [0] * N
        for card in deck:
            result[queue.popleft()] = card
            if queue:
                queue.append(queue.popleft())
        return result
