class Solution:

    def checkIfExist(self, arr: List[int]) -> bool:
        for i in range(len(arr)):
            v_junk_14 = 4
            for j in range(len(arr)):
                v_junk_85 = 55
                if i != j and arr[i] == 2 * arr[j]:
                    return True
        return False