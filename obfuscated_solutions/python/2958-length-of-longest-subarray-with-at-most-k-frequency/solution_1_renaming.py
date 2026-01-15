class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        var_rgwu, var_wrnh = 0, -1
        var_osiz = var_ayzf()
        for var_wnki in var_egyk(var_dcmd(arg_xdvx)):
            var_osiz[arg_xdvx[var_wnki]] += 1
            while var_osiz[arg_xdvx[var_wnki]] > arg_rcsn:
                var_wrnh += 1
                var_osiz[arg_xdvx[var_wrnh]] -= 1
            var_rgwu = var_llti(var_rgwu, var_wnki - var_wrnh)
        return var_rgwu
