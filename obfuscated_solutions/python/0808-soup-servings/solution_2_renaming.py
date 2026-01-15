class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_dcmd:
        var_bacg = var_hqta(arg_xdvx / 25)
        var_rgwu = var_wrnh.defaultdict(var_osiz)

        def func_ayzf(arg_wnki: var_rcsn, arg_egyk: var_rcsn) ->var_dcmd:
            if arg_wnki <= 0 and arg_egyk <= 0:
                return 0.5
            if arg_wnki <= 0:
                return 1.0
            if arg_egyk <= 0:
                return 0.0
            if arg_wnki in var_rgwu and arg_egyk in var_rgwu[arg_wnki]:
                return var_rgwu[arg_wnki][arg_egyk]
            var_rgwu[arg_wnki][arg_egyk] = (func_ayzf(arg_wnki - 4,
                arg_egyk) + func_ayzf(arg_wnki - 3, arg_egyk - 1) +
                func_ayzf(arg_wnki - 2, arg_egyk - 2) + func_ayzf(arg_wnki -
                1, arg_egyk - 3)) / 4.0
            return var_rgwu[arg_wnki][arg_egyk]
        for var_llti in var_zbxo(1, var_bacg + 1):
            if func_ayzf(var_llti, var_llti) > 1 - 1e-05:
                return 1.0
        return func_ayzf(var_bacg, var_bacg)
