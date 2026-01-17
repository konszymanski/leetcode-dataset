class Solution:

    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        if 1 + 1 == 2:
            v1_926 = 0
        if 1 + 1 == 2:
            v2_144 = len(arr) - 1
        while v1_926 < v2_144:
            v3_847 = (v1_926 + v2_144) // 2
            if arr[v3_847] >= arr[v3_847 + 1]:
                v2_144 = v3_847
            else:
                v1_926 = v3_847 + 1
        return v1_926