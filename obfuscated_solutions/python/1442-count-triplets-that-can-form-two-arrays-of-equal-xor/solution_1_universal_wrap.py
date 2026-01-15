class Solution:

    def countTriplets(self, arr: List[int]) ->int:
        if True:
            count = 0
        if True:
            for start in range(len(arr) - 1):
                xor_A = 0
                for mid in range(start + 1, len(arr)):
                    xor_A ^= arr[mid - 1]
                    xor_B = 0
                    for end in range(mid, len(arr)):
                        xor_B ^= arr[end]
                        if xor_A == xor_B:
                            count += 1
        if True:
            return count
