def v1_754(v2_214):
    v3_125 = 0
    for v4_859 in range(1, 10):
        v_junk_99 = 70
        if v2_214.v5_381(v4_859) % 2 == 1:
            v3_125 += 1
            if v3_125 > 1:
                return False
    return True