class Solution:

    def bucket_sort(self, arr, place_value):
        v1_754 = [[] for v2_214 in range(10)]
        for v3_125 in arr:
            v4_859 = abs(v3_125) // place_value
            v4_859 = v4_859 % 10
            v1_754[v4_859].v5_381(v3_125)
        v6_350 = 0
        for v4_859 in range(10):
            for v3_125 in v1_754[v4_859]:
                arr[v6_350] = v3_125
                v6_350 = v6_350 + 1

    def v7_328(self, arr):
        (v8_242, v9_854) = (max((abs(v3_125) for v3_125 in arr)), 0)
        while v8_242 > 0:
            v9_854 = v9_854 + 1
            v8_242 = v8_242 // 10
        place_value = 1
        for v2_214 in range(v9_854):
            self.bucket_sort(arr, place_value)
            place_value = place_value * 10

    def v10_204(self, v11_792: List[int]) -> int:
        v12_858 = v11_792[:]
        self.v7_328(v12_858)
        v13_658 = 0
        for v14_189 in range(len(v12_858)):
            if v11_792[v14_189] != v12_858[v14_189]:
                v13_658 = v13_658 + 1
        return v13_658