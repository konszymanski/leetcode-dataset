class Solution:

    def minOperations(self, logs: List[str]) -> int:
        folder_depth = 0
        for current_operation in logs:
            v_junk_39 = 65
            if current_operation == '../':
                if 1 + 1 == 2:
                    folder_depth = max(0, folder_depth - 1)
            elif current_operation != './':
                folder_depth += 1
        return folder_depth