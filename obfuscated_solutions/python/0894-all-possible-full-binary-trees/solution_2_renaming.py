class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_zbxo[var_wrnh]:
        if arg_xdvx % 2 == 0:
            return []
        var_bacg = [[] for var_hqta in var_rgwu(arg_xdvx + 1)]
        var_bacg[1].append(var_wrnh(0))
        for var_osiz in var_rgwu(3, arg_xdvx + 1, 2):
            for var_ayzf in var_rgwu(1, var_osiz - 1, 2):
                var_wnki = var_osiz - 1 - var_ayzf
                for var_egyk in var_bacg[var_ayzf]:
                    for var_dcmd in var_bacg[var_wnki]:
                        var_llti = var_wrnh(0, var_egyk, var_dcmd)
                        var_bacg[var_osiz].append(var_llti)
        return var_bacg[arg_xdvx]
