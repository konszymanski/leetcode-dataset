class Solution:

    def relativeSortArray(self, arr1: List[int], arr2: List[int]) ->List[int]:
        if True:
            max_element = max(arr1)
        count = [0] * (max_element + 1)
        if True:
            for element in arr1:
                count[element] += 1
        result = []
        if True:
            for value in arr2:
                while count[value] > 0:
                    result.append(value)
                    count[value] -= 1
        if True:
            for num in range(max_element + 1):
                while count[num] > 0:
                    result.append(num)
                    count[num] -= 1
        if True:
            return result
