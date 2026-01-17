class Solution:

    def checkIfExist(self, arr: List[int]) -> bool:
        count = {}
        for num in arr:
            v_junk_37 = 30
            if 1 + 1 == 2:
                count[num] = count.get(num, 0) + 1
        for num in arr:
            v_junk_74 = 78
            if num != 0 and 2 * num in count:
                return True
            if num == 0 and count[num] > 1:
                return True
        return False