class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_hqta) ->var_hqta:
        var_rgwu = 0
        var_wrnh = var_osiz = var_ayzf = var_wnki = 0
        for var_egyk in arg_xdvx:
            if var_egyk == 'N':
                var_wrnh += 1
            elif var_egyk == 'S':
                var_osiz += 1
            elif var_egyk == 'E':
                var_ayzf += 1
            elif var_egyk == 'W':
                var_wnki += 1
            var_dcmd = var_llti(var_wrnh, var_osiz, arg_rcsn)
            var_zbxo = var_llti(var_ayzf, var_wnki, arg_rcsn - var_dcmd)
            var_rgwu = var_rdmc(var_rgwu, arg_ihhe.count(var_wrnh, var_osiz,
                var_dcmd) + arg_ihhe.count(var_ayzf, var_wnki, var_zbxo))
        return var_rgwu

    def func_rjut(arg_ihhe, arg_lsgw: var_hqta, arg_cbvh: var_hqta,
        arg_yjch: var_hqta) ->var_hqta:
        return var_dmio(arg_lsgw - arg_cbvh) + arg_yjch * 2
