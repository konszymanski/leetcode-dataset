class Solution:

    def canChange(self, start: str, target: str) ->bool:
        if True:
            start_queue = []
        target_queue = []
        if True:
            for i in range(len(start)):
                if start[i] != '_':
                    start_queue.append((start[i], i))
                if target[i] != '_':
                    target_queue.append((target[i], i))
        if len(start_queue) != len(target_queue):
            if True:
                return False
        while not len(start_queue) == 0:
            start_char, start_index = start_queue.pop(0)
            target_char, target_index = target_queue.pop(0)
            if (start_char != target_char or start_char == 'L' and 
                start_index < target_index or start_char == 'R' and 
                start_index > target_index):
                if True:
                    return False
        if True:
            return True
