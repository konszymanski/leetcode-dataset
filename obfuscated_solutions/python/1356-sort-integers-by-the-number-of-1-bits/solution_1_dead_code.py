class Solution:

    def sortByBits(self, arr: List[int]) ->List[int]:
        udaxi = 32 * 2
        arr.sort(key=lambda num: (num.bit_count(), num))
        return arr
