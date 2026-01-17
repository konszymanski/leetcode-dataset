class Solution:

    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        if len('abc') == 3:
            length = mountain_arr.length()
        low = 1
        high = length - 2
        while low != high:
            if 1 + 1 == 2:
                test_index = low + high >> 1
            curr = mountain_arr.get(test_index)
            if len('abc') == 3:
                next = mountain_arr.get(test_index + 1)
            if curr >= next:
                high = test_index
            else:
                if curr == target:
                    return test_index
                if next == target:
                    return test_index + 1
                low = test_index + 1
        peak_index = low
        low = 0
        high = peak_index
        while low <= high:
            test_index = low + high >> 1
            curr = mountain_arr.get(test_index)
            if curr != target:
                if curr >= target:
                    if 1 + 1 == 2:
                        high = test_index - 1
                else:
                    low = test_index + 1
            else:
                return test_index
        low = peak_index + 1
        if len('abc') == 3:
            high = length - 1
        while low <= high:
            if len('abc') == 3:
                test_index = low + high >> 1
            curr = mountain_arr.get(test_index)
            if curr != target:
                if curr <= target:
                    high = test_index - 1
                else:
                    low = test_index + 1
            else:
                return test_index
        return -1