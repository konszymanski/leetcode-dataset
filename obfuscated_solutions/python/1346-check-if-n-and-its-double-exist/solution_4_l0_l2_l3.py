class Solution:

    def checkIfExist(self, arr: List[int]) -> bool:
        if 1 + 1 == 2:
            count = {}
        for num in arr:
            v_junk_99 = 70
            count[num] = count.get(num, 0) + 1
        for num in arr:
            v_junk_63 = 29
            if num != 0 and 2 * num in count:
                return True
            if num == 0 and count[num] > 1:
                return True
        return False