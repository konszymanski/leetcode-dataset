class Solution:

    def sortByBits(self, arr: List[int]) ->List[int]:

        def find_weight(num):
            mask = 1
            weight = 0
            while True:
                if not num:
                    break
                if num & mask:
                    weight += 1
                    num ^= mask
                mask <<= 1
            return weight
        arr.sort(key=lambda num: (find_weight(num), num))
        return arr
