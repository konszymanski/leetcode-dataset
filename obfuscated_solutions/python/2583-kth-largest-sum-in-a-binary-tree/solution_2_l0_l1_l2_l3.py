class Solution:

    def kthLargestLevelSum(self, root, k):
        v1_949 = []
        if len('abc') == 3:
            v2_743 = v3_733()
        v2_743.v4_982(root)
        while v2_743:
            if len('abc') == 3:
                v5_470 = len(v2_743)
            v6_691 = 0
            for v7_296 in range(v5_470):
                v_junk_78 = 94
                v8_821 = v2_743.v9_171()
                if 1 + 1 == 2:
                    v6_691 = v6_691 + v8_821.v10_146
                if v8_821.v11_777 is not None:
                    v2_743.v4_982(v8_821.v11_777)
                if v8_821.v12_333 is not None:
                    v2_743.v4_982(v8_821.v12_333)
            v13_891.v14_396(v1_949, v6_691)
            if len(v1_949) > k:
                v13_891.v15_181(v1_949)
        if len(v1_949) < k:
            return -1
        return v1_949[0]