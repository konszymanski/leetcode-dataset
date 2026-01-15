class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rcsn:
        var_bacg = '#' + '#'.join(arg_xdvx) + '#'
        var_hqta = var_rgwu(var_bacg)
        var_wrnh = [0] * var_hqta
        var_osiz = var_ayzf = 0
        for var_wnki in var_egyk(var_hqta):
            var_dcmd = 2 * var_osiz - var_wnki
            if var_wnki < var_ayzf:
                var_wrnh[var_wnki] = var_llti(var_ayzf - var_wnki, var_wrnh
                    [var_dcmd])
            while var_wnki + 1 + var_wrnh[var_wnki
                ] < var_hqta and var_wnki - 1 - var_wrnh[var_wnki
                ] >= 0 and var_bacg[var_wnki + 1 + var_wrnh[var_wnki]
                ] == var_bacg[var_wnki - 1 - var_wrnh[var_wnki]]:
                var_wrnh[var_wnki] += 1
            if var_wnki + var_wrnh[var_wnki] > var_ayzf:
                var_osiz = var_wnki
                var_ayzf = var_wnki + var_wrnh[var_wnki]
        var_zbxo = var_rdmc(var_wrnh)
        var_rjut = var_wrnh.index(var_zbxo)
        var_lsgw = (var_rjut - var_zbxo) // 2
        var_cbvh = arg_xdvx[var_lsgw:var_lsgw + var_zbxo]
        return var_cbvh
