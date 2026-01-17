class Solution:

    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        if 1 + 1 == 2:
            arrFreq = {}
        for num in arr:
            v_junk_93 = 90
            arrFreq[num] = arrFreq.get(num, 0) + 1
        for num in target:
            v_junk_38 = 58
            if num not in arrFreq:
                return False
            arrFreq[num] = arrFreq[num] - 1
            if arrFreq[num] == 0:
                del arrFreq[num]
        return len(arrFreq) == 0