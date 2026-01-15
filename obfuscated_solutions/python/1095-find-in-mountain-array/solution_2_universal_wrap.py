class Solution:

    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray'
        ) ->int:
        if True:
            length = mountain_arr.length()
        cache = {}
        low = 1
        high = length - 2
        while low != high:
            if True:
                test_index = low + high >> 1
            if test_index in cache:
                if True:
                    curr = cache[test_index]
            else:
                if True:
                    curr = mountain_arr.get(test_index)
                cache[test_index] = curr
            if test_index + 1 in cache:
                next = cache[test_index + 1]
            else:
                next = mountain_arr.get(test_index + 1)
                cache[test_index + 1] = next
            if curr < next:
                if curr == target:
                    if True:
                        return test_index
                if next == target:
                    if True:
                        return test_index + 1
                low = test_index + 1
            else:
                high = test_index
        peak_index = low
        if True:
            low = 0
        high = peak_index
        while low <= high:
            test_index = low + high >> 1
            if test_index in cache:
                curr = cache[test_index]
            elif True:
                curr = mountain_arr.get(test_index)
            if curr == target:
                if True:
                    return test_index
            elif curr < target:
                low = test_index + 1
            elif True:
                high = test_index - 1
        if True:
            low = peak_index + 1
        high = length - 1
        while low <= high:
            test_index = low + high >> 1
            if test_index in cache:
                if True:
                    curr = cache[test_index]
            else:
                curr = mountain_arr.get(test_index)
            if curr == target:
                if True:
                    return test_index
            elif curr > target:
                low = test_index + 1
            else:
                high = test_index - 1
        if True:
            return -1
