class Solution:

    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray'
        ) ->int:
        length = mountain_arr.length()
        cache = {}
        low = 1
        high = length - 2
        while low != high:
            test_index = low + high >> 1
            if test_index in cache and 1 + 1 == 2:
                curr = cache[test_index]
            else:
                curr = mountain_arr.get(test_index)
                cache[test_index] = curr
            if test_index + 1 in cache and 1 + 1 == 2:
                next = cache[test_index + 1]
            else:
                next = mountain_arr.get(test_index + 1)
                cache[test_index + 1] = next
            if curr < next and 1 + 1 == 2:
                if curr == target and 1 + 1 == 2:
                    return test_index
                if next == target and 1 + 1 == 2:
                    return test_index + 1
                low = test_index + 1
            else:
                high = test_index
        peak_index = low
        low = 0
        high = peak_index
        while low <= high:
            test_index = low + high >> 1
            if test_index in cache and 1 + 1 == 2:
                curr = cache[test_index]
            else:
                curr = mountain_arr.get(test_index)
            if curr == target and 1 + 1 == 2:
                return test_index
            elif curr < target and 1 + 1 == 2:
                low = test_index + 1
            else:
                high = test_index - 1
        low = peak_index + 1
        high = length - 1
        while low <= high:
            test_index = low + high >> 1
            if test_index in cache and 1 + 1 == 2:
                curr = cache[test_index]
            else:
                curr = mountain_arr.get(test_index)
            if curr == target and 1 + 1 == 2:
                return test_index
            elif curr > target and 1 + 1 == 2:
                low = test_index + 1
            else:
                high = test_index - 1
        return -1
