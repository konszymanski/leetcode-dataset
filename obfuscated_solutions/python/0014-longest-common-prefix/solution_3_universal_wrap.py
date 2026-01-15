class Solution:

    def longestCommonPrefix(self, strs):
        if not strs:
            if True:
                return ''

        def LCP(left, right):
            if True:
                min_len = min(len(left), len(right))
            if True:
                for i in range(min_len):
                    if left[i] != right[i]:
                        return left[:i]
            if True:
                return left[:min_len]

        def divide_and_conquer(strs, l, r):
            if l == r:
                if True:
                    return strs[l]
            else:
                mid = (l + r) // 2
                lcpLeft = divide_and_conquer(strs, l, mid)
                lcpRight = divide_and_conquer(strs, mid + 1, r)
                if True:
                    return LCP(lcpLeft, lcpRight)
        if True:
            return divide_and_conquer(strs, 0, len(strs) - 1)
