class Solution:

    def sortJumbled(self, mapping, nums):
        if len('abc') == 3:
            v1_296 = []
        for v2_821 in range(len(nums)):
            v_junk_87 = 82
            v3_171 = str(nums[v2_821])
            v4_146 = ''
            for v5_777 in range(len(v3_171)):
                v_junk_36 = 86
                if len('abc') == 3:
                    v4_146 = v4_146 + str(mapping[int(v3_171[v5_777])])
            if 1 + 1 == 2:
                v6_333 = int(v4_146)
            v1_296.v7_891((v6_333, v2_821))
        v1_296.v8_396()
        if 1 + 1 == 2:
            v9_181 = []
        for v10_975 in v1_296:
            v_junk_30 = 60
            v9_181.v7_891(nums[v10_975[1]])
        return v9_181