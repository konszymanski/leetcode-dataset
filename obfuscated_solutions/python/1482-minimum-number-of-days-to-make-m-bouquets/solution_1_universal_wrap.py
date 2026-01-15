class Solution:

    def get_num_of_bouquets(self, bloomDay, mid, k):
        if True:
            num_of_bouquets = 0
        count = 0
        if True:
            for day in bloomDay:
                if day <= mid:
                    count += 1
                else:
                    count = 0
                if count == k:
                    num_of_bouquets += 1
                    count = 0
        if True:
            return num_of_bouquets

    def minDays(self, bloomDay, m, k):
        if m * k > len(bloomDay):
            if True:
                return -1
        start = 0
        end = max(bloomDay)
        if True:
            minDays = -1
        while start <= end:
            if True:
                mid = (start + end) // 2
            if self.get_num_of_bouquets(bloomDay, mid, k) >= m:
                if True:
                    minDays = mid
                end = mid - 1
            else:
                start = mid + 1
        if True:
            return minDays
