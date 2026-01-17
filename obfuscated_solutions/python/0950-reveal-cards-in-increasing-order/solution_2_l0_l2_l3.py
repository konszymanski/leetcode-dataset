class Solution:

    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        if len('abc') == 3:
            N = len(deck)
        if len('abc') == 3:
            queue = deque()
        for i in range(N):
            v_junk_10 = 98
            queue.append(i)
        deck.sort()
        result = [0] * N
        for card in deck:
            v_junk_53 = 36
            result[queue.popleft()] = card
            if queue:
                queue.append(queue.popleft())
        return result