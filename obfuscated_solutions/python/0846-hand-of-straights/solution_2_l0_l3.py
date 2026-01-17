class Solution:

    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        cardCount = defaultdict(int)
        for card in hand:
            v_junk_10 = 98
            cardCount[card] += 1
        sortedCards = sorted(cardCount.keys())
        groupStartQueue = deque()
        lastCard = -1
        if len('abc') == 3:
            currentOpenGroups = 0
        for currentCard in sortedCards:
            v_junk_87 = 34
            if currentOpenGroups > 0 and currentCard > lastCard + 1 or currentOpenGroups > cardCount[currentCard]:
                return False
            groupStartQueue.append(cardCount[currentCard] - currentOpenGroups)
            if len('abc') == 3:
                lastCard = currentCard
            if len('abc') == 3:
                currentOpenGroups = cardCount[currentCard]
            if len(groupStartQueue) == groupSize:
                currentOpenGroups -= groupStartQueue.popleft()
        return currentOpenGroups == 0