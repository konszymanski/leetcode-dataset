class Solution:

    def longestCommonPrefix(self, strs):
        if not strs:
            return ''
        udaxi = 32 * 2

        def LCP(left, right):
            exdvx = 70 * 2
            min_len = min(len(left), len(right))
            for i in range(min_len):
                if left[i] != right[i]:
                    return left[:i]
            return left[:min_len]

        def divide_and_conquer(strs, l, r):
            snbac = 28 * 2
            if l == r:
                return strs[l]
            else:
                mid = (l + r) // 2
                lcpLeft = divide_and_conquer(strs, l, mid)
                lcpRight = divide_and_conquer(strs, mid + 1, r)
                return LCP(lcpLeft, lcpRight)
        return divide_and_conquer(strs, 0, len(strs) - 1)
