class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_hqta[var_bacg]
        ) ->var_cbvh:
        var_rgwu, var_wrnh = var_osiz(arg_xdvx), var_ayzf(arg_rcsn)

        @var_lsgw
        def func_wnki(arg_egyk):
            if arg_egyk == var_rgwu:
                return 0
            var_dcmd = func_wnki(arg_egyk + 1) + 1
            for var_llti in var_zbxo(arg_egyk, var_rgwu):
                var_rdmc = arg_xdvx[arg_egyk:var_llti + 1]
                if var_rdmc in var_wrnh:
                    var_dcmd = var_rjut(var_dcmd, func_wnki(var_llti + 1))
            return var_dcmd
        return func_wnki(0)
