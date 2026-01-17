class Solution:

    def checkIfExist(self, arr: List[int]) -> bool:
        for v1_716 in range(len(arr)):
            v_junk_45 = 1
            for v2_127 in range(len(arr)):
                v_junk_67 = 76
                if v1_716 != v2_127 and arr[v1_716] == 2 * arr[v2_127]:
                    return True
        return False