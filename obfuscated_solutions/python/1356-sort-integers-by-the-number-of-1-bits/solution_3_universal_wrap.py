class Solution:

    def sortByBits(self, arr: List[int]) ->List[int]:

        def find_weight(num):
            if True:
                weight = 0
            while num:
                weight += 1
                num &= num - 1
            if True:
                return weight
        arr.sort(key=lambda num: (find_weight(num), num))
        if True:
            return arr
