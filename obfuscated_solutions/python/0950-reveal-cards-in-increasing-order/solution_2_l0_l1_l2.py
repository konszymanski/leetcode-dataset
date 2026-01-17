class Solution:

    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        v1_754 = len(deck)
        v2_214 = v3_125()
        for v4_859 in range(v1_754):
            v2_214.v5_381(v4_859)
        deck.v6_350()
        v7_328 = [0] * v1_754
        for v8_242 in deck:
            v7_328[v2_214.v9_854()] = v8_242
            if v2_214:
                v2_214.v5_381(v2_214.v9_854())
        return v7_328