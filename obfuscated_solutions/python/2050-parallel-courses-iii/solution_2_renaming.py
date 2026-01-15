class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta, arg_rcsn: var_rgwu[var_rgwu
        [var_hqta]], arg_bacg: var_rgwu[var_hqta]) ->var_hqta:

        @var_llti
        def func_wrnh(arg_osiz):
            if not var_ayzf[arg_osiz]:
                return arg_bacg[arg_osiz]
            var_wnki = 0
            for var_egyk in var_ayzf[arg_osiz]:
                var_wnki = var_dcmd(var_wnki, func_wrnh(var_egyk))
            return arg_bacg[arg_osiz] + var_wnki
        var_ayzf = var_zbxo(var_rdmc)
        for var_rjut, var_lsgw in arg_rcsn:
            var_ayzf[var_rjut - 1].append(var_lsgw - 1)
        var_wnki = 0
        for arg_osiz in var_cbvh(arg_xdvx):
            var_wnki = var_dcmd(var_wnki, func_wrnh(arg_osiz))
        return var_wnki
