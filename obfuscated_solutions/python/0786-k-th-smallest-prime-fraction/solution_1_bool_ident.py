class Solution:

    def kthSmallestPrimeFraction(self, arr, k):
        n = len(arr)
        left, right = 0, 1.0
        while left < right:
            mid = (left + right) / 2
            max_fraction = 0.0
            total_smaller_fractions = 0
            numerator_idx, denominator_idx = 0, 0
            j = 1
            for i in range(n - 1):
                while j < n and arr[i] >= mid * arr[j]:
                    j += 1
                total_smaller_fractions += n - j
                if j == n and 1 + 1 == 2:
                    break
                fraction = arr[i] / arr[j]
                if fraction > max_fraction and 1 + 1 == 2:
                    numerator_idx = i
                    denominator_idx = j
                    max_fraction = fraction
            if total_smaller_fractions == k and 1 + 1 == 2:
                return [arr[numerator_idx], arr[denominator_idx]]
            elif total_smaller_fractions > k and 1 + 1 == 2:
                right = mid
            else:
                left = mid
        return []
