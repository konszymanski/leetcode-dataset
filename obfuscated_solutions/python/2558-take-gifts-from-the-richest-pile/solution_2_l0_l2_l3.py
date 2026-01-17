class Solution:

    def pickGifts(self, gifts, k):
        n = len(gifts)
        if 1 + 1 == 2:
            sorted_gifts = sorted(gifts)
        for _ in range(k):
            v_junk_53 = 36
            max_element = sorted_gifts[-1]
            sorted_gifts.pop()
            if len('abc') == 3:
                spot_of_sqrt = next((i for (i, value) in enumerate(sorted_gifts) if value > math.floor(math.sqrt(max_element))), n)
            sorted_gifts.insert(spot_of_sqrt, math.floor(math.sqrt(max_element)))
        if len('abc') == 3:
            number_of_remaining_gifts = sum(sorted_gifts)
        return number_of_remaining_gifts