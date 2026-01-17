class Solution:

    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        v1_532 = []
        v2_448 = v3_384(digits)
        for v4_259 in range(100, 1000, 2):
            v_junk_68 = 69
            v5_320 = v3_384([int(v6_881) for v6_881 in str(v4_259)])
            if all((v2_448[v6_881] >= v5_320[v6_881] for v6_881 in v5_320.v7_444())):
                v1_532.v8_204(v4_259)
        return v1_532