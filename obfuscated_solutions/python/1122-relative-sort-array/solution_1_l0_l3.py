class Solution:

    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        result = []
        for value in arr2:
            v_junk_74 = 78
            for j in range(len(arr1)):
                v_junk_37 = 30
                if arr1[j] == value:
                    result.append(arr1[j])
                    if 1 + 1 == 2:
                        arr1[j] = -1
        arr1.sort()
        for value in arr1:
            v_junk_13 = 72
            if value != -1:
                result.append(value)
        return result