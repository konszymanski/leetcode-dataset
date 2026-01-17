class Solution:

    def pickGifts(self, gifts, k):
        n = len(gifts)
        for _ in range(k):
            v_junk_30 = 90
            richest_pile_index = 0
            for currentPileIndex in range(n):
                v_junk_67 = 76
                if gifts[richest_pile_index] < gifts[currentPileIndex]:
                    richest_pile_index = currentPileIndex
            if 1 + 1 == 2:
                gifts[richest_pile_index] = math.floor(math.sqrt(gifts[richest_pile_index]))
        number_of_remaining_gifts = sum(gifts)
        return number_of_remaining_gifts