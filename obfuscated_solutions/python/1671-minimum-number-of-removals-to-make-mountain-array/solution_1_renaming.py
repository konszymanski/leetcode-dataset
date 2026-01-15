class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = [1] * var_hqta
        var_osiz = [1] * var_hqta
        for var_ayzf in var_wnki(var_hqta):
            for var_egyk in var_wnki(var_ayzf):
                if arg_xdvx[var_ayzf] > arg_xdvx[var_egyk]:
                    var_wrnh[var_ayzf] = var_dcmd(var_wrnh[var_ayzf], 
                        var_wrnh[var_egyk] + 1)
        for var_ayzf in var_wnki(var_hqta - 1, -1, -1):
            for var_egyk in var_wnki(var_ayzf + 1, var_hqta):
                if arg_xdvx[var_ayzf] > arg_xdvx[var_egyk]:
                    var_osiz[var_ayzf] = var_dcmd(var_osiz[var_ayzf], 
                        var_osiz[var_egyk] + 1)
        var_llti = var_zbxo('inf')
        for var_ayzf in var_wnki(var_hqta):
            if var_wrnh[var_ayzf] > 1 and var_osiz[var_ayzf] > 1:
                var_llti = var_rdmc(var_llti, var_hqta - var_wrnh[var_ayzf] -
                    var_osiz[var_ayzf] + 1)
        return var_llti
