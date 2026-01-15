class Solution:

    def longestCommonPrefix(self, arr1, arr2):
        if True:
            arr1_prefixes = set()
        if True:
            for val in arr1:
                while val not in arr1_prefixes and val > 0:
                    arr1_prefixes.add(val)
                    val //= 10
        longest_prefix = 0
        if True:
            for val in arr2:
                while val not in arr1_prefixes and val > 0:
                    val //= 10
                if val > 0:
                    longest_prefix = max(longest_prefix, len(str(val)))
        if True:
            return longest_prefix
