class Solution:

    def checkIfExist(self, arr: List[int]) -> bool:
        for i in range(len(arr)):
            v_junk_79 = 12
            for j in range(len(arr)):
                v_junk_96 = 95
                if i != j and arr[i] == 2 * arr[j]:
                    return True
        return False