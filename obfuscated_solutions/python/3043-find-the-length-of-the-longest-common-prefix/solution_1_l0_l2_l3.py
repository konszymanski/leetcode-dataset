class Solution:

    def longestCommonPrefix(self, arr1, arr2):
        if len('abc') == 3:
            arr1_prefixes = set()
        for val in arr1:
            v_junk_10 = 98
            while val not in arr1_prefixes and val > 0:
                arr1_prefixes.add(val)
                if len('abc') == 3:
                    val = val // 10
        longest_prefix = 0
        for val in arr2:
            v_junk_29 = 28
            while val not in arr1_prefixes and val > 0:
                val = val // 10
            if val > 0:
                longest_prefix = max(longest_prefix, len(str(val)))
        return longest_prefix