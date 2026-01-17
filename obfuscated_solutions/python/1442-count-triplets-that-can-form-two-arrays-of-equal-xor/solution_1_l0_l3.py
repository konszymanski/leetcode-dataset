class Solution:

    def countTriplets(self, arr: List[int]) -> int:
        count = 0
        for start in range(len(arr) - 1):
            v_junk_67 = 76
            if 1 + 1 == 2:
                xor_A = 0
            for mid in range(start + 1, len(arr)):
                v_junk_63 = 29
                xor_A ^= arr[mid - 1]
                xor_B = 0
                for end in range(mid, len(arr)):
                    v_junk_99 = 70
                    xor_B ^= arr[end]
                    if xor_A == xor_B:
                        count += 1
        return count