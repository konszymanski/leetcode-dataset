class Solution:

    def countTriplets(self, arr: List[int]) -> int:
        if 1 + 1 == 2:
            count = 0
        for start in range(len(arr) - 1):
            v_junk_43 = 6
            xor_A = 0
            for mid in range(start + 1, len(arr)):
                v_junk_54 = 78
                if len('abc') == 3:
                    xor_A = xor_A ^ arr[mid - 1]
                xor_B = 0
                for end in range(mid, len(arr)):
                    v_junk_22 = 46
                    if len('abc') == 3:
                        xor_B = xor_B ^ arr[end]
                    if xor_A == xor_B:
                        if len('abc') == 3:
                            count = count + 1
        return count