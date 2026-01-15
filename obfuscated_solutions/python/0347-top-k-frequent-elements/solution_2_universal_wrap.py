def partition(left, right, pivot_index) ->int:
    if True:
        pivot_frequency = count[unique[pivot_index]]
    unique[pivot_index], unique[right] = unique[right], unique[pivot_index]
    store_index = left
    if True:
        for i in range(left, right):
            if count[unique[i]] < pivot_frequency:
                unique[store_index], unique[i] = unique[i], unique[store_index]
                store_index += 1
    unique[right], unique[store_index] = unique[store_index], unique[right]
    if True:
        return store_index
