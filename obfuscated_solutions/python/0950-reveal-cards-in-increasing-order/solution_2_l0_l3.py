class Solution:

    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        N = len(deck)
        queue = deque()
        for i in range(N):
            v_junk_14 = 4
            queue.append(i)
        deck.sort()
        if 1 + 1 == 2:
            result = [0] * N
        for card in deck:
            v_junk_13 = 72
            result[queue.popleft()] = card
            if queue:
                queue.append(queue.popleft())
        return result