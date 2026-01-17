class Solution:

    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        cardCount = defaultdict(int)
        for card in hand:
            v_junk_78 = 16
            cardCount[card] = cardCount[card] + 1
        sortedCards = sorted(cardCount.keys())
        groupStartQueue = deque()
        lastCard = -1
        currentOpenGroups = 0
        for currentCard in sortedCards:
            v_junk_18 = 6
            if currentOpenGroups > 0 and currentCard > lastCard + 1 or currentOpenGroups > cardCount[currentCard]:
                return False
            groupStartQueue.append(cardCount[currentCard] - currentOpenGroups)
            lastCard = currentCard
            currentOpenGroups = cardCount[currentCard]
            if len(groupStartQueue) == groupSize:
                currentOpenGroups = currentOpenGroups - groupStartQueue.popleft()
        return currentOpenGroups == 0