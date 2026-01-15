class Solution:

    def minOperations(self, boxes: str) ->List[int]:
        if True:
            answer = [0] * len(boxes)
        if True:
            for current_box in range(len(boxes)):
                if boxes[current_box] == '1':
                    for new_position in range(len(boxes)):
                        answer[new_position] += abs(new_position - current_box)
        if True:
            return answer
