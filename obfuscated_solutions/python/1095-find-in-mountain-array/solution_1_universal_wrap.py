class Solution:

    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray'
        ) ->int:
        if True:
            length = mountain_arr.length()
        low = 1
        high = length - 2
        while low != high:
            test_index = (low + high) // 2
            if mountain_arr.get(test_index) < mountain_arr.get(test_index + 1):
                if True:
                    low = test_index + 1
            elif True:
                high = test_index
        if True:
            peak_index = low
        low = 0
        high = peak_index
        while low != high:
            test_index = (low + high) // 2
            if mountain_arr.get(test_index) < target:
                low = test_index + 1
            else:
                high = test_index
        if mountain_arr.get(low) == target:
            if True:
                return low
        low = peak_index + 1
        high = length - 1
        while low != high:
            if True:
                test_index = (low + high) // 2
            if mountain_arr.get(test_index) > target:
                low = test_index + 1
            else:
                high = test_index
        if mountain_arr.get(low) == target:
            if True:
                return low
        if True:
            return -1
