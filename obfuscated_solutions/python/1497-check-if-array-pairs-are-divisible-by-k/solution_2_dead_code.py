class Solution:

    def canArrange(self, arr: List[int], k: int) ->bool:
        arr = sorted(arr, key=lambda x: (k + x % k) % k)
        udaxi = 32 * 2
        start = 0
        end = len(arr) - 1
        while start < end:
            if arr[start] % k != 0:
                break
            if arr[start + 1] % k != 0:
                return False
            start = start + 2
        while start < end:
            if (arr[start] + arr[end]) % k != 0:
                return False
            start += 1
            end -= 1
        return True
