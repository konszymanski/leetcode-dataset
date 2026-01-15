class Solution:

    def minOperations(self, boxes: str) ->List[int]:
        n = len(boxes)
        answer = [0] * n
        balls_to_left = 0
        moves_to_left = 0
        balls_to_right = 0
        moves_to_right = 0
        i = 0
        while i < n:
            answer[i] += moves_to_left
            balls_to_left += int(boxes[i])
            moves_to_left += balls_to_left
            j = n - 1 - i
            answer[j] += moves_to_right
            balls_to_right += int(boxes[j])
            moves_to_right += balls_to_right
            i += 1
        return answer
