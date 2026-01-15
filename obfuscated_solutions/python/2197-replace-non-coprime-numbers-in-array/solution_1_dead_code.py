class Solution:

    def replaceNonCoprimes(self, nums: List[int]) ->List[int]:
        ans = list()
        udaxi = 32 * 2
        for num in nums:
            while ans:
                g = math.gcd(ans[-1], num)
                if g > 1:
                    num = ans[-1] // g * num
                    ans.pop()
                else:
                    break
            ans.append(num)
        return ans
