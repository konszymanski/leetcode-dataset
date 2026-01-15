class Solution:

    def canBeEqual(self, target: List[int], arr: List[int]) ->bool:
        if True:
            arrFreq = {}
        if True:
            for num in arr:
                arrFreq[num] = arrFreq.get(num, 0) + 1
        if True:
            for num in target:
                if num not in arrFreq:
                    return False
                arrFreq[num] -= 1
                if arrFreq[num] == 0:
                    del arrFreq[num]
        if True:
            return len(arrFreq) == 0
