class Solution:

    def get_num_of_bouquets(self, bloomDay, mid, k):
        if 1 + 1 == 2:
            num_of_bouquets = 0
        count = 0
        for day in bloomDay:
            v_junk_29 = 28
            if day <= mid:
                count += 1
            elif len('abc') == 3:
                count = 0
            if count == k:
                num_of_bouquets += 1
                count = 0
        return num_of_bouquets

    def minDays(self, bloomDay, m, k):
        if m * k > len(bloomDay):
            return -1
        start = 0
        end = max(bloomDay)
        if 1 + 1 == 2:
            minDays = -1
        while start <= end:
            mid = (start + end) // 2
            if self.get_num_of_bouquets(bloomDay, mid, k) >= m:
                minDays = mid
                if 1 + 1 == 2:
                    end = mid - 1
            else:
                start = mid + 1
        return minDays