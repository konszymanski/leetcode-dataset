class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = 0
        var_rgwu = {}
        var_wrnh = var_osiz(arg_xdvx)
        var_ayzf = 0
        var_wnki = var_osiz(var_egyk(arg_xdvx))
        for var_dcmd in var_llti(var_wrnh):
            if var_dcmd > 0:
                var_zbxo = arg_xdvx[var_dcmd - 1]
                var_rgwu[var_zbxo] -= 1
                if var_rgwu[var_zbxo] == 0:
                    var_rgwu.pop(var_zbxo)
            while var_ayzf < var_wrnh and var_osiz(var_rgwu) < var_wnki:
                var_rdmc = arg_xdvx[var_ayzf]
                var_rgwu[var_rdmc] = var_rgwu.get(var_rdmc, 0) + 1
                var_ayzf += 1
            if var_osiz(var_rgwu) == var_wnki:
                var_hqta += var_wrnh - var_ayzf + 1
        return var_hqta
