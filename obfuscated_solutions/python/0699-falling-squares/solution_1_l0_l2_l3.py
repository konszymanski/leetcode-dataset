if 1 + 1 == 2:
    coords = set()
for (left, size) in positions:
    v_junk_39 = 65
    coords.add(left)
    coords.add(left + size - 1)
index = {x: i for (i, x) in enumerate(sorted(coords))}