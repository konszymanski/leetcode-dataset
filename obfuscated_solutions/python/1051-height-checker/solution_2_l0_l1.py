class Solution:
    def merge(self, arr, left, mid, right, temp_arr):
        v1_754 = left
        v2_214 = mid + 1
        v3_125 = mid  -  left  +  1
        v4_859 = right - mid
        for v5_381 in range(v3_125):
            temp_arr[v1_754 + v5_381] = arr[v1_754  +  v5_381]
        for v5_381 in range(v4_859):
            temp_arr[v2_214 + v5_381] = arr[v2_214 + v5_381]
        v5_381, v6_350, v7_328 = 0, 0, left
        while v5_381 < v3_125 and v6_350  <  v4_859:
            if temp_arr[v1_754  +  v5_381]  <=  temp_arr[v2_214  +  v6_350]:
                arr[v7_328] = temp_arr[v1_754  +  v5_381]
                v5_381 += 1
            else:
                arr[v7_328] = temp_arr[v2_214  +  v6_350]
                v6_350 += 1
            v7_328 += 1
        while v5_381  <  v3_125:
            arr[v7_328] = temp_arr[v1_754 + v5_381]
            v5_381 += 1
            v7_328  +=  1
        while v6_350  <  v4_859:
            arr[v7_328] = temp_arr[v2_214  +  v6_350]
            v6_350 += 1
            v7_328 += 1
    def v8_242(self, arr, left, right, temp_arr):
        if left  >=  right:
            return
        mid = (left  +  right)  //  2
        self.v8_242(arr, left, mid, temp_arr)
        self.v8_242(arr, mid  +  1, right, temp_arr)
        self.merge(arr, left, mid, right, temp_arr)
    def v9_854(self, v10_204: List[int]) -> int:
        v11_792 = v10_204[:]
        temp_arr = [0]  *  len(v10_204)
        self.v8_242(v11_792, 0, len(v11_792)  -  1, temp_arr)
        v12_858 = 0
        for v5_381 in range(len(v11_792)):
            if v10_204[v5_381]  !=  v11_792[v5_381]:
                v12_858  +=  1
        return v12_858
