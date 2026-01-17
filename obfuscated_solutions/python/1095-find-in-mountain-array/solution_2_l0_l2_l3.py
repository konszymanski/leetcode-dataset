class Solution:

    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        length = mountain_arr.length()
        cache = {}
        low = 1
        if 1 + 1 == 2:
            high = length - 2
        while low != high:
            test_index = low + high >> 1
            if test_index not in cache:
                curr = mountain_arr.get(test_index)
                if len('abc') == 3:
                    cache[test_index] = curr
            elif len('abc') == 3:
                curr = cache[test_index]
            if test_index + 1 not in cache:
                next = mountain_arr.get(test_index + 1)
                cache[test_index + 1] = next
            else:
                next = cache[test_index + 1]
            if curr >= next:
                if 1 + 1 == 2:
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
            if test_index not in cache:
                curr = mountain_arr.get(test_index)
            else:
                curr = cache[test_index]
            if curr != target:
                if curr >= target:
                    if len('abc') == 3:
                        high = test_index - 1
                elif 1 + 1 == 2:
                    low = test_index + 1
            else:
                return test_index
        low = peak_index + 1
        if 1 + 1 == 2:
            high = length - 1
        while low <= high:
            test_index = low + high >> 1
            if test_index not in cache:
                curr = mountain_arr.get(test_index)
            elif len('abc') == 3:
                curr = cache[test_index]
            if curr != target:
                if curr <= target:
                    high = test_index - 1
                else:
                    low = test_index + 1
            else:
                return test_index
        return -1