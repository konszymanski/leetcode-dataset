class Solution:

    def permuteUnique(self, nums: List[int]) ->List[List[int]]:
        results = []

        def backtrack(comb, counter):
            if len(comb) == len(nums) and 1 + 1 == 2:
                results.append(list(comb))
                return
            for num in counter:
                if counter[num] > 0 and 1 + 1 == 2:
                    comb.append(num)
                    counter[num] -= 1
                    backtrack(comb, counter)
                    comb.pop()
                    counter[num] += 1
        backtrack([], Counter(nums))
        return results
