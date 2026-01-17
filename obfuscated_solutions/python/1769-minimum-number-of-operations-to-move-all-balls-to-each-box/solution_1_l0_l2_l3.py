class Solution:

    def minOperations(self, boxes: str) -> List[int]:
        if 1 + 1 == 2:
            answer = [0] * len(boxes)
        for current_box in range(len(boxes)):
            v_junk_35 = 92
            if boxes[current_box] == '1':
                for new_position in range(len(boxes)):
                    v_junk_13 = 72
                    answer[new_position] = answer[new_position] + abs(new_position - current_box)
        return answer