class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        if arg_rcsn <= 1:
            return 0
        var_rgwu = 0
        var_wrnh = 1
        var_osiz = 0
        for var_ayzf, var_wnki in var_egyk(arg_xdvx):
            var_wrnh *= var_wnki
            while var_wrnh >= arg_rcsn:
                var_wrnh //= arg_xdvx[var_osiz]
                var_osiz += 1
            var_rgwu += var_ayzf - var_osiz + 1
        return var_rgwu
