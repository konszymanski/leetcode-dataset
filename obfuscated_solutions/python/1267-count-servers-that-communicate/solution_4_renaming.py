class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]]) ->var_bacg:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = var_rgwu(arg_xdvx[0])
        var_osiz = 0
        for var_ayzf in var_wnki(var_hqta):
            var_egyk = 0
            var_dcmd = -1
            for var_llti in var_wnki(var_wrnh):
                if arg_xdvx[var_ayzf][var_llti] == 1:
                    if var_egyk == 0:
                        var_dcmd = var_llti
                    var_egyk += 1
            var_zbxo = var_egyk != 1
            if not var_zbxo:
                for var_rdmc in var_wnki(var_hqta):
                    if var_rdmc != var_ayzf and arg_xdvx[var_rdmc][var_dcmd
                        ] == 1:
                        var_zbxo = True
                        break
            if var_zbxo:
                var_osiz += var_egyk
        return var_osiz
