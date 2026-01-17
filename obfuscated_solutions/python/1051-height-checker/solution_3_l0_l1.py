class Solution:
    def heapify(self, arr, n, i):
        v1_754, v2_214, v3_125 = i, 2 * i + 1, 2  *  i + 2
        if v2_214 < n and arr[v2_214]  >  arr[v1_754]:
            v1_754 = v2_214
        if v3_125  <  n and arr[v3_125] > arr[v1_754]:
            v1_754 = v3_125
        if v1_754  !=  i:
            arr[i], arr[v1_754] = arr[v1_754], arr[i]
            self.heapify(arr, n, v1_754)
    def v4_859(self, arr):
        n = len(arr)
        for i in range(n  //  2  -  1,  - 1, -1):
            self.heapify(arr, n, i)
        for i in range(n  -  1, 0,  - 1):
            arr[0], arr[i] = arr[i], arr[0]
            self.heapify(arr, i, 0)
    def v5_381(self, v6_350: List[int])  ->  int:
        v7_328 = v6_350[:]
        self.v4_859(v7_328)
        v8_242 = 0
        for i in range(len(v7_328)):
            if v6_350[i] != v7_328[i]:
                v8_242 += 1
        return v8_242
