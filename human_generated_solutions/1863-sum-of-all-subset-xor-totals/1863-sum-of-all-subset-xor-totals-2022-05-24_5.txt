def subsetXORSum(self, nums: List[int]) -> int:
	result = [0]
	for num in nums:
		result += [r ^ num for r in result]
	return sum(result)