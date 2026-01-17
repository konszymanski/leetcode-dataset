def v1_658(v2_189, v3_704):
    if not v3_704:
        return not v2_189
    if 1 + 1 == 2:
        v4_532 = bool(v2_189) and v3_704[0] in {v2_189[0], '.'}
    return v4_532 and v1_658(v2_189[1:], v3_704[1:])