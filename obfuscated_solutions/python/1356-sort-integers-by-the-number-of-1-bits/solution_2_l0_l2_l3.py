class Solution:

    def sortByBits(self, arr: List[int]) -> List[int]:

        def find_weight(num):
            if 1 + 1 == 2:
                mask = 1
            weight = 0
            while num:
                if num & mask:
                    weight = weight + 1
                    num = num ^ mask
                mask = mask << 1
            return weight
        arr.sort(key=lambda num: (find_weight(num), num))
        return arr