class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn:
        var_bacg[var_hqta]) ->var_bacg[var_hqta]:
        var_rgwu = var_wrnh(arg_xdvx)
        var_osiz = [(0) for var_ayzf in var_wnki(var_rgwu)]
        var_egyk = [(0) for var_ayzf in var_wnki(var_rgwu + 1)]
        var_dcmd = 0
        for var_llti in var_wnki(var_rgwu):
            var_egyk[arg_xdvx[var_llti]] += 1
            if var_egyk[arg_xdvx[var_llti]] == 2:
                var_dcmd += 1
            var_egyk[arg_rcsn[var_llti]] += 1
            if var_egyk[arg_rcsn[var_llti]] == 2:
                var_dcmd += 1
            var_osiz[var_llti] = var_dcmd
        return var_osiz
