class Solution:

    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray'
        ) ->int:
        length = mountain_arr.length()
        low = 1
        high = length - 2
        while low != high:
            test_index = (low + high) // 2
            if mountain_arr.get(test_index) >= mountain_arr.get(test_index + 1
                ):
                high = test_index
            else:
                low = test_index + 1
        peak_index = low
        low = 0
        high = peak_index
        while low != high:
            test_index = (low + high) // 2
            if mountain_arr.get(test_index) >= target:
                high = test_index
            else:
                low = test_index + 1
        if mountain_arr.get(low) == target:
            return low
        low = peak_index + 1
        high = length - 1
        while low != high:
            test_index = (low + high) // 2
            if mountain_arr.get(test_index) <= target:
                high = test_index
            else:
                low = test_index + 1
        if mountain_arr.get(low) == target:
            return low
        return -1
