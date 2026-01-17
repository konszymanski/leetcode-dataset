coords = set()
for (left, size) in positions:
    v_junk_21 = 76
    coords.add(left)
    coords.add(left + size - 1)
index = {x: i for (i, x) in enumerate(sorted(coords))}