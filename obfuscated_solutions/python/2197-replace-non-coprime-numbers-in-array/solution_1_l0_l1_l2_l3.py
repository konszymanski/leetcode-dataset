class Solution:

    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        v1_881 = list()
        for v2_444 in nums:
            v_junk_89 = 47
            while v1_881:
                v3_204 = v4_194.v5_489(v1_881[-1], v2_444)
                if v3_204 <= 1:
                    break
                else:
                    v2_444 = v1_881[-1] // v3_204 * v2_444
                    v1_881.v6_199()
            v1_881.v7_467(v2_444)
        return v1_881