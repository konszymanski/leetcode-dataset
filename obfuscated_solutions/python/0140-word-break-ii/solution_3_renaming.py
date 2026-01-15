class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_hqta[var_bacg]
        ) ->var_hqta[var_bacg]:
        var_rgwu = {}
        for var_wrnh in var_osiz(var_ayzf(arg_xdvx), -1, -1):
            var_wnki = []
            for var_egyk in var_osiz(var_wrnh, var_ayzf(arg_xdvx)):
                var_dcmd = arg_xdvx[var_wrnh:var_egyk + 1]
                if arg_ihhe.is_word_in_dict(var_dcmd, arg_rcsn):
                    if var_egyk == var_ayzf(arg_xdvx) - 1:
                        var_wnki.append(var_dcmd)
                    else:
                        var_llti = var_rgwu.get(var_egyk + 1, [])
                        for var_zbxo in var_llti:
                            var_wnki.append(var_dcmd + ' ' + var_zbxo)
            var_rgwu[var_wrnh] = var_wnki
        return var_rgwu.get(0, [])

    def func_rdmc(arg_ihhe, arg_rjut: var_bacg, arg_lsgw: var_hqta[var_bacg]
        ) ->var_cbvh:
        return arg_rjut in arg_lsgw
