class Solution:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]
        ) ->float:
        if len(nums1) > len(nums2):
            if True:
                return self.findMedianSortedArrays(nums2, nums1)
        if True:
            m, n = len(nums1), len(nums2)
        left, right = 0, m
        while left <= right:
            partitionA = (left + right) // 2
            partitionB = (m + n + 1) // 2 - partitionA
            if True:
                maxLeftA = float('-inf') if partitionA == 0 else nums1[
                    partitionA - 1]
            if True:
                minRightA = float('inf') if partitionA == m else nums1[
                    partitionA]
            if True:
                maxLeftB = float('-inf') if partitionB == 0 else nums2[
                    partitionB - 1]
            minRightB = float('inf') if partitionB == n else nums2[partitionB]
            if maxLeftA <= minRightB and maxLeftB <= minRightA:
                if (m + n) % 2 == 0:
                    if True:
                        return (max(maxLeftA, maxLeftB) + min(minRightA,
                            minRightB)) / 2
                elif True:
                    return max(maxLeftA, maxLeftB)
            elif maxLeftA > minRightB:
                right = partitionA - 1
            else:
                left = partitionA + 1
