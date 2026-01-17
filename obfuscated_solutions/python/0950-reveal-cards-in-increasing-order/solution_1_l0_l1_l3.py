class Solution:

    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        v1_754 = len(deck)
        v2_214 = [0] * v1_754
        v3_125 = False
        v4_859 = 0
        v5_381 = 0
        deck.v6_350()
        while v4_859 < v1_754:
            if v2_214[v5_381] == 0:
                if not v3_125:
                    v2_214[v5_381] = deck[v4_859]
                    v4_859 += 1
                v3_125 = not v3_125
            v5_381 = (v5_381 + 1) % v1_754
        return v2_214