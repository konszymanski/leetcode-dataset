class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta, arg_rcsn: var_rgwu[var_hqta
        ], arg_bacg: var_hqta) ->var_dcmd:
        var_wrnh = 0
        var_osiz = arg_rcsn[var_wrnh]
        for var_ayzf in var_wnki(arg_bacg):
            if var_osiz <= arg_xdvx:
                var_wrnh += 1
                if var_wrnh == var_egyk(arg_rcsn):
                    return True
                else:
                    var_osiz = arg_rcsn[var_wrnh]
            else:
                var_osiz -= arg_xdvx
        return False

    def func_llti(arg_ihhe, arg_bacg: var_hqta, arg_rcsn: var_rgwu[var_hqta]
        ) ->var_hqta:
        var_zbxo = 0
        var_rdmc = var_rjut(arg_rcsn)
        while var_zbxo < var_rdmc:
            var_lsgw = (var_zbxo + var_rdmc) // 2
            if arg_ihhe.can_distribute(var_lsgw, arg_rcsn, arg_bacg):
                var_rdmc = var_lsgw
            else:
                var_zbxo = var_lsgw + 1
        return var_zbxo
