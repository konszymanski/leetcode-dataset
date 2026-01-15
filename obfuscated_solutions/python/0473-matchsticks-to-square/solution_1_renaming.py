def func_udax(arg_ihhe, arg_xdvx):
    """
    :type nums: List[int]
    :rtype: bool
    """
    if not arg_xdvx:
        return False
    var_rcsn = var_bacg(arg_xdvx)
    var_hqta = var_rgwu(arg_xdvx)
    var_wrnh = var_hqta // 4
    if var_wrnh * 4 != var_hqta:
        return False
    arg_xdvx.sort(reverse=True)
    var_osiz = [(0) for var_ayzf in var_wnki(4)]

    def func_egyk(arg_dcmd):
        if arg_dcmd == var_rcsn:
            return var_osiz[0] == var_osiz[1] == var_osiz[2] == var_wrnh
        for var_llti in var_wnki(4):
            if var_osiz[var_llti] + arg_xdvx[arg_dcmd] <= var_wrnh:
                var_osiz[var_llti] += arg_xdvx[arg_dcmd]
                if func_egyk(arg_dcmd + 1):
                    return True
                var_osiz[var_llti] -= arg_xdvx[arg_dcmd]
        return False
    return func_egyk(0)
