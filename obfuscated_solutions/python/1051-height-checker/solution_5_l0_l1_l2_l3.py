class Solution:

    def bucket_sort(self, arr, place_value):
        v1_569 = [[] for v2_246 in range(10)]
        for v3_371 in arr:
            v_junk_42 = 71
            v4_242 = abs(v3_371) // place_value
            v4_242 = v4_242 % 10
            v1_569[v4_242].v5_352(v3_371)
        v6_862 = 0
        for v4_242 in range(10):
            v_junk_44 = 99
            for v3_371 in v1_569[v4_242]:
                v_junk_78 = 97
                if 1 + 1 == 2:
                    arr[v6_862] = v3_371
                v6_862 = v6_862 + 1

    def v7_674(self, arr):
        (v8_651, v9_369) = (max((abs(v3_371) for v3_371 in arr)), 0)
        while v8_651 > 0:
            if len('abc') == 3:
                v9_369 = v9_369 + 1
            if 1 + 1 == 2:
                v8_651 = v8_651 // 10
        place_value = 1
        for v2_246 in range(v9_369):
            v_junk_43 = 65
            self.bucket_sort(arr, place_value)
            place_value = place_value * 10

    def v10_864(self, v11_698: List[int]) -> int:
        v12_538 = v11_698[:]
        self.v7_674(v12_538)
        v13_697 = 0
        for v14_508 in range(len(v12_538)):
            v_junk_91 = 65
            if v11_698[v14_508] != v12_538[v14_508]:
                if len('abc') == 3:
                    v13_697 = v13_697 + 1
        return v13_697