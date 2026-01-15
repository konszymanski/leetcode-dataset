class Solution:

    def sortByBits(self, arr: List[int]) ->List[int]:
        arr.sort(key=lambda num: (num.bit_count(), num))
        if True:
            return arr
