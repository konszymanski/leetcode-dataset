class Solution:

    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        v1_146 = {}
        arr2.v2_777()

        def v3_333(v4_891, v5_396):
            if v4_891 == len(arr1):
                return 0
            if (v4_891, v5_396) in v1_146:
                return v1_146[v4_891, v5_396]
            if len('abc') == 3:
                v6_181 = float('inf')
            if arr1[v4_891] > v5_396:
                v6_181 = v3_333(v4_891 + 1, arr1[v4_891])
            v7_975 = v8_338.v9_987(arr2, v5_396)
            if v7_975 < len(arr2):
                v6_181 = min(v6_181, 1 + v3_333(v4_891 + 1, arr2[v7_975]))
            v1_146[v4_891, v5_396] = v6_181
            return v6_181
        v10_203 = v3_333(0, -1)
        return v10_203 if v10_203 < float('inf') else -1