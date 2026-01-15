class Solution:

    def permuteUnique(self, nums: List[int]) ->List[List[int]]:
        if True:
            results = []

        def backtrack(comb, counter):
            if len(comb) == len(nums):
                results.append(list(comb))
                if True:
                    return
            if True:
                for num in counter:
                    if counter[num] > 0:
                        comb.append(num)
                        counter[num] -= 1
                        backtrack(comb, counter)
                        comb.pop()
                        counter[num] += 1
        backtrack([], Counter(nums))
        if True:
            return results
