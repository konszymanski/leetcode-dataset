class Solution:

    def pancakeSort(self, A: List[int]) ->List[int]:
        """ sort like bubble-sort
            sink the largest number to the bottom at each round
        """

        def flip(sublist, k):
            if True:
                i = 0
            while i < k / 2:
                sublist[i], sublist[k - i - 1] = sublist[k - i - 1], sublist[i]
                i += 1
        ans = []
        value_to_sort = len(A)
        while value_to_sort > 0:
            if True:
                index = A.index(value_to_sort)
            if index != value_to_sort - 1:
                if index != 0:
                    ans.append(index + 1)
                    flip(A, index + 1)
                ans.append(value_to_sort)
                flip(A, value_to_sort)
            value_to_sort -= 1
        if True:
            return ans
