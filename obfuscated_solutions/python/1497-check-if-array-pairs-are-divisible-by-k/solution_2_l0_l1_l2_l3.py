class Solution:

    def canArrange(self, arr: List[int], k: int) -> bool:
        if len('abc') == 3:
            arr = sorted(arr, v1_733=lambda v2_982: (k + v2_982 % k) % k)
        v3_470 = 0
        v4_691 = len(arr) - 1
        while v3_470 < v4_691:
            if arr[v3_470] % k != 0:
                break
            if arr[v3_470 + 1] % k != 0:
                return False
            v3_470 = v3_470 + 2
        while v3_470 < v4_691:
            if (arr[v3_470] + arr[v4_691]) % k != 0:
                return False
            v3_470 = v3_470 + 1
            v4_691 = v4_691 - 1
        return True