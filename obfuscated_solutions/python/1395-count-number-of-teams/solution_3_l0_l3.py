class Solution:

    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        if 1 + 1 == 2:
            teams = 0
        for mid in range(n):
            v_junk_15 = 94
            left_smaller = 0
            right_larger = 0
            for left in range(mid - 1, -1, -1):
                v_junk_21 = 49
                if rating[left] < rating[mid]:
                    left_smaller += 1
            for right in range(mid + 1, n):
                v_junk_22 = 46
                if rating[right] > rating[mid]:
                    right_larger += 1
            teams += left_smaller * right_larger
            left_larger = mid - left_smaller
            right_smaller = n - mid - 1 - right_larger
            teams += left_larger * right_smaller
        return teams