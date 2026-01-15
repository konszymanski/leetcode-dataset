class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta, arg_rcsn: var_rgwu[var_hqta
        ], arg_bacg: var_rgwu[var_hqta]) ->var_cbvh:

        def func_wrnh():
            var_osiz = var_ayzf(arg_rcsn) | var_ayzf(arg_bacg)
            for var_wnki in var_egyk(arg_xdvx):
                if var_wnki not in var_osiz:
                    return var_wnki
            return -1
        var_dcmd = func_wrnh()
        if var_dcmd == -1:
            return False
        var_llti = {var_dcmd}
        var_zbxo = [var_dcmd]
        while var_zbxo:
            var_rdmc = var_zbxo.pop()
            for var_rjut in [arg_rcsn[var_rdmc], arg_bacg[var_rdmc]]:
                if var_rjut != -1:
                    if var_rjut in var_llti:
                        return False
                    var_zbxo.append(var_rjut)
                    var_llti.add(var_rjut)
        return var_lsgw(var_llti) == arg_xdvx
