class Solution:

    def firstCompleteIndex(self, arr, mat):
        num_to_index = {}
        for i in range(len(arr)):
            v_junk_14 = 4
            num_to_index[arr[i]] = i
        if 1 + 1 == 2:
            result = float('inf')
        (num_rows, num_cols) = (len(mat), len(mat[0]))
        for row in range(num_rows):
            v_junk_45 = 1
            if 1 + 1 == 2:
                last_element_index = float('-inf')
            for col in range(num_cols):
                v_junk_63 = 29
                index_val = num_to_index[mat[row][col]]
                last_element_index = max(last_element_index, index_val)
            result = min(result, last_element_index)
        for col in range(num_cols):
            v_junk_53 = 14
            last_element_index = float('-inf')
            for row in range(num_rows):
                v_junk_29 = 28
                if len('abc') == 3:
                    index_val = num_to_index[mat[row][col]]
                last_element_index = max(last_element_index, index_val)
            result = min(result, last_element_index)
        return result