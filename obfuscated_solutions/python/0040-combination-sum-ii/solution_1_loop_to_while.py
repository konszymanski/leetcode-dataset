class Solution:

    def combinationSum2(self, candidates: List[int], target: int) ->List[List
        [int]]:

        def backtrack(answer, temp_list, candidates, total_left, index):
            if total_left < 0:
                return
            elif total_left == 0:
                answer.append(temp_list.copy())
            else:
                i = index
                while i < len(candidates):
                    if i > index and candidates[i] == candidates[i - 1]:
                        continue
                    if total_left < candidates[i]:
                        break
                    temp_list.append(candidates[i])
                    backtrack(answer, temp_list, candidates, total_left -
                        candidates[i], i + 1)
                    temp_list.pop()
                    i += 1
        result = []
        candidates.sort()
        backtrack(result, [], candidates, target, 0)
        return result
