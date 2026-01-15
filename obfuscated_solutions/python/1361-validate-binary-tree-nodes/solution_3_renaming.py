class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta, arg_rcsn: var_rgwu[var_hqta
        ], arg_bacg: var_rgwu[var_hqta]) ->var_yjch:

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
        var_zbxo = var_rdmc([var_dcmd])
        while var_zbxo:
            var_rjut = var_zbxo.popleft()
            for var_lsgw in [arg_rcsn[var_rjut], arg_bacg[var_rjut]]:
                if var_lsgw != -1:
                    if var_lsgw in var_llti:
                        return False
                    var_zbxo.append(var_lsgw)
                    var_llti.add(var_lsgw)
        return var_cbvh(var_llti) == arg_xdvx
