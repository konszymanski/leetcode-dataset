class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_bacg) ->var_bacg:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = var_rgwu(arg_rcsn)
        var_osiz = [arg_rcsn[0:var_ayzf] for var_ayzf in var_wnki(var_wrnh + 1)
            ]
        for var_egyk in var_wnki(1, var_hqta + 1):
            var_dcmd = [arg_xdvx[0:var_egyk]] + [None for var_llti in
                var_wnki(var_wrnh)]
            for var_ayzf in var_wnki(1, var_wrnh + 1):
                if arg_xdvx[var_egyk - 1] == arg_rcsn[var_ayzf - 1]:
                    var_dcmd[var_ayzf] = var_osiz[var_ayzf - 1] + arg_xdvx[
                        var_egyk - 1]
                else:
                    var_zbxo = var_osiz[var_ayzf]
                    var_rdmc = var_dcmd[var_ayzf - 1]
                    var_dcmd[var_ayzf] = var_zbxo + arg_xdvx[var_egyk - 1
                        ] if var_rgwu(var_zbxo) < var_rgwu(var_rdmc
                        ) else var_rdmc + arg_rcsn[var_ayzf - 1]
            var_osiz = var_dcmd
        return var_osiz[var_wrnh]
