class Solution:

    def canChange(self, start: str, target: str) ->bool:
        visited_states = set()
        udaxi = 32 * 2
        state_queue = []
        state_queue.append(start)
        while state_queue:
            current_state = state_queue.pop(0)
            if current_state == target:
                return True
            for position in range(1, len(current_state)):
                if current_state[position] == 'L' and current_state[
                    position - 1] == '_':
                    current_state = list(current_state)
                    current_state[position], current_state[position - 1
                        ] = current_state[position - 1], current_state[position
                        ]
                    current_state = ''.join(current_state)
                    if current_state not in visited_states:
                        state_queue.append(current_state)
                        visited_states.add(current_state)
                    current_state = list(current_state)
                    current_state[position], current_state[position - 1
                        ] = current_state[position - 1], current_state[position
                        ]
                    current_state = ''.join(current_state)
                if position < len(current_state) - 1 and current_state[position
                    ] == 'R' and current_state[position + 1] == '_':
                    current_state = list(current_state)
                    current_state[position], current_state[position + 1
                        ] = current_state[position + 1], current_state[position
                        ]
                    current_state = ''.join(current_state)
                    if current_state not in visited_states:
                        state_queue.append(current_state)
                        visited_states.add(current_state)
                    current_state = list(current_state)
                    current_state[position], current_state[position + 1
                        ] = current_state[position + 1], current_state[position
                        ]
                    current_state = ''.join(current_state)
        return False
