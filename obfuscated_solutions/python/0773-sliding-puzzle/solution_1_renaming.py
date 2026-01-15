class Solution:
    var_udax = [[1, 3], [0, 2, 4], [1, 5], [0, 4], [3, 5, 1], [4, 2]]

    def func_ihhe(arg_xdvx, arg_rcsn: var_bacg[var_bacg[var_hqta]]) ->var_hqta:

        def func_rgwu(arg_wrnh, arg_osiz, arg_ayzf):
            arg_wrnh = var_wnki(arg_wrnh)
            arg_wrnh[arg_osiz], arg_wrnh[arg_ayzf] = arg_wrnh[arg_ayzf
                ], arg_wrnh[arg_osiz]
            return ''.join(arg_wrnh)
        var_egyk = ''.join(var_dcmd(var_llti) for var_zbxo in arg_rcsn for
            var_llti in var_zbxo)
        var_rdmc = {}

        def func_rjut(arg_lsgw, arg_cbvh, arg_yjch):
            if arg_lsgw in var_rdmc and var_rdmc[arg_lsgw] <= arg_yjch:
                return
            var_rdmc[arg_lsgw] = arg_yjch
            for var_dmio in arg_xdvx.directions[arg_cbvh]:
                var_ulfl = func_rgwu(arg_lsgw, arg_cbvh, var_dmio)
                func_rjut(var_ulfl, var_dmio, arg_yjch + 1)
        func_rjut(var_egyk, var_egyk.index('0'), 0)
        return var_rdmc.get('123450', -1)
