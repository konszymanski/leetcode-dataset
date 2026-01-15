class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]]) ->var_bacg:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = {}

        def func_osiz(arg_ayzf, arg_wnki):
            if arg_ayzf == var_hqta - 1:
                return arg_xdvx[arg_ayzf][arg_wnki]
            if (arg_ayzf, arg_wnki) in var_wrnh:
                return var_wrnh[arg_ayzf, arg_wnki]
            var_egyk = var_dcmd
            for var_llti in var_zbxo(var_hqta):
                if var_llti != arg_wnki:
                    var_egyk = var_rdmc(var_egyk, func_osiz(arg_ayzf + 1,
                        var_llti))
            var_wrnh[arg_ayzf, arg_wnki] = arg_xdvx[arg_ayzf][arg_wnki
                ] + var_egyk
            return var_wrnh[arg_ayzf, arg_wnki]
        var_rjut = var_dcmd
        for arg_wnki in var_zbxo(var_hqta):
            var_rjut = var_rdmc(var_rjut, func_osiz(0, arg_wnki))
        return var_rjut
