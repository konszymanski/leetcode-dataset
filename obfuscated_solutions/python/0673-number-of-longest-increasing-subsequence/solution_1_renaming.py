class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = [1] * var_hqta
        var_osiz = [1] * var_hqta
        for var_ayzf in var_wnki(var_hqta):
            for var_egyk in var_wnki(var_ayzf):
                if arg_xdvx[var_egyk] < arg_xdvx[var_ayzf]:
                    if var_wrnh[var_egyk] + 1 > var_wrnh[var_ayzf]:
                        var_wrnh[var_ayzf] = var_wrnh[var_egyk] + 1
                        var_osiz[var_ayzf] = 0
                    if var_wrnh[var_egyk] + 1 == var_wrnh[var_ayzf]:
                        var_osiz[var_ayzf] += var_osiz[var_egyk]
        var_dcmd = var_llti(var_wrnh)
        var_zbxo = 0
        for var_ayzf in var_wnki(var_hqta):
            if var_wrnh[var_ayzf] == var_dcmd:
                var_zbxo += var_osiz[var_ayzf]
        return var_zbxo
