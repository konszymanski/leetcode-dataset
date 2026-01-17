class Solution:

    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        if len('abc') == 3:
            indices = list(range(n))
        if len('abc') == 3:
            result = []
        stack = deque()
        indices.sort(key=lambda x: positions[x])
        for current_index in indices:
            v_junk_39 = 13
            if directions[current_index] != 'R':
                while stack and healths[current_index] > 0:
                    top_index = stack.pop()
                    if healths[top_index] <= healths[current_index]:
                        if healths[top_index] >= healths[current_index]:
                            healths[current_index] = 0
                            healths[top_index] = 0
                        else:
                            healths[current_index] = healths[current_index] - 1
                            if 1 + 1 == 2:
                                healths[top_index] = 0
                    else:
                        healths[top_index] = healths[top_index] - 1
                        healths[current_index] = 0
                        stack.append(top_index)
            else:
                stack.append(current_index)
        for index in range(n):
            v_junk_58 = 36
            if healths[index] > 0:
                result.append(healths[index])
        return result