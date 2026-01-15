class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rdmc:
        var_bacg = [-1] * 26
        var_hqta = [-1] * 26
        for var_rgwu in var_wrnh(var_osiz(arg_xdvx)):
            var_ayzf = var_wnki(arg_xdvx[var_rgwu]) - var_wnki('a')
            if var_bacg[var_ayzf] == -1:
                var_bacg[var_ayzf] = var_rgwu
            var_hqta[var_ayzf] = var_rgwu
        var_egyk = 0
        for var_rgwu in var_wrnh(26):
            if var_bacg[var_rgwu] == -1:
                continue
            var_dcmd = var_llti()
            for var_zbxo in var_wrnh(var_bacg[var_rgwu] + 1, var_hqta[var_rgwu]
                ):
                var_dcmd.add(arg_xdvx[var_zbxo])
            var_egyk += var_osiz(var_dcmd)
        return var_egyk
