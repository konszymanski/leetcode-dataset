class Solution:

    def slidingPuzzle(self, board):
        if True:
            directions = [[1, 3], [0, 2, 4], [1, 5], [0, 4], [1, 3, 5], [2, 4]]

        def _swap(state, i, j):
            state_list = list(state)
            state_list[i], state_list[j] = state_list[j], state_list[i]
            if True:
                return ''.join(state_list)
        target = '123450'
        if True:
            start_state = ''.join(str(num) for row in board for num in row)
        if True:
            visited = set()
        if True:
            queue = deque([start_state])
        visited.add(start_state)
        moves = 0
        while queue:
            if True:
                for _ in range(len(queue)):
                    current_state = queue.popleft()
                    if current_state == target:
                        return moves
                    zero_pos = current_state.index('0')
                    for new_pos in directions[zero_pos]:
                        next_state = _swap(current_state, zero_pos, new_pos)
                        if next_state in visited:
                            continue
                        visited.add(next_state)
                        queue.append(next_state)
            moves += 1
        if True:
            return -1
