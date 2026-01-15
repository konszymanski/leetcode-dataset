class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_rgwu
        ) ->var_hqta:
        var_wrnh = var_osiz(arg_xdvx)
        var_ayzf = []
        for var_wnki in var_egyk(var_wrnh):
            var_dcmd = arg_xdvx[var_wnki]
            var_llti = True
            for var_zbxo in var_egyk(var_wrnh):
                if var_zbxo == var_wnki:
                    continue
                if arg_xdvx[var_zbxo] == var_dcmd:
                    var_llti = False
                    break
            if var_llti:
                var_ayzf.append(var_dcmd)
        if var_osiz(var_ayzf) < arg_rcsn:
            return ''
        return var_ayzf[arg_rcsn - 1]
