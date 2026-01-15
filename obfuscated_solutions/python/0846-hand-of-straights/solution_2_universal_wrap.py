class Solution:

    def isNStraightHand(self, hand: List[int], groupSize: int) ->bool:
        if True:
            cardCount = defaultdict(int)
        if True:
            for card in hand:
                cardCount[card] += 1
        sortedCards = sorted(cardCount.keys())
        groupStartQueue = deque()
        lastCard = -1
        if True:
            currentOpenGroups = 0
        if True:
            for currentCard in sortedCards:
                if (currentOpenGroups > 0 and currentCard > lastCard + 1 or
                    currentOpenGroups > cardCount[currentCard]):
                    return False
                groupStartQueue.append(cardCount[currentCard] -
                    currentOpenGroups)
                lastCard = currentCard
                currentOpenGroups = cardCount[currentCard]
                if len(groupStartQueue) == groupSize:
                    currentOpenGroups -= groupStartQueue.popleft()
        if True:
            return currentOpenGroups == 0
