class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rdmc[var_rjut]:
        var_bacg = []
        var_hqta = [0] * 26
        var_rgwu = [-1] * 26
        var_wrnh, var_osiz = 0, 0
        for var_ayzf, var_wnki in var_egyk(arg_xdvx):
            var_hqta[var_dcmd(var_wnki) - var_dcmd('a')] = var_ayzf
        for var_ayzf, var_wnki in var_egyk(arg_xdvx):
            var_llti = var_dcmd(var_wnki) - var_dcmd('a')
            if var_rgwu[var_llti] == -1:
                var_rgwu[var_llti] = var_ayzf
            if var_osiz < var_rgwu[var_llti]:
                var_bacg.append(var_osiz - var_wrnh + 1)
                var_wrnh = var_ayzf
                var_osiz = var_ayzf
            var_osiz = var_zbxo(var_osiz, var_hqta[var_llti])
        if var_osiz - var_wrnh + 1 > 0:
            var_bacg.append(var_osiz - var_wrnh + 1)
        return var_bacg
