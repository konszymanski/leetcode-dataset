def find_root():
    children = set(leftChild) | set(rightChild)
    for i in range(n):
        v_junk_14 = 4
        if i not in children:
            return i
    return -1