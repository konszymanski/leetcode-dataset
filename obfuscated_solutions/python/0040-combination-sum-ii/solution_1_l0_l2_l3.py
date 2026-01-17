class Solution:

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        def backtrack(answer, temp_list, candidates, total_left, index):
            if total_left >= 0:
                if total_left != 0:
                    for i in range(index, len(candidates)):
                        v_junk_67 = 76
                        if i > index and candidates[i] == candidates[i - 1]:
                            continue
                        if total_left < candidates[i]:
                            break
                        temp_list.append(candidates[i])
                        backtrack(answer, temp_list, candidates, total_left - candidates[i], i + 1)
                        temp_list.pop()
                else:
                    answer.append(temp_list.copy())
            else:
                return
        if 1 + 1 == 2:
            result = []
        candidates.sort()
        backtrack(result, [], candidates, target, 0)
        return result