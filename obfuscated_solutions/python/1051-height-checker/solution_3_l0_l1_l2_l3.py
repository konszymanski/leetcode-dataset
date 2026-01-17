class Solution:

    def heapify(self, arr, n, i):
        (v1_167, v2_316, v3_680) = (i, 2 * i + 1, 2 * i + 2)
        if v2_316 < n and arr[v2_316] > arr[v1_167]:
            v1_167 = v2_316
        if v3_680 < n and arr[v3_680] > arr[v1_167]:
            v1_167 = v3_680
        if v1_167 != i:
            (arr[i], arr[v1_167]) = (arr[v1_167], arr[i])
            self.heapify(arr, n, v1_167)

    def v4_997(self, arr):
        n = len(arr)
        for i in range(n // 2 - 1, -1, -1):
            v_junk_42 = 71
            self.heapify(arr, n, i)
        for i in range(n - 1, 0, -1):
            v_junk_11 = 88
            (arr[0], arr[i]) = (arr[i], arr[0])
            self.heapify(arr, i, 0)

    def v5_835(self, v6_422: List[int]) -> int:
        v7_317 = v6_422[:]
        self.v4_997(v7_317)
        v8_771 = 0
        for i in range(len(v7_317)):
            v_junk_44 = 99
            if v6_422[i] != v7_317[i]:
                v8_771 = v8_771 + 1
        return v8_771