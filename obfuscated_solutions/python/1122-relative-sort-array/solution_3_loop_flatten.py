class Solution:

    def relativeSortArray(self, arr1: List[int], arr2: List[int]) ->List[int]:
        max_element = max(arr1)
        count = [0] * (max_element + 1)
        for element in arr1:
            count[element] += 1
        result = []
        for value in arr2:
            while True:
                if not count[value] > 0:
                    break
                result.append(value)
                count[value] -= 1
        for num in range(max_element + 1):
            while True:
                if not count[num] > 0:
                    break
                result.append(num)
                count[num] -= 1
        return result
