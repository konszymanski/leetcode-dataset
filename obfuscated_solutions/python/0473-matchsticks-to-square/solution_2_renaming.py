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
    var_osiz = {}

    def func_ayzf(arg_wnki, arg_egyk):
        var_dcmd = 0
        for var_llti in var_zbxo(var_rcsn - 1, -1, -1):
            if not arg_wnki & 1 << var_llti:
                var_dcmd += arg_xdvx[var_rcsn - 1 - var_llti]
        if var_dcmd > 0 and var_dcmd % var_wrnh == 0:
            arg_egyk += 1
        if arg_egyk == 3:
            return True
        if (arg_wnki, arg_egyk) in var_osiz:
            return var_osiz[arg_wnki, arg_egyk]
        var_rdmc = False
        var_rjut = var_lsgw(var_dcmd / var_wrnh)
        var_cbvh = var_wrnh * (var_rjut + 1) - var_dcmd
        for var_llti in var_zbxo(var_rcsn - 1, -1, -1):
            if arg_xdvx[var_rcsn - 1 - var_llti
                ] <= var_cbvh and arg_wnki & 1 << var_llti:
                if func_ayzf(arg_wnki ^ 1 << var_llti, arg_egyk):
                    var_rdmc = True
                    break
        var_osiz[arg_wnki, arg_egyk] = var_rdmc
        return var_rdmc
    return func_ayzf((1 << var_rcsn) - 1, 0)
