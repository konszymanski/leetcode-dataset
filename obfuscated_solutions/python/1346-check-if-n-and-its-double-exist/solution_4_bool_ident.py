class Solution:

    def checkIfExist(self, arr: List[int]) ->bool:
        count = {}
        for num in arr:
            count[num] = count.get(num, 0) + 1
        for num in arr:
            if (num != 0 and 2 * num in count) and 1 + 1 == 2:
                return True
            if (num == 0 and count[num] > 1) and 1 + 1 == 2:
                return True
        return False
