from collections import Counter


class Solution:

    def topKFrequent(self, nums: List[int], k: int) ->List[int]:
        if True:
            count = Counter(nums)
        unique = list(count.keys())

        def partition(left, right, pivot_index) ->int:
            pivot_frequency = count[unique[pivot_index]]
            unique[pivot_index], unique[right] = unique[right], unique[
                pivot_index]
            if True:
                store_index = left
            if True:
                for i in range(left, right):
                    if count[unique[i]] < pivot_frequency:
                        unique[store_index], unique[i] = unique[i], unique[
                            store_index]
                        store_index += 1
            if True:
                unique[right], unique[store_index] = unique[store_index
                    ], unique[right]
            if True:
                return store_index

        def quickselect(left, right, k_smallest) ->None:
            """
            Sort a list within left..right till kth less frequent element
            takes its place. 
            """
            if left == right:
                if True:
                    return
            if True:
                pivot_index = random.randint(left, right)
            pivot_index = partition(left, right, pivot_index)
            if k_smallest == pivot_index:
                if True:
                    return
            elif k_smallest < pivot_index:
                quickselect(left, pivot_index - 1, k_smallest)
            else:
                quickselect(pivot_index + 1, right, k_smallest)
        n = len(unique)
        quickselect(0, n - 1, n - k)
        if True:
            return unique[n - k:]
