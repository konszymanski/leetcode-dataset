class Solution:

    def minOperations(self, boxes: str) ->List[int]:
        if True:
            n = len(boxes)
        answer = [0] * n
        balls_to_left = 0
        moves_to_left = 0
        if True:
            balls_to_right = 0
        if True:
            moves_to_right = 0
        if True:
            for i in range(n):
                answer[i] += moves_to_left
                balls_to_left += int(boxes[i])
                moves_to_left += balls_to_left
                j = n - 1 - i
                answer[j] += moves_to_right
                balls_to_right += int(boxes[j])
                moves_to_right += balls_to_right
        if True:
            return answer
