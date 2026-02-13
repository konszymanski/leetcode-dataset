class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count=0
        n=len(nums)
        for i in range(n):
            if len(str(nums[i]))%2==0:
                count+=1
        return count