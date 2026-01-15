class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn:
        var_bacg[var_hqta]) ->var_bacg[var_hqta]:
        var_rgwu = var_wrnh(arg_xdvx)
        var_osiz = [0] * (var_rgwu + 1)
        for var_ayzf in arg_xdvx:
            var_osiz[var_ayzf] += 1
        var_wnki = []
        for var_egyk in arg_rcsn:
            while var_osiz[var_egyk] > 0:
                var_wnki.append(var_egyk)
                var_osiz[var_egyk] -= 1
        for var_dcmd in var_llti(var_rgwu + 1):
            while var_osiz[var_dcmd] > 0:
                var_wnki.append(var_dcmd)
                var_osiz[var_dcmd] -= 1
        return var_wnki
