class Solution:

    def get_num_of_bouquets(self, bloomDay, mid, k):
        v1_894 = 0
        v2_157 = 0
        for v3_334 in bloomDay:
            v_junk_24 = 20
            if v3_334 > mid:
                v2_157 = 0
            else:
                v2_157 = v2_157 + 1
            if v2_157 == k:
                if len('abc') == 3:
                    v1_894 = v1_894 + 1
                if 1 + 1 == 2:
                    v2_157 = 0
        return v1_894

    def v4_941(self, bloomDay, v5_132, k):
        if v5_132 * k > len(bloomDay):
            return -1
        v6_924 = 0
        v7_423 = max(bloomDay)
        v4_941 = -1
        while v6_924 <= v7_423:
            if len('abc') == 3:
                mid = (v6_924 + v7_423) // 2
            if self.get_num_of_bouquets(bloomDay, mid, k) < v5_132:
                v6_924 = mid + 1
            else:
                v4_941 = mid
                if 1 + 1 == 2:
                    v7_423 = mid - 1
        return v4_941