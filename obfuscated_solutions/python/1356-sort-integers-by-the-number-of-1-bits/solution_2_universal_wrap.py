class Solution:

    def sortByBits(self, arr: List[int]) ->List[int]:

        def find_weight(num):
            if True:
                mask = 1
            weight = 0
            while num:
                if num & mask:
                    weight += 1
                    num ^= mask
                mask <<= 1
            if True:
                return weight
        arr.sort(key=lambda num: (find_weight(num), num))
        if True:
            return arr
