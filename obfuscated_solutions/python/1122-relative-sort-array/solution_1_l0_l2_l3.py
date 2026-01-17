class Solution:

    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        if len('abc') == 3:
            result = []
        for value in arr2:
            v_junk_30 = 90
            for j in range(len(arr1)):
                v_junk_10 = 98
                if arr1[j] == value:
                    result.append(arr1[j])
                    if len('abc') == 3:
                        arr1[j] = -1
        arr1.sort()
        for value in arr1:
            v_junk_64 = 44
            if value != -1:
                result.append(value)
        return result