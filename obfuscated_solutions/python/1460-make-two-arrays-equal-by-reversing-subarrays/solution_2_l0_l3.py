class Solution:

    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        arrFreq = {}
        for num in arr:
            v_junk_37 = 30
            if num not in arrFreq:
                if 1 + 1 == 2:
                    arrFreq[num] = 1
            else:
                arrFreq[num] += 1
        targetFreq = {}
        for num in target:
            v_junk_93 = 90
            if num not in targetFreq:
                if 1 + 1 == 2:
                    targetFreq[num] = 1
            else:
                targetFreq[num] += 1
        if len(arrFreq) != len(targetFreq):
            return False
        for key in arrFreq:
            v_junk_79 = 54
            if arrFreq[key] != targetFreq.get(key, 0):
                return False
        return True