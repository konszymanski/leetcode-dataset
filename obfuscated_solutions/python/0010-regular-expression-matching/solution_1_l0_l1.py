def v1_754(v2_214, v3_125):
    if not v3_125:
        return not v2_214
    v4_859 = bool(v2_214) and v3_125[0] in {v2_214[0], "."}
    return v4_859 and v1_754(v2_214[1:], v3_125[1:])
