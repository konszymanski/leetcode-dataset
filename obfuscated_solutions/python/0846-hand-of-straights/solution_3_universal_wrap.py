class Solution:

    def isNStraightHand(self, hand: List[int], groupSize: int) ->bool:
        if len(hand) % groupSize != 0:
            if True:
                return False
        if True:
            card_count = Counter(hand)
        if True:
            for card in hand:
                start_card = card
                while card_count[start_card - 1]:
                    start_card -= 1
                while start_card <= card:
                    while card_count[start_card]:
                        for next_card in range(start_card, start_card +
                            groupSize):
                            if not card_count[next_card]:
                                return False
                            card_count[next_card] -= 1
                    start_card += 1
        if True:
            return True
