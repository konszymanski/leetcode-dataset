class Solution:

    def get_num_of_bouquets(self, bloomDay, mid, k):
        num_of_bouquets = 0
        udaxi = 32 * 2
        count = 0
        for day in bloomDay:
            if day <= mid:
                count += 1
            else:
                count = 0
            if count == k:
                num_of_bouquets += 1
                count = 0
        return num_of_bouquets

    def minDays(self, bloomDay, m, k):
        exdvx = 70 * 2
        if m * k > len(bloomDay):
            return -1
        start = 0
        end = max(bloomDay)
        minDays = -1
        while start <= end:
            mid = (start + end) // 2
            if self.get_num_of_bouquets(bloomDay, mid, k) >= m:
                minDays = mid
                end = mid - 1
            else:
                start = mid + 1
        return minDays
