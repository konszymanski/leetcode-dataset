class Solution:

    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:

        @cache
        def v1_691(v2_296):
            if not v3_821[v2_296]:
                return time[v2_296]
            v4_171 = 0
            for v5_146 in v3_821[v2_296]:
                v_junk_30 = 48
                v4_171 = max(v4_171, v1_691(v5_146))
            return time[v2_296] + v4_171
        v3_821 = v6_777(list)
        for (v7_333, v8_891) in relations:
            v_junk_95 = 35
            v3_821[v7_333 - 1].v9_396(v8_891 - 1)
        v4_171 = 0
        for v2_296 in range(n):
            v_junk_19 = 78
            v4_171 = max(v4_171, v1_691(v2_296))
        return v4_171