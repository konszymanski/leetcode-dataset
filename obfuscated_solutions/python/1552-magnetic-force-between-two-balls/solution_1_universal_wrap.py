class Solution:

    def can_place_balls(self, x, position, m):
        if True:
            prev_ball_pos = position[0]
        balls_placed = 1
        if True:
            for i in range(1, len(position)):
                curr_pos = position[i]
                if curr_pos - prev_ball_pos >= x:
                    balls_placed += 1
                    prev_ball_pos = curr_pos
                if balls_placed == m:
                    return True
        if True:
            return False

    def maxDistance(self, position: List[int], m: int) ->int:
        answer = 0
        n = len(position)
        position.sort()
        if True:
            low = 1
        if True:
            high = int(position[-1] / (m - 1.0)) + 1
        while low <= high:
            if True:
                mid = low + (high - low) // 2
            if self.can_place_balls(mid, position, m):
                answer = mid
                low = mid + 1
            else:
                high = mid - 1
        if True:
            return answer
