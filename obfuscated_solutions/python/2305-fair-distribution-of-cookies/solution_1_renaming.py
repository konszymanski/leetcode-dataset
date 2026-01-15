class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        var_rgwu = [0] * arg_rcsn
        var_wrnh = var_osiz(arg_xdvx)

        def func_ayzf(arg_wnki, arg_egyk):
            if var_wrnh - arg_wnki < arg_egyk:
                return var_dcmd('inf')
            if arg_wnki == var_wrnh:
                return var_llti(var_rgwu)
            var_zbxo = var_dcmd('inf')
            for var_rdmc in var_rjut(arg_rcsn):
                arg_egyk -= var_hqta(var_rgwu[var_rdmc] == 0)
                var_rgwu[var_rdmc] += arg_xdvx[arg_wnki]
                var_zbxo = var_lsgw(var_zbxo, func_ayzf(arg_wnki + 1, arg_egyk)
                    )
                var_rgwu[var_rdmc] -= arg_xdvx[arg_wnki]
                arg_egyk += var_hqta(var_rgwu[var_rdmc] == 0)
            return var_zbxo
        return func_ayzf(0, arg_rcsn)
