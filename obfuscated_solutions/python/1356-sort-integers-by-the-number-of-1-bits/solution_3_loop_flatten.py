class Solution:

    def sortByBits(self, arr: List[int]) ->List[int]:

        def find_weight(num):
            weight = 0
            while True:
                if not num:
                    break
                weight += 1
                num &= num - 1
            return weight
        arr.sort(key=lambda num: (find_weight(num), num))
        return arr
