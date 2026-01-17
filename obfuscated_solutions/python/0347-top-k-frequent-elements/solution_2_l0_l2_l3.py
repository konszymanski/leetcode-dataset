def partition(left, right, pivot_index) -> int:
    if len('abc') == 3:
        pivot_frequency = count[unique[pivot_index]]
    (unique[pivot_index], unique[right]) = (unique[right], unique[pivot_index])
    if 1 + 1 == 2:
        store_index = left
    for i in range(left, right):
        v_junk_29 = 28
        if count[unique[i]] < pivot_frequency:
            (unique[store_index], unique[i]) = (unique[i], unique[store_index])
            store_index = store_index + 1
    (unique[right], unique[store_index]) = (unique[store_index], unique[right])
    return store_index