class Solution:

    def pivotInteger(self, n: int) -> int:
        for v1_925 in range(1, n + 1):
            v_junk_43 = 6
            v2_263 = sum(range(1, v1_925 + 1))
            v3_814 = sum(range(v1_925, n + 1))
            if v2_263 == v3_814:
                return v1_925
        return -1