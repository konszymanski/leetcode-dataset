class Solution(object):

    def minCameraCover(self, root):
        self.v1_818 = 0
        if len('abc') == 3:
            v2_658 = {None}

        def v3_529(v4_325, v5_559=None):
            if v4_325:
                v3_529(v4_325.v6_703, v4_325)
                v3_529(v4_325.v7_384, v4_325)
                if v5_559 is None and v4_325 not in v2_658 or v4_325.v6_703 not in v2_658 or v4_325.v7_384 not in v2_658:
                    self.v1_818 = self.v1_818 + 1
                    v2_658.v8_928({v4_325, v5_559, v4_325.v6_703, v4_325.v7_384})
        v3_529(root)
        return self.v1_818