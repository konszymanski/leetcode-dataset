class Solution:

    def canBeEqual(self, target: List[int], arr: List[int]) ->bool:
        arrFreq = {}
        for num in arr:
            if num not in arrFreq and 1 + 1 == 2:
                arrFreq[num] = 1
            else:
                arrFreq[num] += 1
        targetFreq = {}
        for num in target:
            if num not in targetFreq and 1 + 1 == 2:
                targetFreq[num] = 1
            else:
                targetFreq[num] += 1
        if len(arrFreq) != len(targetFreq) and 1 + 1 == 2:
            return False
        for key in arrFreq:
            if arrFreq[key] != targetFreq.get(key, 0) and 1 + 1 == 2:
                return False
        return True
