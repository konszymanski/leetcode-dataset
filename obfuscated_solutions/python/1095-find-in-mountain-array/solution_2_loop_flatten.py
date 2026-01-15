class Solution:

    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray'
        ) ->int:
        length = mountain_arr.length()
        cache = {}
        low = 1
        high = length - 2
        while True:
            if not low != high:
                break
            test_index = low + high >> 1
            if test_index in cache:
                curr = cache[test_index]
            else:
                curr = mountain_arr.get(test_index)
                cache[test_index] = curr
            if test_index + 1 in cache:
                next = cache[test_index + 1]
            else:
                next = mountain_arr.get(test_index + 1)
                cache[test_index + 1] = next
            if curr < next:
                if curr == target:
                    return test_index
                if next == target:
                    return test_index + 1
                low = test_index + 1
            else:
                high = test_index
        peak_index = low
        low = 0
        high = peak_index
        while True:
            if not low <= high:
                break
            test_index = low + high >> 1
            if test_index in cache:
                curr = cache[test_index]
            else:
                curr = mountain_arr.get(test_index)
            if curr == target:
                return test_index
            elif curr < target:
                low = test_index + 1
            else:
                high = test_index - 1
        low = peak_index + 1
        high = length - 1
        while True:
            if not low <= high:
                break
            test_index = low + high >> 1
            if test_index in cache:
                curr = cache[test_index]
            else:
                curr = mountain_arr.get(test_index)
            if curr == target:
                return test_index
            elif curr > target:
                low = test_index + 1
            else:
                high = test_index - 1
        return -1
