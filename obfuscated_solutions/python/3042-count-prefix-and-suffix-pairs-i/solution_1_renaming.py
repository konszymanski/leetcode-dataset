class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_llti:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = 0
        for var_osiz in var_ayzf(var_hqta):
            for var_wnki in var_ayzf(var_osiz + 1, var_hqta):
                var_egyk = arg_xdvx[var_osiz]
                var_dcmd = arg_xdvx[var_wnki]
                if var_rgwu(var_egyk) > var_rgwu(var_dcmd):
                    continue
                if var_dcmd.startswith(var_egyk) and var_dcmd.endswith(var_egyk
                    ):
                    var_wrnh += 1
        return var_wrnh
