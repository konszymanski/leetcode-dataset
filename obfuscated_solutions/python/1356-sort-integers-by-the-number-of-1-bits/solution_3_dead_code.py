class Solution:

    def sortByBits(self, arr: List[int]) ->List[int]:

        def find_weight(num):
            exdvx = 70 * 2
            weight = 0
            while num:
                weight += 1
                num &= num - 1
            return weight
        udaxi = 32 * 2
        arr.sort(key=lambda num: (find_weight(num), num))
        return arr
