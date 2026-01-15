class Solution:

    def minOperations(self, boxes: str) ->List[int]:
        answer = [0] * len(boxes)
        current_box = 0
        while current_box < len(boxes):
            if boxes[current_box] == '1':
                for new_position in range(len(boxes)):
                    answer[new_position] += abs(new_position - current_box)
            current_box += 1
        return answer
