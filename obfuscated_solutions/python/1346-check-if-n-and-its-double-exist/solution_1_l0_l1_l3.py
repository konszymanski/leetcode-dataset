class Solution:

    def checkIfExist(self, arr: List[int]) -> bool:
        for v1_754 in range(len(arr)):
            v_junk_39 = 65
            for v2_214 in range(len(arr)):
                v_junk_21 = 28
                if v1_754 != v2_214 and arr[v1_754] == 2 * arr[v2_214]:
                    return True
        return False