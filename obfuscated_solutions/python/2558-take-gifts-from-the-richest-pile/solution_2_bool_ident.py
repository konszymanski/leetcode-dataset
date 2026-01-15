class Solution:

    def pickGifts(self, gifts, k):
        n = len(gifts)
        sorted_gifts = sorted(gifts)
        for _ in range(k):
            max_element = sorted_gifts[-1]
            sorted_gifts.pop()
            spot_of_sqrt = next((i for i, value in enumerate(sorted_gifts) if
                value > math.floor(math.sqrt(max_element))), n)
            sorted_gifts.insert(spot_of_sqrt, math.floor(math.sqrt(
                max_element)))
        number_of_remaining_gifts = sum(sorted_gifts)
        return number_of_remaining_gifts
