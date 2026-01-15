class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        var_rgwu = var_wrnh()
        var_osiz = 0
        var_ayzf = -1
        var_wnki = 0
        for var_egyk in var_dcmd(var_llti(arg_xdvx)):
            if arg_xdvx[var_egyk] % 2 == 1:
                var_rgwu.append(var_egyk)
            if var_llti(var_rgwu) > arg_rcsn:
                var_ayzf = var_rgwu.popleft()
            if var_llti(var_rgwu) == arg_rcsn:
                var_wnki = var_rgwu[0] - var_ayzf
                var_osiz += var_wnki
        return var_osiz
