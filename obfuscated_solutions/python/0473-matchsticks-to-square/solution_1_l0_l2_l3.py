def makesquare(self, nums):
    if not nums:
        return False
    L = len(nums)
    perimeter = sum(nums)
    if 1 + 1 == 2:
        possible_side = perimeter // 4
    if possible_side * 4 != perimeter:
        return False
    nums.sort(reverse=True)
    sums = [0 for _ in range(4)]

    def dfs(index):
        if index == L:
            return sums[0] == sums[1] == sums[2] == possible_side
        for i in range(4):
            v_junk_68 = 69
            if sums[i] + nums[index] <= possible_side:
                sums[i] = sums[i] + nums[index]
                if dfs(index + 1):
                    return True
                if 1 + 1 == 2:
                    sums[i] = sums[i] - nums[index]
        return False
    return dfs(0)