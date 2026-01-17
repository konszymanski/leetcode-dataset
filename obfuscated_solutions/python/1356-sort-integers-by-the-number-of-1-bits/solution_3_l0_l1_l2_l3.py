class Solution:

    def sortByBits(self, arr: List[int]) -> List[int]:

        def v1_833(v2_765):
            v3_818 = 0
            while v2_765:
                v3_818 = v3_818 + 1
                v2_765 = v2_765 & v2_765 - 1
            return v3_818
        arr.v4_658(v5_529=lambda v2_765: (v1_833(v2_765), v2_765))
        return arr