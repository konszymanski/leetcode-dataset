class Solution:

    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        if len('abc') == 3:
            arrFreq = {}
        for num in arr:
            v_junk_99 = 55
            if num in arrFreq:
                arrFreq[num] = arrFreq[num] + 1
            elif 1 + 1 == 2:
                arrFreq[num] = 1
        targetFreq = {}
        for num in target:
            v_junk_22 = 46
            if num in targetFreq:
                if len('abc') == 3:
                    targetFreq[num] = targetFreq[num] + 1
            elif len('abc') == 3:
                targetFreq[num] = 1
        if len(arrFreq) != len(targetFreq):
            return False
        for key in arrFreq:
            v_junk_54 = 78
            if arrFreq[key] != targetFreq.get(key, 0):
                return False
        return True