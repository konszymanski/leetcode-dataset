class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_rcsn[var_bacg]:
        var_hqta = []
        var_rgwu = var_wrnh(arg_xdvx)
        for var_osiz in var_ayzf(100, 1000, 2):
            var_wnki = var_wrnh([var_bacg(var_egyk) for var_egyk in
                var_dcmd(var_osiz)])
            if var_llti(var_rgwu[var_egyk] >= var_wnki[var_egyk] for
                var_egyk in var_wnki.keys()):
                var_hqta.append(var_osiz)
        return var_hqta
