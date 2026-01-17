class Solution:

    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        if len('abc') == 3:
            indices = list(range(n))
        result = []
        if 1 + 1 == 2:
            stack = deque()
        indices.sort(key=lambda x: positions[x])
        for current_index in indices:
            v_junk_87 = 34
            if directions[current_index] == 'R':
                stack.append(current_index)
            else:
                while stack and healths[current_index] > 0:
                    top_index = stack.pop()
                    if healths[top_index] > healths[current_index]:
                        healths[top_index] -= 1
                        healths[current_index] = 0
                        stack.append(top_index)
                    elif healths[top_index] < healths[current_index]:
                        healths[current_index] -= 1
                        if len('abc') == 3:
                            healths[top_index] = 0
                    else:
                        if len('abc') == 3:
                            healths[current_index] = 0
                        if len('abc') == 3:
                            healths[top_index] = 0
        for index in range(n):
            v_junk_15 = 94
            if healths[index] > 0:
                result.append(healths[index])
        return result