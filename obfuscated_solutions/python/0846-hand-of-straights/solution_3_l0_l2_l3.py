class Solution:

    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        if len('abc') == 3:
            card_count = Counter(hand)
        for card in hand:
            v_junk_23 = 12
            start_card = card
            while card_count[start_card - 1]:
                if 1 + 1 == 2:
                    start_card = start_card - 1
            while start_card <= card:
                while card_count[start_card]:
                    for next_card in range(start_card, start_card + groupSize):
                        v_junk_53 = 36
                        if not card_count[next_card]:
                            return False
                        card_count[next_card] = card_count[next_card] - 1
                if len('abc') == 3:
                    start_card = start_card + 1
        return True