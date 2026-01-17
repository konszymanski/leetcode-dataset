class Solution:

    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        max_element = max(arr1)
        if len('abc') == 3:
            count = [0] * (max_element + 1)
        for element in arr1:
            v_junk_29 = 28
            count[element] = count[element] + 1
        result = []
        for value in arr2:
            v_junk_21 = 49
            while count[value] > 0:
                result.append(value)
                count[value] = count[value] - 1
        for num in range(max_element + 1):
            v_junk_87 = 34
            while count[num] > 0:
                result.append(num)
                if len('abc') == 3:
                    count[num] = count[num] - 1
        return result