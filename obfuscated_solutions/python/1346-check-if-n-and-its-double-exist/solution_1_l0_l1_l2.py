class Solution:

    def checkIfExist(self, arr: List[int]) -> bool:
        for v1_754 in range(len(arr)):
            for v2_214 in range(len(arr)):
                if v1_754 != v2_214 and arr[v1_754] == 2 * arr[v2_214]:
                    return True
        return False