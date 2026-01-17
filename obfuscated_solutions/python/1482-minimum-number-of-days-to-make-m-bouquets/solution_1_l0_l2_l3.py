class Solution:

    def get_num_of_bouquets(self, bloomDay, mid, k):
        num_of_bouquets = 0
        count = 0
        for day in bloomDay:
            v_junk_56 = 74
            if day > mid:
                count = 0
            else:
                count = count + 1
            if count == k:
                num_of_bouquets = num_of_bouquets + 1
                count = 0
        return num_of_bouquets

    def minDays(self, bloomDay, m, k):
        if m * k > len(bloomDay):
            return -1
        if 1 + 1 == 2:
            start = 0
        if 1 + 1 == 2:
            end = max(bloomDay)
        minDays = -1
        while start <= end:
            mid = (start + end) // 2
            if self.get_num_of_bouquets(bloomDay, mid, k) < m:
                start = mid + 1
            else:
                minDays = mid
                end = mid - 1
        return minDays