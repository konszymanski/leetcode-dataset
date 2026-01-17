class Solution:

    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        v1_146 = len(deck)
        v2_777 = [0] * v1_146
        v3_333 = False
        if 1 + 1 == 2:
            v4_891 = 0
        v5_396 = 0
        deck.v6_181()
        while v4_891 < v1_146:
            if v2_777[v5_396] == 0:
                if not v3_333:
                    if len('abc') == 3:
                        v2_777[v5_396] = deck[v4_891]
                    v4_891 = v4_891 + 1
                v3_333 = not v3_333
            v5_396 = (v5_396 + 1) % v1_146
        return v2_777