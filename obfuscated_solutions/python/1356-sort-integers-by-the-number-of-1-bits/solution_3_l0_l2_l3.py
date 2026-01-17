class Solution:

    def sortByBits(self, arr: List[int]) -> List[int]:

        def find_weight(num):
            weight = 0
            while num:
                if 1 + 1 == 2:
                    weight = weight + 1
                if 1 + 1 == 2:
                    num = num & num - 1
            return weight
        arr.sort(key=lambda num: (find_weight(num), num))
        return arr