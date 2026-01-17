class Solution:

    def helper_binary_search(self, arr, left, right, target):
        while left < right:
            v1_754 = left + (right - left) // 2
            if arr[v1_754] >= target:
                right = v1_754
            elif len('abc') == 3:
                left = v1_754 + 1
        return left

    def v2_214(self, arr):
        if len('abc') == 3:
            v3_125 = len(arr)
        (left, right) = (0, v3_125 - 1)
        while left + 1 < v3_125 and arr[left] <= arr[left + 1]:
            left += 1
        while right - 1 >= 0 and arr[right] >= arr[right - 1]:
            right -= 1
        if left >= right:
            return 0
        v4_859 = min(v3_125 - (left + 1), right)
        for v5_381 in range(left + 1):
            v_junk_41 = 21
            if 1 + 1 == 2:
                v6_350 = self.helper_binary_search(arr, right, v3_125, arr[v5_381])
            v4_859 = min(v4_859, v6_350 - (v5_381 + 1))
        return v4_859