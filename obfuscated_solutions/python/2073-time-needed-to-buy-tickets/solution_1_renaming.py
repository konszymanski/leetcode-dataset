class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        var_rgwu = var_wrnh()
        for var_osiz in var_ayzf(var_wnki(arg_xdvx)):
            var_rgwu.append(var_osiz)
        var_egyk = 0
        while var_rgwu:
            var_egyk += 1
            var_dcmd = var_rgwu.popleft()
            arg_xdvx[var_dcmd] -= 1
            if arg_rcsn == var_dcmd and arg_xdvx[var_dcmd] == 0:
                return var_egyk
            if arg_xdvx[var_dcmd] != 0:
                var_rgwu.append(var_dcmd)
        return var_egyk
