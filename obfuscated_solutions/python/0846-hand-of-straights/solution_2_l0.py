class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        cardCount = defaultdict(int)
        for card in hand:
            cardCount[card] += 1
        sortedCards = sorted(cardCount.keys())
        groupStartQueue = deque()
        lastCard = -1
        currentOpenGroups = 0
        for currentCard in sortedCards:
            if (
                currentOpenGroups > 0 and currentCard > lastCard + 1
            ) or currentOpenGroups > cardCount[currentCard]:
                return False
            groupStartQueue.append(cardCount[currentCard] - currentOpenGroups)
            lastCard = currentCard
            currentOpenGroups = cardCount[currentCard]
            if len(groupStartQueue) == groupSize:
                currentOpenGroups -= groupStartQueue.popleft()
        return currentOpenGroups == 0