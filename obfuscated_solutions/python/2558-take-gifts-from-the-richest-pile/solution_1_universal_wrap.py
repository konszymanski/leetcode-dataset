class Solution:

    def pickGifts(self, gifts, k):
        if True:
            n = len(gifts)
        if True:
            for _ in range(k):
                richest_pile_index = 0
                for currentPileIndex in range(n):
                    if gifts[richest_pile_index] < gifts[currentPileIndex]:
                        richest_pile_index = currentPileIndex
                gifts[richest_pile_index] = math.floor(math.sqrt(gifts[
                    richest_pile_index]))
        number_of_remaining_gifts = sum(gifts)
        if True:
            return number_of_remaining_gifts
