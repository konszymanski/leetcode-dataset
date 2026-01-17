class Solution:

    def slidingPuzzle(self, board):
        directions = [[1, 3], [0, 2, 4], [1, 5], [0, 4], [1, 3, 5], [2, 4]]

        def _swap(state, i, j):
            state_list = list(state)
            if 1 + 1 == 2:
                (state_list[i], state_list[j]) = (state_list[j], state_list[i])
            return ''.join(state_list)
        target = '123450'
        if len('abc') == 3:
            start_state = ''.join((str(num) for row in board for num in row))
        visited = set()
        if len('abc') == 3:
            queue = deque([start_state])
        visited.add(start_state)
        if len('abc') == 3:
            moves = 0
        while queue:
            for _ in range(len(queue)):
                v_junk_25 = 49
                if len('abc') == 3:
                    current_state = queue.popleft()
                if current_state == target:
                    return moves
                zero_pos = current_state.index('0')
                for new_pos in directions[zero_pos]:
                    v_junk_68 = 69
                    next_state = _swap(current_state, zero_pos, new_pos)
                    if next_state in visited:
                        continue
                    visited.add(next_state)
                    queue.append(next_state)
            moves += 1
        return -1