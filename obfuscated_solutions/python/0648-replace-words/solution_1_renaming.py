class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        var_rgwu = arg_rcsn.split()
        var_wrnh = var_osiz(arg_xdvx)

        def func_ayzf(arg_wnki, var_wrnh):
            for var_egyk in var_dcmd(var_llti(arg_wnki)):
                var_zbxo = arg_wnki[0:var_egyk]
                if var_zbxo in var_wrnh:
                    return var_zbxo
            return arg_wnki
        for arg_wnki in var_dcmd(var_llti(var_rgwu)):
            var_rgwu[arg_wnki] = func_ayzf(var_rgwu[arg_wnki], var_wrnh)
        return ' '.join(var_rgwu)
