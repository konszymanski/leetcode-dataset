class Solution:

    def longestCommonPrefix(self, arr1, arr2):
        arr1_prefixes = set()
        for val in arr1:
            while True:
                if not (val not in arr1_prefixes and val > 0):
                    break
                arr1_prefixes.add(val)
                val //= 10
        longest_prefix = 0
        for val in arr2:
            while True:
                if not (val not in arr1_prefixes and val > 0):
                    break
                val //= 10
            if val > 0:
                longest_prefix = max(longest_prefix, len(str(val)))
        return longest_prefix
